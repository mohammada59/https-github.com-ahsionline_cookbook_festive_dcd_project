# online_cookbook_festive_dcd_project 
*https://online-festive-recipe-cookbook.herokuapp.com/
## UX

I created an application called ONLINE COOKBOOK that allows user to store and easily access recipes.
The app is a recipe Festival that will store all your Festive and occasional recipes in one place! It allow the user
to read recipe, create new recipe, edit and delete them (CRUD).
As a user you can:

## User story
* view the app on your preferred device (mobile, tablet, desktop)
* create your own recipe and add to the website
* edit the recipes
* delete the recipes
* see card of all recipes
* see a list of all recipes
* search for recipes by choosen recipe name
* register to the application with username and password
* login to the application with username and password
* Manage cstegoris by
* create new categories
* edit categories
* delete categories
* update categories

### Design

I created this website using  Materialize CSS. This app contain register page where new user is able to register, login page where user is able to login, home page
with navbar, buttons, and lists of recipes when clicked it will lead to individual recipe page.
when you want to add new recipes and also new categories you need to Register first when you register then you will have to Login in app
your username your email and password then you will enter the Result of data page in this page you can edit or delete the recipes 
also add recipes and manage, add , update and delete categories

## WIREFRAMES
User story of online festive cookbook step by step explain with Demo
The Readme file will see the wireframe is different in wallpaper The app was body style of backgound
was looking  squeshy you can see in wireframe mobile demo thats why i remove wallpaper and style.css file
to change the color of body thats why you will see the some of wireframe is difference. 
### wireframes for mobile
user freidly Responsive Application Desktop and Mobile user can see the Mobile version (Responsive)
![Home-Mobile](https://user-images.githubusercontent.com/38302279/65285854-98834480-db35-11e9-9354-ede11e979123.png)
user can use the app in Desktop show the view of Desktop
### wireframes for desktop
![Home-Desktop](https://user-images.githubusercontent.com/38302279/65380517-bdfa8480-dcd4-11e9-8a13-899aab5d7d09.png)
### wireframes for Search
if user want to serach recipes in database just search recipe for example if user want to search christmas recipes just 
click christmas and then Go user will find all christmas recipe show on the Result page in the result page 
user got theree options only if user search recipe edit delete and view the recipe if user click view recipe
redirect to full recipe page but if user want to edit or delete recipe user needs to be Login the app 
![Search](https://user-images.githubusercontent.com/38302279/65547917-4fa30580-df12-11e9-93a7-111d75416c9b.png)
the search of result is show like that 
![search_result](https://user-images.githubusercontent.com/38302279/65548777-0f448700-df14-11e9-9e62-1273e00c4df9.png)
when user want to see full recipe click view recipe you can get full recipe 
![search_result1](https://user-images.githubusercontent.com/38302279/65548927-5af73080-df14-11e9-8ae7-fff4c62b4e0c.png)

### wireframes for Recipes
user open the app and user can see all Recipes when user click the Recipes page it will be redirect to Recipe card 
where user can see the Name and image of Recipe and view button when user click view button to show the full
recipe page recipe name,image,category,cooking_time,prep_time also Recipe ingredients and Method and last cusines
and name of the Author mean user of Recipe who add the Recipe
![Recipe](https://user-images.githubusercontent.com/38302279/65380519-c357cf00-dcd4-11e9-9867-626774551bf8.png)
![Recipe_id](https://user-images.githubusercontent.com/38302279/65380828-f05bb000-dcdb-11e9-9bd4-dd003f6330a5.png)
### wireframes for signup/signin
user create signup add user name and password when user signin fill the username and password to Login the page 
![Singnup](https://user-images.githubusercontent.com/38302279/65380419-2c3e4780-dcd3-11e9-9926-f464aab972e1.png)
![SignIn](https://user-images.githubusercontent.com/38302279/65380447-dae28800-dcd3-11e9-82d8-453b7f24935e.png)
### wireframes Add Recipe and after redirect the add recipe page in Result Data
when user Login the page user can see the Result page where he can see the latest recipe and also user can add the Recipe 
user fill the Recipe and page Redirect to Result where user can see the recipe he Add it
![Add-Recipe](https://user-images.githubusercontent.com/38302279/65380548-6dcff200-dcd5-11e9-8ec9-d467cf6ffad5.png)
![Result-of-Data](https://user-images.githubusercontent.com/38302279/65380610-dc617f80-dcd6-11e9-8358-10118d158755.png)
### wireframes Edit Recipe and Delete Recipe
when user in Result page user can edit or delete Recipe 
![Edit_Recipe](https://user-images.githubusercontent.com/38302279/65380552-7aece100-dcd5-11e9-90b9-1166c78877cf.png)
if user want to edit recipe click edit button and changes made and click button save chages and page Redirect to the
Result page where changes made.
![Delete recipe](https://user-images.githubusercontent.com/38302279/65380598-65c48200-dcd6-11e9-954d-940ef9a8ae07.png)
if user want to delete recipe simple click delete the button and Recipe will delete on the Result and Recipe page
### wireframes Manage Add edit and delete category
when user click manage categories user can see the all Festive category and every category is edit and delete button
where user can choose add,edit and delete category
![Manage-Categories](https://user-images.githubusercontent.com/38302279/65380634-4843e800-dcd7-11e9-8b9e-328124383f24.png)
if user want to add category click add category button add the name of category example:Freindship Day then click add
category button to add category page will redirect to the Manage Categories
![Add-Category](https://user-images.githubusercontent.com/38302279/65380650-98bb4580-dcd7-11e9-92e0-25ca9e5bfa73.png)
if user want edit category in Manage Category click edit button and change example:Freindship to Freindship Day and
save change and click page Redirect to Manage category 
![Edit-Categoery](https://user-images.githubusercontent.com/38302279/65380725-264b6500-dcd9-11e9-8e79-8e99679d3890.png)
if user want to the delete category simple user need to click the delete category and category will delete in
Manage Category page
![Category-Delete1](https://user-images.githubusercontent.com/38302279/65380707-a4f3d280-dcd8-11e9-95a2-b51c93622617.png)
![Category-Delete2](https://user-images.githubusercontent.com/38302279/65380708-a9b88680-dcd8-11e9-94b7-5032d8ffb15b.png)
### store
if user want to shopping he can choose and select the item and add to the cart and when user want to purchase
click the purchase button and user received the message Thank you for purchase 
i explain you example 
user click the store choose pots and pans and add to cart and add remove purchase pots and pans and user received the 
Thank you for purchase message
![store](https://user-images.githubusercontent.com/38302279/65554817-88e37180-df22-11e9-8a3d-75ed56a91c6b.png)
![store_cart](https://user-images.githubusercontent.com/38302279/65554822-8bde6200-df22-11e9-8e38-1ceddf691ba6.png)
![store_purchase](https://user-images.githubusercontent.com/38302279/65554965-05765000-df23-11e9-897c-4b609fb18e02.png)

### Database schema
![Database_Schema_mongo](https://user-images.githubusercontent.com/38302279/65286748-98d10f00-db38-11e9-91ff-42fdacdea7cf.png)
### Example schema from the 'recipes' collection:
```
{
    "_id": {
        "$oid": "5cbdf6f4e7179a264cf45ea0"
    },
    "cooking_time": "15 mins",
    "cuisine": "British",
    "method": "Bring a deep saucepan of water to the boil (at least 2 litres) and add the vinegar. Break the eggs into 4 separate coffee cups or ramekins. Split the muffins, toast them and warm some plates. Swirl the vinegared water briskly to form a vortex and slide in an egg. It will curl round and set to a neat round shape. Cook for 2-3 mins, then remove with a slotted spoon. Repeat with the other eggs, one at a time, re-swirling the water as you slide in the eggs. Spread some sauce on each muffin, scrunch a slice of ham on top, then top with an egg. Spoon over the remaining hollandaise and serve at once.",
    "ingredients": [
        "3 tbsp White Wine Vinegar",
        "2 Toasting Muffins",
        "4 Eggs",
        "4 slices Parma Ham",
        "1 batch Hollandaise sauce"
    ],
    "name": "Eggs Benedict",
    "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Eggs_Benedict-01-cropped.jpg",
    "added_by": "cskinner",
    "prep_time": "5 mins",
    "category": "Breakfast",
    "serves": "2"
}
```
## FEATURES

##### Existing features

* **Register page** - will allow new user to register to get access to the application

* **Login page** - will allow user to login before using the application


* **Navbar** - created to navigate particular list: (*recipes*, *categories* or *cusines*). Across the navbar the are links
with names of the lists. When hoover over the link color will change. For smaller devices the navbar collapse 
into *burger icon*.

* **'Add New Recipe' - button** - when clicked, it will allows the user to add new recipe

* **'Search By Reecipe name' - button** - when clicked, it will allows user to search recipes by particular Recipe name


* **'Edit Recipe' - button** - allows user to edit particular recipe and make changes

* **'Delete' - button** - allows user to Delete particualar recipe

##### Features left to implement

* Feature that will allow user remove or edit(make changes) only its own recipes - but not others users recipes.


## TECHNOLOGIES USED

* **Git** - used command line to for regular commits and to push my project to github
* **Github** - used to remotely store project code and allow public to see my website
* **JQuery 3.3.1** - to assist the form.js file
* **Materialize 1.0.0** - https://materializecss.com/text-inputs.html used for imput fields
* **Material Design Icons** - https://material.io/resources/icons/?style=baseline used to add icons to the input fields
* **Heroku** - this application is hosted via heroku


##### Front-End Technologies

* **HTML** - to create basic structure
* **CSS** - to add styles to the websites
* **Java Script** to add quary in form.js file

##### Back-End Technologies

* **Flask 1.0.2** - to construct and render templates
* ** Flask -Bcrypt==0.7.1** -  User model just stored the password for our users as text without any type of encryption.
* **Python 3.6.8** - used as the backend programming language
* **MongoDB Atlas** - database used to storewebsite backend data
* **PyMongo 3.8.0** - used for interacting with MongoDB database from Python
* **Jinja** - to display back-end data to the front-end
* **BSON ObjectId** - allows you to create and parse ObjectIDs without a reference to the MongoDB or bson modules

## TESTING

This website had been tested on different devices such as: Desktop, Tablet, Mobile. I used Chrome DevTools to make sure it works on: Samsung Galaxy S5, iPhone 5/6/7/8, iPad, PC Desktop;


## TROUBLESHOOTING

**Registration and Login system** - that was the biggest challenge but with lots of searching in google  websites I eventually  was able to create it

##### To be fixed

Add alert messages to registration and login system: 

* when user register to the app successfully - confirmation message should pop up
* when user login and try to use the same username which already exist - warning message should pop up

### Bugs
A number of bugs were caught during the testing process which were fixed. Some of
these were caused by the DOM manipulation on the add recipe and edit recipe pages.

There are a number of bugs that I am currently aware of that are yet to be fixed.
* One bug is in the filter options:
    * When changing between filter by main ingredient and cuisine all cuisines 
      are temporarly shown before an option in these categories is selected.
* Add Recipe/Edit Recipe
    * There is a bug caused by the validaion process of WTForms where if an invalid
      recipe submission is made, i.e. one field is not valid, on reload sometimes 
      the cuisine selector options do not reload.
* Favourite:
    * I've intermittently experienced an error where if clicked quickly in succession
      the favourite button might submit to the database twice. This seems to be due 
      to some asynchronous behaviour and should be resolved with an async/await 
      function or similar.

#MONGO_URI
Set the accompanying config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 90.193.93.24
MONGO_URI | `mongodb+srv://root:<password>@myfirstcluster-np4or.mongodb.net/test?retryWrites=true&w=majority`

PORT | 28017
SECRET_KEY | `<your_secret_key>`

- To retrieve your MONGO_URI please reference the official MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

## DEPLOYMENT

##### GITHUB

I deploy my project by going to GitHub, navigate to my github pages site's repository. Under my repository name I clicked Settings. Then I used the Select
drop-down menu to select master branch and then save it. Now my project is deployed to github pages and accessible to anyone via URL.

Link to my github repository: https://github.com/ahsin59/online_cookbook_festive_dcd_project.git

##### HEROKU

In the terminal, I created a requirements.txt file using this command: pip freeze > requirements.txt.
In the terminal, I created a Procfile by running: echo web: python app.py > Procfile command.
I push these files to my GitHub repository.
I created a new app on Heroku dashboard, I named it 'COOK-BOOK and then I set the region.
I linked Github repository to Heroku.
I set the config vars as follows: IP 0.0.0.0 and PORT 5000.

My app can be found at: *https://online-festive-recipe-cookbook.herokuapp.com/

To run this project you need to do the following:

* Go to Github repository and click on the 'clone or download' and copy the link.
* Create virtual environment that helps to keep dependencies required by this project separate from other projects by creating isolated python virtual environments.
* Install all required modules by creating requirements.txt file.
* Create a .env file with the connection to MongoDB database, and a secret key.
* You can run this application by following command: python3 app.py

## CREDIT

##### Content

The Recipes I added to this page are from this website: https://www.bbc.co.uk/food/occasions

##### Aknowlegment

my mentor:  Anthnoy Negne and Tutor support and slack Team - my help throughout the project

