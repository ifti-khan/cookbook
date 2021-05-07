import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, ASCENDING
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

import math

app = Flask(__name__)
# Config settings and environmental variables located in env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    '''
    INFO.
    This is the app route for the first
    page that loads which in the index.html
    '''
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    INFO.
    This app route is for the registration page which will allow
    a user to create an account using the registration form.
    It will pull all the user information provided within the
    registration form and then insert it into the MongoDB
    users collection
    '''
    # This will check to see if the user is already logged in and
    # redirect them if they are already logged in
    if 'user' in session:
        flash('You have already registered and have logged in')
        return redirect(url_for('account', username=session["user"]))

    if request.method == "POST":
        # Checks to see if the username already exists within the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username chosen already exists then it will
        # alert the user with a message and redirect them to the
        # registration page
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # This dictionary will be used handle the information from the
        # register form and put into dictionary items and then inserted into
        # the users collection in MongoDB
        register = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            # Converts the string input from the user to a hash to keep
            # the users password secure
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie call user and
        # alerts the user that the registration was successful and
        # redirects them to there account page
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    INFO.
    This app route is for the login page which will allow
    a user to login into the website using the login form.
    If the correct details are entered the user will be taken
    to there account page.
    '''
    # This will check to see if the user is already logged in
    # and if they are it will redirect them to there account page
    if 'user' in session:
        flash('You have already logged in')
        return redirect(url_for('account', username=session["user"]))

    if request.method == "POST":
        # This checks to see if the username exists in user collection
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username is in the user collection, it will check the
        # hashed password matches, put the users username into a session
        # cookie, flash them a welcome message using there username and
        # redirect them to there account page.
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("account", username=session["user"]))
            else:
                # If the hashed password does not match this
                # flash message will display and redirect the user
                # back to the login form
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If the username input does not exist within the
            # user collection, then this flash message will display
            # to the user and redirect them back to the login form
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    '''
    INFO.
    This app route is for the account page and will get
    all the users info provided from the users collection.
    From here a user can change see how many recipes they
    have created and stored.
    '''

    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to access a account')
        return redirect(url_for('index'))

    # This uses the session user to get the username
    # from the user collection within MongoDB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Same as above but this get the users fullname
    fullname = mongo.db.users.find_one(
        {"username": session["user"]})["fullname"]
    # Same as above but this get the users email
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    # This finds all recipes created by a specic user
    # using the users session username
    user_recipes = mongo.db.recipes.find({'created_by': username})
    # This counts how many recipes the user has created
    num_of_user_recipes = user_recipes.count()
    # This is passing the varibles into the template, so
    # they can be used in the rendered page
    return render_template(
        "account.html", username=username, fullname=fullname,
        email=email, user_recipes=user_recipes,
        num_of_user_recipes=num_of_user_recipes)


@app.route("/logout")
def logout():
    '''
    INFO.
    This app route is to help users logout once
    they have logged in.
    '''
    # This removes the user from session cookie and
    # redirects the user to the login page and informs
    # the user that they have been logged out.
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/all_recipes")
def all_recipes():
    '''
    INFO.
    This app route is for the all recipes page and
    pagination for the all recipe page.
    '''
    # This will return a number of how many recipes
    # are in the recipe collection
    num_of_recipes = mongo.db.recipes.count()
    # How many recipe cards will display on the page
    cards_per_page = 8
    # This block of code here calculates using multiple
    # variables for the page pagination
    current_page = int(request.args.get('current_page', 1))
    num_of_pages = range(1, int(
        math.ceil(num_of_recipes / cards_per_page)) + 1)
    recipes = mongo.db.recipes.find().sort([('_id', ASCENDING)]).skip(
        (current_page - 1)*cards_per_page).limit(cards_per_page)

    # This is passing the varibles into the template, so
    # they can be used in the rendered page
    return render_template(
        "recipes.html", recipes=recipes, current_page=current_page,
        num_of_pages=num_of_pages, num_of_recipes=num_of_recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    '''
    INFO.
    This app route is for the add recipe form, it will take
    the data the add recipe form, put into a dictionary. Then
    insert the data from the dictionary into the recipes collection.
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to add a recipe')
        return redirect(url_for('index'))

    if request.method == "POST":
        # This dictionary will be used handle the information from the
        # register form and put into dictionary items and then inserted into
        # the recipes collection in MongoDB
        add_recipe = {
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
        # Once inserted into recipes collection a message will appear informing
        # the user they have successfully added a recipe to the collection
        mongo.db.recipes.insert_one(add_recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("all_recipes"))

    # These variables take data from the assigned collection
    # and they fill within the assigned dropdown list
    meals = mongo.db.meals.find().sort("meal_name", 1)
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)

    # This is passing the varibles into the template, so
    # they can be used in the rendered page
    return render_template(
        "add_recipe.html", meals=meals, cuisines=cuisines, diets=diets)


