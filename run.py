import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# To load home page
@app.route("/")
@app.route("/get_review")
def get_review():
    reviews = list(mongo.db.review.find().sort("_id", -1).limit(3))
    return render_template("review.html", reviews=reviews)


# To load page displaying all reviews
@app.route("/all_reviews")
def all_reviews():
    reviews = list(mongo.db.review.find().sort("_id", -1))
    return render_template("all_reviews.html", reviews=reviews)


# Function to search through reviews
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.review.find({"$text": {"$search": query}}))
    return render_template("all_reviews.html", reviews=reviews)


# Function to register for the site
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # To see if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Allocates user to cookie "session"
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Function to login tp the site
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username is already registered and stored within database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password match password input from user
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # when password is incorrect/does not match hashed password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist within the database
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# To load the profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        reviews = list(mongo.db.review.find().sort("_id", -1))
        return render_template("profile.html", username=username,
                               reviews=reviews)
    return redirect(url_for("login"))


# Function to logout from the site
@app.route("/logout")
def logout():
    # Removes the user from the cookie "session"
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Function to add a new review
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "restaurant_name": request.form.get("restaurant_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "restaurant_location": request.form.get("restaurant_location"),
            "starter_description": request.form.get("starter_description"),
            "main_description": request.form.get("main_description"),
            "dessert_description": request.form.get("dessert_description"),
            "drink_description": request.form.get("drink_description"),
            "date_visited": request.form.get("date_visited"),
            "overall_rating": request.form.get("overall_rating"),
            "overall_comments": request.form.get("overall_comments"),
            "created_by": session["user"]
        }
        mongo.db.review.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_review"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    ratings = mongo.db.ratings.find()
    return render_template("add_review.html", cuisines=cuisines,
                           ratings=ratings)


# Function to edit a review
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {"$set": {
            "restaurant_name": request.form.get("restaurant_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "restaurant_location": request.form.get("restaurant_location"),
            "starter_description": request.form.get("starter_description"),
            "main_description": request.form.get("main_description"),
            "dessert_description": request.form.get("dessert_description"),
            "drink_description": request.form.get("drink_description"),
            "date_visited": request.form.get("date_visited"),
            "overall_rating": request.form.get("overall_rating"),
            "overall_comments": request.form.get("overall_comments"),
            "created_by": session["user"]
        }
        }
        mongo.db.review.update_one({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.review.find_one({"_id": ObjectId(review_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    ratings = mongo.db.ratings.find()
    return render_template(
        "edit_review.html", review=review,
        cuisines=cuisines, ratings=ratings)


# Function to delete a review from the site
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.review.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_review"))


# To load the cuisine page
@app.route("/get_cuisines")
def get_cuisines():
    cuisines = list(mongo.db.cuisines.find().sort("initial_order", 1))
    return render_template("cuisines.html", cuisines=cuisines)


# Function to logout from the site
@app.route("/get_specific_cuisines/<cuisine_name>")
def get_specific_cuisines(cuisine_name):
    reviews = list(mongo.db.review.find
                   ({'cuisine_name': cuisine_name}).sort("_id", -1))
    return render_template("specific_cuisine.html", reviews=reviews,
                           cuisine_name=cuisine_name)


# To load 404 error page
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


# To load 500 error page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html", error=error)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
