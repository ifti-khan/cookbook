import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING, ASCENDING
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import math

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks to see if the username already exists within the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("account", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    fullname = mongo.db.users.find_one(
        {"username": session["user"]})["fullname"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    password = mongo.db.users.find_one(
        {"username": session["user"]})["password"]
    user_recipes = mongo.db.recipes.find({'created_by': username})
    num_of_user_recipes = user_recipes.count()
    return render_template(
        "account.html", username=username, fullname=fullname,
        email=email, password=password,
        user_recipes=user_recipes,
        num_of_user_recipes=num_of_user_recipes)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/all_recipes")
def all_recipes():
    num_of_recipes = mongo.db.recipes.count()
    cards_per_page = 4
    current_page = int(request.args.get('current_page', 1))
    num_of_pages = range(1, int(
        math.ceil(num_of_recipes / cards_per_page)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_page - 1)*cards_per_page).limit(cards_per_page)

    return render_template(
        "recipes.html", recipes=recipes, current_page=current_page,
        num_of_pages=num_of_pages, num_of_recipes=num_of_recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_image_url": request.form.get("recipe_image_url"),
            "recipe_meal_type": request.form.get("recipe_meal_type"),
            "recipe_cuisine_type": request.form.get("recipe_cuisine_type"),
            "recipe_diet_type": request.form.get("recipe_diet_type"),
            "recipe_cooktime": request.form.get("recipe_cooktime"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.get(
                "recipe_ingredients").splitlines(),
            "recipe_steps": request.form.get("recipe_steps").splitlines(),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("all_recipes"))

    meals = mongo.db.meals.find().sort("meal_name", 1)
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)
    return render_template(
        "add_recipe.html", meals=meals, cuisines=cuisines, diets=diets)


@app.route("/search", methods=["GET", "POST"])
def search():
    num_of_recipes = mongo.db.recipes.count()
    mongo.db.recipes.create_index([("$**", 'text')])
    query = request.form.get("search_query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    num_of_recipes_search = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    search_results = f"Search Results ({num_of_recipes_search})"
    return render_template(
        "recipes.html", num_of_recipes=num_of_recipes, recipes=recipes,
        num_of_recipes_search=num_of_recipes_search,
        search_results=search_results)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    recipe_info = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "view_recipe.html", recipe_info=recipe_info)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