@app.route("/search", methods=["GET", "POST"])
def search():
    '''
    This app route is for the search a recipe located
    within the all recpe page. This will allow a user to
    search any recipe with the database using any word.
    '''
    num_of_recipes = mongo.db.recipes.count()
    # This creates a wild card index for the search
    mongo.db.recipes.create_index([("$**", 'text')])
    # assign the var query to the search input
    # in the search form.
    query = request.form.get("search_query")
    # using the query and index it will find in the recipe
    # collection what the user is searching for
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    num_of_recipes_search = mongo.db.recipes.find(
        {'$text': {'$search': query}}).count()
    # displaying a search result string to the user after there search
    search_results = f"Search Results ({num_of_recipes_search})"

    # This is passing the varibles into the template, so
    # they can be used in the rendered page
    return render_template(
        "recipes.html", num_of_recipes=num_of_recipes, recipes=recipes,
        num_of_recipes_search=num_of_recipes_search,
        search_results=search_results)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    '''
    INFO.
    This app route is for the view recipe page using the recipe ID
    as a parameter so when a user clicks on a recipe card it will
    take them to this page and allow them to view the recipe in greater detail.
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to view a recipe in detail')
        return redirect(url_for('index'))

    # assigning recipe_info var to recipe ids within the recipes collection
    # to then be later used in the HTML to display values.
    recipe_info = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "view_recipe.html", recipe_info=recipe_info)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    '''
    INFO.
    This app route is for the edit recipe page using the recipe ID as
    a parameter where a user can only edit there own recipes that they
    created and no on elses.
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to edit a recipe')
        return redirect(url_for('index'))

    if request.method == "POST":
        # This creates a dictionary and gets the data
        # from the update recipe form.
        edit_recipe = {
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
        # when the data is submitted it is then updated
        # within the recipe collection and then displaying a message
        # to the user.
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("all_recipes"))

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # These variables take data from the assigned collection
    # and they fill within the assigned dropdown list
    meals = mongo.db.meals.find().sort("meal_name", 1)
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    diets = mongo.db.diets.find().sort("diet_name", 1)

    # This is passing the varibles into the template, so
    # they can be used in the rendered page
    return render_template(
        "edit_recipe.html", recipes=recipes, meals=meals,
        cuisines=cuisines, diets=diets)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    '''
    INFO.
    This app route is for delete a recipe which uses the
    recipe ID as a parameter but only a logged in user and
    recipe creator can delete a recipe
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to delete a recipe')
        return redirect(url_for('index'))

    # When a user clicks delete, it will delete that recipe using
    # the recipe ID and display a message to the user and redirect
    # them to there account page.
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("account", username=session['user']))


@app.route("/change_username/<username>", methods=["GET", "POST"])
def change_username(username):
    '''
    INFO.
    This app route is for the change username page using the
    username as a parameter. This will allow the logged in user
    to change there username which also changes that users recipe
    created by name as well to the new username.
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to change a username')
        return redirect(url_for('index'))

    if request.method == "POST":
        # These variables are used to change the created by value
        # within the recipes collection
        current_user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        change_created_by = {
            "created_by": request.form.get("new_username")}
        created_by_check = mongo.db.recipes.find(
            {'created_by': current_user})

        # This if checks the recipes collection to see if there
        # are any created recipes by the logged in user and
        # if true update them to the new username
        if created_by_check:
            mongo.db.recipes.update_many(
                {"created_by": username},
                {"$set": change_created_by})

        # These variables are used to change the
        # current user username
        change_username = {
            "username": request.form.get("new_username")}
        username_check = mongo.db.users.find_one(
            {'username': request.form.get('new_username')})

        # This if checks to see if the username is already taken
        # within the users collection and if true then redirect
        # the user and inform them username is taken
        if username_check:
            flash('This username is taken by another user,\
                Please type a new unique username')
            return redirect(url_for(
                'change_username', username=session["user"]))
        else:
            # if the check is false it will then update only
            # the username within the users collection and inform
            # the user of the change
            mongo.db.users.update_one(
                {"username": username}, {"$set": change_username})

        flash("Username has been changed,\
            Remember to login with your new username")
        session.pop("user")
        return redirect(url_for("login"))

    return render_template("change_username.html", username=session["user"])


