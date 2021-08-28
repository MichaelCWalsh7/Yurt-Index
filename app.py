import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    words = list(mongo.db.words.find().sort("rating", -1))
    return render_template("home.html", words=words)


@app.route("/words/<word_Id>")
def word_page(word_Id):
    # initializes variables needed to display a word
    word = mongo.db.words.find_one(
        {"_id": ObjectId(word_Id)}
    )
    created_by = word.get("createdBy")
    last_edited_by = word.get("lastEditedBy")
    user = mongo.db.users.find_one({
        "_id": created_by
    })
    last_edit = mongo.db.users.find_one({
        "_id": last_edited_by
    })

    # finds the rating id arrays to pass through the rating list function
    liked_ids = word.get("liked")
    disliked_ids = word.get("disliked")

    # runs the lists of ids through the function to get a list of names
    users_liked = rating_user_list(liked_ids)
    users_disliked = rating_user_list(disliked_ids)

    # Passes the tags ids through the get_tags funciton to display to user
    tags = get_tags(word_Id)
    return render_template(
        "word-page.html", word=word, user=user, last_edit=last_edit,
        liked=users_liked, disliked=users_disliked, tags=tags)


def get_tags(word_Id):
    word = mongo.db.words.find_one(
        {"_id": ObjectId(word_Id)}
    )
    tag_ids = word.get("tags")
    tags = []
    for tag_id in tag_ids:
        tag = mongo.db.tags.find_one({
            "_id": ObjectId(tag_id)
        })
        tags.append(tag)
    return tags


def rating_user_list(rating_list):
    users = []
    for rating_id in rating_list:
        user = mongo.db.users.find_one({
            "_id": ObjectId(rating_id)
            })
        username = user.get("name")
        users.append(username)
    return users


@app.route("/new_word", methods=["GET", "POST"])
def new_word():
    if request.method == "POST":
        # checks if the word already exists in the dictionary
        existing_word = mongo.db.words.find_one({
            "name": request.form.get("new_name").capitalize()
        })

        if existing_word:
            flash("This word already has an entry")
            return redirect(url_for("new_word"))

        # initializes variables to push to MongoDB
        alt_spellings = []
        alt_definitions = []
        uses = []
        editors = []
        liked = []
        disliked = []
        tag_ids = []
        user = mongo.db.users.find_one({
            "name": session["user"]
        })
        user_id = user.get("_id")
        date = datetime.now().date()

        # adds any additional spellings to the altSpellings list
        x = 1
        while x < 6:
            spelling = request.form.get(
                f"alt_spell_{x}")
            if spelling != "":
                alt_spellings.append(spelling)
            x += 1

        # adds any additional definitions to the altDefinitions list
        x = 1
        while x < 6:
            definition = request.form.get(
                f"alt_def_{x}")
            if definition != "":
                alt_definitions.append(definition)
            x += 1

        # adds inputted uses to the uses list
        required_Use = request.form.get("use")
        uses.append(required_Use)
        x = 1
        while x < 6:
            use = request.form.get(
                f"alt_use_{x}")
            if use != "":
                uses.append(use)
            x += 1

        # adds selected tags to the new tags list
        x = 1
        while x < 6:
            tag_name = request.form.get(f"tag_{x}")
            if tag_name is not None:
                selected_tag = mongo.db.tags.find_one(
                    {"name": tag_name}
                )
                tag_id = selected_tag.get("_id")
                if tag_id not in tag_ids:
                    tag_ids.append(ObjectId(tag_id))
            x += 1

        # initializes booleans and variables to add to collection
        is_tagged = True if len(tag_ids) >= 1 else False
        has_alt_definitions = True if len(alt_definitions) >= 1 else False
        has_alt_spellings = True if len(alt_spellings) >= 1 else False
        name = request.form.get("new_name").capitalize()

        # initializes dictionary variable and pushes it to MongoDB
        word = {
            "name": name,
            "hasAltSpellings": has_alt_spellings,
            "altSpellings": alt_spellings,
            "meaning": request.form.get("meaning"),
            "hasAltDefinitions": has_alt_definitions,
            "altDefinitions": alt_definitions,
            "uses": uses,
            "createdBy": user_id,
            "dateCreated": date.strftime("%-d-%b-%y"),
            "rating": 0,
            "starWord": False,
            "edited": False,
            "lastEditedBy": "",
            "lastEditedDate": "",
            "editors": editors,
            "liked": liked,
            "disliked": disliked,
            "isTagged": is_tagged,
            "tags": tag_ids
        }
        mongo.db.words.insert_one(word)
        flash("Yurt! Word Successfully Added!")

        # finds the id of the added word to add to the 'tags' collection
        if is_tagged:
            added_word = mongo.db.words.find_one({
                "name": name
            })
            added_word_id = added_word.get("_id")

            # pushes the word id to the 'tags' collection
            for tag in tag_ids:
                mongo.db.tags.update({"_id": ObjectId(tag)}, {"$push": {
                    "taggedWords": ObjectId(added_word_id)
                }})

        return redirect(url_for("word_page", word_Id=added_word_id))

    tags = list(mongo.db.tags.find().sort("name", 1))
    return render_template("new_word.html", tags=tags)


