# Further Testing
Since majority of the feautres throughout the website were covered in the User Story Testing section of the readme file, here I will go thorugh each page in general and manually test to see if everything is working correctly. If any issues or bugs are found they will be recorded and fixed. 

## Navigation Bar
All features of the navigation bar work perfectly, they display on all pages across the website. All of the page links work correctly for logged in and non-logged in users. The active page class also works when a user is on a specific page of the website and the logo home link if clicked works on every page. The side navigation bar also works when the website is being viewed by smaller devices and slides in from the right as expected.

## Footer
The footer clearly displays at the bottom of every page of the website and from here the users can click on the social media icons. When they click an icon, a new tab open and takes them to that website of the social icon. Another feature in the footer is when a user clicks on the copyright it opens a new tab and takes them to the personal portfolio of the developer. 

## Contact Modal
The contact modal can be accessed from any page within the website and has a cool feature, so if the user is logged in their information is automatically shown in the input field of the contact modal. This happens for the fullname, username, and email fields within the contact modal but only for logged in users, non-logged in users have to type everything in manually. 

All buttons works fine and have the materialize wave effect on them and if the user clicks anywhere outside the modal it will close. All form validation works and no fields can be left empty and also the text helpers display if there is an input issue. A successful send confirmation box does appear once a message is sent and the admin who is I, does receive the email. 

## Homepage
The homepage clearly loads up across all device when the website is first visited and displays to the user three option buttons. The first option is for registered users to login, the second is for non-registered users to register. The third and final option is browse as a guest which will take users to the all recipes page where they can see all recipe cards. All button effects work when clicked by a user. Another option below the button is a help link which opens the contact modal for users to get in contact with the website administrator.

## Login Page
When the login button is either clicked from the homepage or in the navigation bar, the login page loads fine and shows the full login form with icons and button at the bottom of the form. All form validation works meaning no fields can be left empty and is the user makes a mistake the text helpers will display to the users. 

From here a user must enter a valid username and password to be successfully logged into the website. If a wrong username or password is entered the user will be redirected back to the login page and a message will display to them say username or password is incorrect. Also a quick link to the registration page is shown underneath the login in form just in case a user clicks the wrong button. 


## Register Page
When the register button is either clicked from the homepage or the navigation bar, the register page loads fine and shows the full register form with icons and buttons at the bottom of the form. All form validation works meaning no fields can be left empty and is the user makes a mistake the text helpers will display to the users, along with the character counters was well. All buttons works accordingly and when clicked the waves effect takes place. 

When a user registers and comes to the username input field, the user has to type a unique username which is not already taken, this check is preformed when the user submits the form and if the username matches a username with the users collection. The user will be redirected back to the register form and message will display saying the username is already taken by another user. 

Another validation check happens when a user registers and that is to make sure that the user enters an email address in the correct format. Once a user has successfully registered they will be taken to their account page.
  

## Account Page
Once a user has registered or has logged in the first page they visit is the account page which load as it’s supposed to and display a number of buttons and information. From here a user can access a variety of different features within the website. From here the user can change their username and password, they can also delete their account if they choose too. 

Also on this page they can add their first recipe and after multiple recipes. Once they have added recipes to the recipe collection, they can visit the account page and from there they can view and edit all of their created recipes. 

## All Recipe Page
A logged in and a non-logged in user can visit this page by clicking on the recipes navigation link located within the navigation bar. Once the page fully loads the users will be able to see a recipe search bars with buttons, recipe cards with images and basic recipe information. At the bottom of the page the user will be able to see the page pagination which will show which page they are on and how many recipe pages have been created. 

For a non-logged in user they cannot go any further, a message will display at the top of the page informing them to either login or register to get full access. So if a user tries to view a recipe full details by either clicking the card body or the view button, they will be redirected to the homepage and a message will appear saying to them to they need to register or login to view a recipe in detail. 

For logged in users when they visit the recipe page they will be able to see all recipe card but their recipe cards will have a different background colour from the rest. They will also be able to see the edit button within their recipe cards and this will help users find their created recipes as well. If a logged in users clicks on a recipe card body or the view button they will be taken to the view page for that specific recipe. 

All users can use the search feature within the recipe page and for them to search for a recipe they can type in any query they like for example a recipe name, ingredient, meal type, cuisine type or even a diet type. Once they have entered their search query the results will display below the search bar and they will be shown a search result title with a search result number and the recipe cards below. 

If no results can be found a message will display to the user saying no results found, to then try another search query and also with a clear search button. Validation also is applied to the search bar, for a user to search it cannot be empty and if a user wants to clear a search all they have to do is press the reset button under the search bar. 

## View Recipe Page
Only a registered and logged in user can view the view recipe page of a specific recipe, once the page is fully loaded they will be able to view all of the recipes details. The image if provided by the creator of the recipe will be located on the left and if no image is provided a default image will be displayed. On the right they will be able to see all of the recipe attributes and below that they will be able to see the collapsible ingredient list and cooking instruction list. 

To view the ingredient list all the user has to do is click on it and it will collapse down show the information inside and the same goes for the cooking instructions. Once they are done they can simply click the collapsible element again and it collapse up hiding the information inside. 

Underneath all of that at the bottom of the page, the user will see two buttons, one is to edit that recipe and the other button is to delete that recipe they are view. These buttons can only be seen on recipes that the logged in user has created, which will stop them editing and deleting other peoples recipes.

## Add Recipe Page

## Edit Recipe Page

## Delete Recipe

## Change Username

## Change Password

## Delete Account

## Error Pages

# Admin Pages

## Manage Meals, Cuisines, Diets

## Add Meals, Cuisines, Diets

## Edit Meals, Cuisines, Diets