@app.route("/change_password/<username>", methods=["GET", "POST"])
def change_password(username):
    '''
    INFO.
    This app route is for the change password page using the
    username as a parameter. This will allow the logged in user
    to change there password.
    '''
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('You must register or login, to change a password')
        return redirect(url_for('index'))

    if request.method == "POST":
        # Storing the user session into a variable
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Assigning variables to the form input fields
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get("confirm_password")

        # This checks to see if the current password in the db
        # matches the typed current password by the user
        if check_password_hash(mongo.db.users.find_one(
                {'username': username})['password'], current_password):
            # This checks to see if the new password and
            # confirm password match and if they do it will
            # update the password only in the collection
            if new_password == confirm_password:
                mongo.db.users.update_one(
                    {"username": username},
                    {"$set": {'password': generate_password_hash(
                        new_password)}})
                # Informing the user that the password has changed
                flash("Your password has been changed.")
                return redirect(url_for('account', username=username))
            else:
                # Informing the user that the new and confirm
                # password do not match
                flash("Your passwords do not match,\
                    Please try again and make sure both passwords match")
                return redirect(url_for("change_password",
                                        username=session["user"]))
        else:
            # Informing the user that the current password
            # entered does not match
            flash('Your Current password is incorrect,\
                Please try again and type the correct password')
            return redirect(url_for('change_password',
                            username=session["user"]))

    return render_template("change_password.html", username=session["user"])


'''Admin Section'''


'''Add Meal Type Section'''


@app.route("/manage_meals")
def get_meals():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    # This get all the meal types from the meal db
    # and sorts them alphabetically
    meals = list(mongo.db.meals.find().sort("meal_name", 1))
    return render_template("admin/manage_meals.html", meals=meals,
                           username=username)


@app.route("/add_meal", methods=["GET", "POST"])
def add_meal():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the add new meal form
        # and put it into a dictionary
        new_meal = {
            "meal_name": request.form.get("new_meal_name")
        }
        # This then adds the above dictionary into the meals db,
        # and a message is displayed when meal type is added and
        # redirects them to the manage page
        mongo.db.meals.insert_one(new_meal)
        flash("New Meal Type Added")
        return redirect(url_for("get_meals"))

    return render_template("admin/add_meals.html")


@app.route("/edit_meal/<meal_id>", methods=["GET", "POST"])
def edit_meals(meal_id):
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the edit meal form
        # and put it into a dictionary
        edit_meal = {
            "meal_name": request.form.get("new_meal_name")
        }
        # This then uses the above dictionary and updates
        # the meal type with the meals db,
        # and a message is displayed when the meal type is updated and
        # redirects admin to the manage page
        mongo.db.meals.update({"_id": ObjectId(meal_id)}, edit_meal)
        flash("Meal Has Been Updated")
        return redirect(url_for("get_meals"))

    meals = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    return render_template("admin/edit_meals.html", meals=meals)


@app.route("/delete_meal/<meal_id>")
def delete_meals(meal_id):
    # This allows the admin to delete a meal type using
    # that meals type unique id, once done a message
    # will display and redirect admin to the manage page
    mongo.db.meals.remove({"_id": ObjectId(meal_id)})
    flash("Meal Has Been Deleted")
    return redirect(url_for("get_meals"))