@app.route("/edit_word/<word_Id>", methods=["GET", "POST"])
def edit_word(word_Id):
    if request.method == "POST":
        # initialize variables to push to MongoDB
        alt_spellings = []
        alt_definitions = []
        uses = []
        word = mongo.db.words.find_one({
            "_id": ObjectId(word_Id)
        })
        user = mongo.db.users.find_one({
            "name": session["user"]
        })
        user_id = user.get("_id")
        editors = word.get("editors")
        date = datetime.now().date()

        # adds any additional spellings to the altSpellings list
        x = 1
        while x < 6:
            spelling = request.form.get(
                f"alt_spell_{x}")
            if spelling != "":
                alt_spellings.append(spelling)
            x += 1

        # adds any additional definitions to the altDefinitions list
        x = 1
        while x < 6:
            definition = request.form.get(
                f"alt_def_{x}")
            if definition != "":
                alt_definitions.append(definition)
            x += 1

        # adds inputted uses to the uses list
        required_Use = request.form.get("use")
        uses.append(required_Use)
        x = 1
        while x < 6:
            use = request.form.get(
                f"alt_use_{x}")
            if use != "":
                uses.append(use)
            x += 1

        # initializes booleans and variables to add to collection
        has_alt_definitions = True if len(alt_definitions) >= 1 else False
        has_alt_spellings = True if len(alt_spellings) >= 1 else False

        if user_id not in editors:
            editors.append(user_id)

        # finds out if the user changed any tags and makes a list of changes
        new_tag_names = []
        new_tag_ids = []
        x = 1
        while x < 6:
            new_tag_name = request.form.get(
                f"tag_{x}"
            )
            if (new_tag_name is not None) and (new_tag_name != "remove"):
                new_tag_names.append(new_tag_name)
            x += 1

        # checks if the user has tagged the word
        is_tagged = True if len(new_tag_names) >= 1 else False

        # finds out what previous tags were to delete them from tag
        # collection if necessary
        old_tags = []
        old_tag_id_strings = word.get("tags")
        for old_tag_string in old_tag_id_strings:
            old_tags.append(ObjectId(old_tag_string))

        # if word is tagged, finds those tag objects from the form names
        if is_tagged:
            for new_tag in new_tag_names:
                tag = mongo.db.tags.find_one({
                    "name": new_tag
                })
                # gets the id of all chosen tags
                tag_id = tag.get("_id")
                # adds the id the tag to a list if it isn't there already
                if tag_id not in new_tag_ids:
                    new_tag_ids.append(ObjectId(tag_id))
            # checks if there are any ids to remove from the tag's collection
            for old_tag in old_tags:
                if old_tag not in new_tag_ids:
                    # removes redundant words from tagged word array
                    mongo.db.tags.update({"_id": old_tag}, {"$pull": {
                        "taggedWords": ObjectId(word_Id)
                    }})

        mongo.db.words.update({"_id": ObjectId(word_Id)}, {"$set": {
            "hasAltSpellings": has_alt_spellings,
            "altSpellings": alt_spellings,
            "meaning": request.form.get("meaning"),
            "hasAltDefinitions": has_alt_definitions,
            "altDefinitions": alt_definitions,
            "uses": uses,
            "edited": True,
            "lastEditedBy": user_id,
            "lastEditedDate":  date.strftime("%-d-%b-%y"),
            "editors": editors,
            "isTagged": is_tagged,
            "tags": new_tag_ids
        }})

        # finds the id of the added word to add to the 'tags' collection
        if is_tagged:
            # pushes the word id to the 'tags' collection
            for new_tag_id in new_tag_ids:
                # generates a list of object ids associated with the word
                tag = mongo.db.tags.find_one({
                    "_id": new_tag_id
                })
                old_word_id_list = []
                old_word_ids = tag.get("taggedWords")
                for old_word_id in old_word_ids:
                    old_word_id_list.append(ObjectId(old_word_id))

                # checks if the current word is on that list
                if ObjectId(word_Id) not in old_word_id_list:
                    # if not the tag list is updated
                    mongo.db.tags.update(
                        {"_id": ObjectId(new_tag_id)}, {"$push": {
                            "taggedWords": ObjectId(word_Id)
                        }})
        flash("Word Successfully Updated!")
        return redirect(url_for("word_page", word_Id=word_Id))

    word = mongo.db.words.find_one({
        "_id": ObjectId(word_Id)
    })

    # initializes tags already selected for the word to prefill form
    selected_tags = []

    if word.get("isTagged") is True:
        selected_tag_ids = word.get("tags")
        for tag_id in selected_tag_ids:
            selected_tag = mongo.db.tags.find_one({
                "_id": ObjectId(tag_id)
            })
            selected_tags.append(selected_tag)

    all_tags = list(mongo.db.tags.find())
    return render_template(
        "edit_word.html", word=word, selected_tags=selected_tags,
        all_tags=all_tags)


