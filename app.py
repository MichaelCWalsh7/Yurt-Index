import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    words = list(mongo.db.words.find())
    return render_template("home.html", words=words)


@app.route("/words/<word_Id>")
def word_page(word_Id):
    word = mongo.db.words.find_one(
        {"_id": ObjectId(word_Id)}
    )
    return render_template("word-page.html", word=word)


@app.route("/new_word", methods=["GET", "POST"])
def new_word():
    if request.method == "POST":
        altSpellings = []
        altDefinitions = []
        uses = []

        # adds any additional spellings to the altSpellings list
        x = 1
        while x < 6:
            spelling = request.form.get(
                f"alt_spell_{x}")
            if spelling != "":
                altSpellings.append(spelling)
            x += 1

        # adds any additional definitions to the altDefinitions list
        x = 1
        while x < 6:
            definition = request.form.get(
                f"alt_def_{x}")
            if definition != "":
                altDefinitions.append(definition)
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
        hasAltDefinitions = True if len(altDefinitions) > 1 else False
        hasAltSpellings = True if len(altSpellings) > 1 else False
        name = request.form.get("new_name").capitalize()

        # initializes dictionary variable and pushe to MongoDB
        word = {
            "name": name,
            "hasAltSpellings": hasAltSpellings,
            "altSpellings": altSpellings,
            "meaning": request.form.get("meaning"),
            "hasAltDefinitions": hasAltDefinitions,
            "altDefinitions": altDefinitions,
            "uses": uses,
            "createdBy": "placeholder",
            "dateCreated": "placeholder",
            "rating": 0,
            "starWord": False,
            "edited": False,
            "lastEditedBy": "",
            "lastEditedDate": ""
        }
        mongo.db.words.insert_one(word)
        flash("Yurt! Word Successfully Added!")
        return redirect(url_for("home_page"))

    return render_template("new_word.html")


@app.route("/edit_word/<word_Id>", methods=["GET", "POST"])
def edit_word(word_Id):
    if request.method == "POST":
        altSpellings = []
        altDefinitions = []
        uses = []
        word = mongo.db.words.find_one({
            "_id": ObjectId(word_Id)
        })
        rating = word.get('rating')

        # adds any additional spellings to the altSpellings list
        x = 1
        while x < 6:
            spelling = request.form.get(
                f"alt_spell_{x}")
            if spelling != "":
                altSpellings.append(spelling)
            x += 1

        # adds any additional definitions to the altDefinitions list
        x = 1
        while x < 6:
            definition = request.form.get(
                f"alt_def_{x}")
            if definition != "":
                altDefinitions.append(definition)
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
        hasAltDefinitions = True if len(altDefinitions) > 1 else False
        hasAltSpellings = True if len(altSpellings) > 1 else False
        name = request.form.get("name").capitalize()

        # initializes dictionary variable and pushe to MongoDB
        word_edit = {
            "name": name,
            "hasAltSpellings": hasAltSpellings,
            "altSpellings": altSpellings,
            "meaning": request.form.get("meaning"),
            "hasAltDefinitions": hasAltDefinitions,
            "altDefinitions": altDefinitions,
            "uses": uses,
            "createdBy": "placeholder",
            "dateCreated": "placeholder",
            "rating": rating,
            "starWord": False,
            "edited": True,
            "lastEditedBy": "placeholder",
            "lastEditedDate": "placeholder"
        }

        mongo.db.words.update({"_id": ObjectId(word_Id)}, word_edit)
        flash("Word Successfully Updated!")
        return redirect(url_for("word_page", word_Id=word_Id))

    word = mongo.db.words.find_one({
        "_id": ObjectId(word_Id)
    })
    return render_template("edit_word.html", word=word)


@app.route("/delete_word/<word_Id>")
def delete_word(word_Id):
    mongo.db.words.remove({
        "_id": ObjectId(word_Id)
    })
    flash("Word Successfully Deleted")
    return redirect(url_for('home_page'))


@app.route("/all_words")
def all_words():
    words = list(mongo.db.words.find().sort("name", 1))
    return render_template("all_words.html", words=words)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    words = list(mongo.db.words.find({
        "$text": {"$search": search}
    }))
    return render_template("search_results.html", words=words)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists already
        existing_user = mongo.db.users.find_one(
            {"name": request.form.get("username").lower()})
        if existing_user:
            flash("Sorry! That username is taken!")
            return redirect(url_for("register"))

        new_user = {
            "name": request.form.get("username"),
            "description": "",
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "dateOfBirth": request.form.get("date_of_birth"),
            "dateJoined": "placeholder",
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
        return redirect(url_for('home_page'))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# DO NOT FORGET TO DELETE THIS BEFORE DEPLOYMENT!!
err_Avoid = (
    env, redirect, request, session, url_for,
    ObjectId, generate_password_hash, check_password_hash)