'''Add Cuisine Type Section'''


@app.route("/manage_cuisines")
def get_cuisines():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    # This get all the cuisine types from the cuisines db
    # and sorts them alphabetically
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    return render_template("admin/manage_cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the add new cuisine form
        # and put it into a dictionary
        new_cuisine = {
            "cuisine_name": request.form.get("new_cuisine_name")
        }
        # This then adds the above dictionary into the cuisine db,
        # and a message is displayed when cuisine type is added and
        # redirects them to the manage page
        mongo.db.cuisines.insert_one(new_cuisine)
        flash("New Cuisine Type Added")
        return redirect(url_for("get_cuisines"))

    return render_template("admin/add_cuisines.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisines(cuisine_id):
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the update cuisine form
        # and put it into a dictionary
        edit_cuisine = {
            "cuisine_name": request.form.get("new_cuisine_name")
        }
        # This then uses the above dictionary and updates
        # the cuisine type within the cuisines db,
        # and a message is displayed when the cuisine type is updated and
        # redirects admin to the manage page
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, edit_cuisine)
        flash("Cuisine Has Been Updated")
        return redirect(url_for("get_cuisines"))

    cuisines = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("admin/edit_cuisines.html", cuisines=cuisines)


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisines(cuisine_id):
    # This allows the admin to delete a cuisine type using
    # that cuisines type unique id, once done a message
    # will display and redirect admin to the manage page
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Has Been Deleted")
    return redirect(url_for("get_cuisines"))


'''Add Diet Type Section'''


@app.route("/manage_diets")
def get_diets():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    # This get all the diet types from the diets db
    # and sorts them alphabetically
    diets = list(mongo.db.diets.find().sort("diet_name", 1))
    return render_template("admin/manage_diets.html", diets=diets)


@app.route("/add_diet", methods=["GET", "POST"])
def add_diet():
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the add new diet form
        # and put it into a dictionary
        new_diet = {
            "diet_name": request.form.get("new_diet_name")
        }
        # This then adds the above dictionary into the diets db,
        # and a message is displayed when diet type is added and
        # redirects them to the manage page
        mongo.db.diets.insert_one(new_diet)
        flash("New Diet Type Added")
        return redirect(url_for("get_diets"))

    return render_template("admin/add_diets.html")


@app.route("/edit_diet/<diet_id>", methods=["GET", "POST"])
def edit_diets(diet_id):
    # This prevents users who are not registered or logged in,
    # from viewing certain pages and forms
    if 'user' not in session:
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for('index'))

    # This prevents logged in users who are not admin to
    # view this page and redirects them to there account page
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if not username == "admin":
        flash('Only Site Administrator Has Access To This Page')
        return redirect(url_for("account", username=session['user']))

    if request.method == "POST":
        # This takes the admin input from the update diet form
        # and put it into a dictionary
        edit_diet = {
            "diet_name": request.form.get("new_diet_name")
        }
        # This then uses the above dictionary and updates
        # the diet type within the diets db,
        # and a message is displayed when the diet type is updated and
        # redirects admin to the manage page
        mongo.db.diets.update({"_id": ObjectId(diet_id)}, edit_diet)
        flash("Diet Has Been Updated")
        return redirect(url_for("get_diets"))

    diets = mongo.db.diets.find_one({"_id": ObjectId(diet_id)})
    return render_template("admin/edit_diets.html", diets=diets)


@app.route("/delete_diet/<diet_id>")
def delete_diets(diet_id):
    # This allows the admin to delete a diet type using
    # that diets type unique id, once done a message
    # will display and redirect admin to the manage page
    mongo.db.diets.remove({"_id": ObjectId(diet_id)})
    flash("Diet Has Been Deleted")
    return redirect(url_for("get_diets"))


@app.errorhandler(404)
def page_not_found_error(error):
    '''
    This handles page not found 404 error
    '''
    return render_template('error_pages/404.html', error=True), 404


@app.errorhandler(500)
def internal_server_error(error):
    '''
    This handles internal server 500 error
    '''
    return render_template('error_pages/500.html', error=True), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