@app.route("/rating_up/<username>/<word_id>", methods=["GET", "POST"])
def rating_up(word_id, username):
    # initializes variables to increment the rating
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    user = mongo.db.users.find_one({"name": username})
    user_id = ObjectId(user.get("_id"))
    old_rating = word.get("rating")
    new_rating = old_rating + 1
    liked = word.get("liked")
    disliked = word.get("disliked")

    # checks if the user has disliked the word, and if so removes them from
    # the disliked array
    if user_id in disliked:
        disliked.remove(user_id)
        new_rating = new_rating + 1

    if user_id in liked:
        return redirect(url_for('word_page', word_Id=word_id))

    # adds user's id to the like array
    liked.append(user_id)

    # updates the word entry on MongoDB
    mongo.db.words.update({"_id": ObjectId(word_id)}, {"$set": {
        "rating": new_rating,
        "liked": liked,
        "disliked": disliked
    }})

    return redirect(url_for('word_page', word_Id=word_id))


@app.route("/rating_down/<username>/<word_id>", methods=["GET", "POST"])
def rating_down(word_id, username):
    # initializes variables to increment the rating
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    user = mongo.db.users.find_one({"name": username})
    user_id = ObjectId(user.get("_id"))
    old_rating = word.get("rating")
    new_rating = old_rating - 1
    liked = word.get("liked")
    disliked = word.get("disliked")

    # checks if the user has liked the word, and if so removes them from
    # the liked array
    if user_id in liked:
        liked.remove(user_id)
        new_rating = new_rating - 1

    if user_id in disliked:
        return redirect(url_for('word_page', word_Id=word_id))

    # adds user's id to the disliked array
    disliked.append(user_id)

    # updates the word entry on MongoDB
    mongo.db.words.update({"_id": ObjectId(word_id)}, {"$set": {
        "rating": new_rating,
        "liked": liked,
        "disliked": disliked
    }})

    return redirect(url_for('word_page', word_Id=word_id))


