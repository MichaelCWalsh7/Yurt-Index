import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
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
@app.route("/home")
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
            if definition != "":
                uses.append(use)
            x += 1

        # initializes booleans to add to collection
        hasAltDefinitions = True if len(altDefinitions) > 1 else False
        hasAltSpellings = True if len(altSpellings) > 1 else False

        word = {
            "name": request.form.get("new_name"),
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

    return render_template("new_word.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# DO NOT FORGET TO DELETE THIS BEFORE DEPLOYMENT!!
err_Avoid = (
    env, redirect, request, session, url_for,
    ObjectId, generate_password_hash, check_password_hash)
