import os
from flask import Flask, render_template, redirect, request, url_for ,request, redirect, session, g, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask import request
from flask_bcrypt import bcrypt
import math
 
app = Flask(__name__)
app.secret_key=os.urandom(24)


app.config["MONGO_DBNAME"] = 'online_cookbookt'
app.config["MONGO_URI"] = "mongodb+srv://root:root123456@myfirstcluster-jkztf.mongodb.net/online_cookbookt?retryWrites=true&w=majority"


mongo = PyMongo(app)

# MongoDB collections

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes
categories_collection = mongo.db.categories

@app.route('/')
def index():
    """
    Route allows users to view all the recipes within the database
    collection with pagination, logged in users can view profile and create
    recipes.
    """
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipe.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)

    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('index.html', recipe=recipes,
                               title='Home', current_page=current_page,
                               pages=pages, current_user=current_user)
    else:
        return render_template('index.html', recipe=recipes,
                               title='Home', current_page=current_page,
                               pages=pages)



@app.route('/search')
def search():
    """Route for full text search bar"""
    
    
    db_query = request.form.get('db_query')
    results = mongo.db.recipes.find({'$text': {'$search': db_query}})
    categories = list(categories_collection.find())
    return render_template('recipe.html',  recipes=results, categories=categories)
    
@app.route('/<category_name>', methods=['GET'])
def filter_list (category_name):
    categories = list(categories_collection.find())
    category_name = categories_collection.find_one(
        {'category_name': category_name})
    recipes = recipes_collection.find()
    return render_template(
        'filter.html',
        categories=categories,
        category_name=category_name,
        recipes=recipes)
        
        

"""
Login/User sessions
"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        existing_user = users_collection.find_one(
            {'name': request.form.get('username')})
        if existing_user:
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
        return redirect(url_for('signup'))
    return render_template('login.html')
    
    
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = \
            users_collection.find_one(
                {'name': request.form.get('username')})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form.get('password')
                                     .encode('utf-8'), bcrypt.gensalt())
            users_collection.insert(
                {'name': request.form.get('username'), 'password': hashpass})
            session['username'] = request.form.get('username')
            return redirect('/loggedin/' + session['username'])
    return render_template('signup.html')
    
@app.route('/loggedin/<username>', methods=['GET', 'POST'])
def loggedin(username):
    recipes = \
        recipes_collection.find({'added_by': session['username']})\
        .sort('name', pymongo.ASCENDING)
    return render_template(
        'result.html',
        username=session['username'],
        recipes=recipes
        )
        
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

"""
Recipe Create/Update/Delete Methods
"""    
@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe_page(recipe_id):
    """Route to show single recipe view page"""
    recipe = recipes_collection.find_one({"_id": ObjectId(recipe_id).limit(6)})
    return render_template('recipe.html', recipe=recipe)
    

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", 
    categories= mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = recipes_collection
    recipes.insert_one({
        'category': request.form.get('category_name'),
        'name': request.form.get('name'),
        'cooking_time': request.form.get('cooking'),
        'prep_time': request.form.get('prep'),
        'serves': request.form.get('serves'),
        'image': request.form.get('image'),
        'added_by': session['username'],
        'ingredients': request.form.getlist('ingredient'),
        'method': request.form.get('method'),
        'cuisine': request.form.get('cuisine'),
        })
    return redirect(url_for('loggedin', username=session['username']))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = recipes_collection.find_one({'_id': ObjectId(recipe_id)})
    _categories = categories_collection.find()
    category_list = [category for category in _categories]
    return render_template('editrecipe.html', recipe=recipe,
                           categories=category_list)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes_collection.update({'_id': ObjectId(recipe_id)}, {
        'category': request.form.get('category_name'),
        'name': request.form.get('name'),
        'cooking_time': request.form.get('cooking'),
        'prep_time': request.form.get('prep'),
        'image': request.form.get('image'),
        'serves': request.form.get('serves'),
        'ingredients': request.form.getlist('ingredient'),
        'method': request.form.get('method'),
        'cuisine': request.form.get('cuisine'),
        'added_by': session['username'],
        })
    return redirect(url_for('loggedin', username=session['username']))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes_collection.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('loggedin', username=session['username']))

"""
Category adding
"""

@app.route('/categories')
def categories():
    categories = \
        categories_collection.find().sort('category_name', pymongo.ASCENDING)
    return render_template('categories.html', categories=categories)

@app.route('/add_category ')
def add_category():
    return render_template("add_category.html")

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form['category_name']}
    categories_collection.insert_one(category_doc)
    return redirect(url_for('categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    categories_collection.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=categories_collection.find_one(
                               {'_id': ObjectId(category_id)}
                               ))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories_collection.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('categories'))
    

@app.route('/store')
def store():
    return render_template('store.html')




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)