@app.route("/unrate/<username>/<rating>/<word_id>", methods=["GET", "POST"])
def unrate(username, rating, word_id):
    # initializes vairables needed to unrate the word
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    user = mongo.db.users.find_one({"name": username})
    user_id = ObjectId(user.get("_id"))
    old_rate = word.get("rating")

    # checks if user had previoulsy liked or disliked the given word
    if rating == "up":
        rating_list = word.get("liked")

        # checks if user is still in the list in the case of a double-click
        if user_id in rating_list:
            # removes the user from the appropriate id array
            rating_list.remove(user_id)
            mongo.db.words.update({"_id": ObjectId(word_id)}, {"$set": {
                "liked": rating_list,
                "rating": old_rate - 1
            }})

    if rating == "down":
        rating_list = word.get("disliked")
        # checks if user is still in the list in the case of a double-click
        if user_id in rating_list:
            # removes the user from the appropriate id array
            rating_list.remove(user_id)
            mongo.db.words.update({"_id": ObjectId(word_id)}, {"$set": {
                "disliked": rating_list,
                "rating": old_rate + 1
            }})
    return redirect(url_for('word_page', word_Id=word_id))


@app.route("/add_tag/<username>", methods=["GET", "POST"])
def add_tag(username):
    if request.method == "POST":
        tags = []
        x = 1
        user = mongo.db.users.find_one({
            "name": username
        })
        user_id = user.get("_id")
        words = mongo.db.words.find().sort("rating", 1)
        date = datetime.now().date()

        while x < 5:
            tags.append(request.form.get(f"name-{x}").capitalize())
            x += 1
        for tag in tags:
            if tag != "":
                new_tag = {
                    "name": tag,
                    "createdBy": ObjectId(user_id),
                    "dateCreated": date.strftime("%-d-%b-%y"),
                    "taggedWords": []
                }
                mongo.db.tags.insert(new_tag)
        flash("Tag(s) Added Successfully!")
        return redirect(url_for('home_page', words=words))

    return render_template("add_tag.html")


@app.route("/delete_word/<word_Id>")
def delete_word(word_Id):
    mongo.db.words.remove({
        "_id": ObjectId(word_Id)
    })
    flash("Word Successfully Deleted")
    return redirect(url_for('home_page'))


@app.route("/all_words")
def all_words():
    words = mongo.db.words.find().sort("name", 1)
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    return render_template("all_words.html", words=words, letters=letters)


@app.route("/sort_all/<field>/<order>")
def sort_all(field, order):
    if order == '+':
        value = 1

    if order == '-':
        value = -1

    words = mongo.db.words.find().sort(field, value)
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    return render_template("all_words.html", words=words, letters=letters)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    words = list(mongo.db.words.find({
        "$text": {"$search": search}
    }))
    return render_template("search_results.html", words=words)


@app.route("/display_by_letter/<letter>")
def display_by_letter(letter):
    all_words = list(mongo.db.words.find().sort("name", 1))
    words = []
    current_letter = letter
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    for word in all_words:
        name = word.get("name")
        if name[0].lower() == letter.lower():
            words.append(word)
    return render_template('display_by_letter.html', words=words,
                           letters=letters, current_letter=current_letter)


@app.route("/display_by_tag/<tag_id>")
def display_by_tag(tag_id):
    # initialize a dictionary variable of the given tag
    tag = mongo.db.tags.find_one({
        "_id": ObjectId(tag_id)
    })

    # initialize a variable of all tags available for dropdown selector
    all_tags = list(mongo.db.tags.find())

    # form a list of the words(dictionaries) associated with the tag
    word_ids = tag.get("taggedWords")
    words = []
    for word_id in word_ids:
        word = mongo.db.words.find_one({
            "_id": ObjectId(word_id)
        })
        words.append(word)

    return render_template(
        "display_by_tag.html", tag=tag, words=words, all_tags=all_tags)


@app.route("/sort_letters/<letter>/<field>/<order>")
def sort_letters(letter, field, order):
    # determines if the words will be sorted ascendingly or descendingly
    if order == '+':
        value = 1

    if order == '-':
        value = -1

    all_words = mongo.db.words.find().sort(field, value)
    words = []
    current_letter = letter
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    for word in all_words:
        name = word.get("name")
        if name[0].lower() == letter.lower():
            words.append(word)
    return render_template('display_by_letter.html', words=words,
                           letters=letters, current_letter=current_letter)


@app.route("/sort_tags/<tag_id>/<field>/<order>")
def sort_tags(tag_id, field, order):
    # determines if the words will be sorted ascendingly or descendingly
    if order == '+':
        value = 1

    if order == '-':
        value = -1

    # initializes the tag variable for display to the user
    tag = mongo.db.tags.find_one({
        "_id": ObjectId(tag_id)
    })

    # initializes a sorted list of words to display
    words = list(mongo.db.words.find(
        {"tags": ObjectId(tag_id)}).sort(field, value)
        )

    return render_template("display_by_tag.html", tag=tag, words=words)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists already
        existing_user = mongo.db.users.find_one(
            {"name": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry! That username is taken!")
            return redirect(url_for("register"))

        date = datetime.now().date()

        new_user = {
            "name": request.form.get("username").lower(),
            "description": "",
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "dateOfBirth": request.form.get("date_of_birth"),
            "dateJoined": date.strftime("%-d-%b-%y"),
            "country": "",
            "city": "",
            "isAdmin": False,
            "wordsCreated": [],
            "wordsEdited": []
        }

        mongo.db.users.insert_one(new_user)

        # put the new user into session cookie
        session["user"] = request.form.get("name")
        flash("Yurt! You've Been Registered Successfully!")
        return redirect(url_for('log_in'))

    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"name": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = existing_user.get("name")
                session["admin"] = existing_user.get("isAdmin")
                user_id = str(ObjectId(existing_user.get("_id")))
                session["id"] = user_id
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    'profile', user_id=session["id"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/log_out")
def log_out():
    # remove user from session cookies
    flash("You are now logged out")
    session.clear()
    return redirect(url_for("log_in"))


@app.route("/profile/<user_id>")
def profile(user_id):
    user = mongo.db.users.find_one(
        {"_id": ObjectId(user_id)}
    )
    # Finds what words the user has created to display on their profile
    created_words = mongo.db.words.find(
        {"createdBy": ObjectId(user_id)}
    )
    # Finds what words the user has edited to display on their profile
    edited_words = mongo.db.words.find(
        {"editors": ObjectId(user_id)}
    )
    user_id_string = str(user_id)
    return render_template(
        "profile.html", user=user, created_words=created_words,
        edited_words=edited_words, user_id_string=user_id_string)


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if request.method == "POST":
        description = request.form.get("description")
        country = request.form.get("country")
        city = request.form.get("city")
        has_description = True if description != "" else False
        has_country = True if country != "" else False
        has_city = True if city != "" else False

        mongo.db.users.update({"name": username}, {"$set": {
            "description": description,
            "country": country,
            "city": city,
            "hasDescription": has_description,
            "hasCountry": has_country,
            "hasCity": has_city
        }})
        return redirect(url_for('profile', username=username))

    user = mongo.db.users.find_one(
        {"name": username}
    )
    return render_template("edit_profile.html", user=user)


@app.errorhandler(404)
def error404(e):
    return render_template("404.html")


@app.errorhandler(500)
def error500(e):
    return render_template("500.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# DO NOT FORGET TO DELETE THIS BEFORE DEPLOYMENT!!
err_Avoid = env
