# Further Testing
Since majority of the feautres throughout the website were covered in the User Story Testing section of the readme file, here I will go thorugh each page in general and manually test to see if everything is working correctly. If any issues or bugs are found they will be recorded and fixed. 

## Navigation Bar
All features of the navigation bar work perfectly, they display on all pages across the website. All of the page links work correctly for logged in and non-logged in users. The active page class also works when a user is on a specific page of the website and the logo home link if clicked works on every page. The side navigation bar also works when the website is being viewed by smaller devices and slides in from the right as expected.

## Footer
The footer clearly displays at the bottom of every page of the website and from here the users can click on the social media icons. When they click an icon, a new tab open and takes them to that website of the social icon. Another feature in the footer is when a user clicks on the copyright it opens a new tab and takes them to the personal portfolio of the developer. 

## Contact Modal
The contact modal can be accessed from any page within the website and has a cool feature, so if the user is logged in their information is automatically shown in the input field of the contact modal using the user cookie session. This happens for the fullname, username, and email fields within the contact modal but only for logged in users, non-logged in users have to type everything in manually. 

All buttons works fine and have the materialize wave effect on them and if the user clicks anywhere outside the modal it will close. All form validation works and no fields can be left empty and also the text helpers display if there is an input issue. A successful send confirmation box does appear once a message is sent and the admin who is I, does receive the email. 

## Homepage
The homepage clearly loads up across all device when the website is first visited and displays to the user three option buttons. The first option is for registered users to login, the second is for non-registered users to register. The third and final option is browse as a guest which will take users to the all recipes page where they can see all recipe cards. All button effects work when clicked by a user. Another option below the button is a help link which opens the contact modal for users to get in contact with the website administrator.

## Login Page
When the login button is either clicked from the homepage or in the navigation bar, the login page loads fine and shows the full login form with icons and button at the bottom of the form. All form validation works meaning no fields can be left empty and if the user makes a mistake the text helpers will display to the users. 

From here a user must enter a valid username and password to be successfully logged into the website. If a wrong username or password is entered the user will be redirected back to the login page and a message will display to them say username or password is incorrect. Also a quick link to the registration page is shown underneath the login in form just in case a user clicks the wrong button. 

## Register Page
When the register button is either clicked from the homepage or the navigation bar, the register page loads fine and shows the full register form with icons and buttons at the bottom of the form. All form validation works meaning no fields can be left empty and if the user makes a mistake the text helpers will display to the users, along with the character counters was well. All buttons works accordingly and when clicked the waves effect takes place. 

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
Only a logged in user can access the add recipe page and for a user to add a recipe they have to visit their account page and click on the add recipe button. Once the button is clicked the user will be taken to the add recipe page which loads up a add recipe form, with icons and buttons at the bottom of the form. All form validation works meaning no fields can be left empty and if the user makes a mistake the text helpers will display to the users, along with the character counters as well.

For a user to add a recipe they must fill the key fields within the form, the key fields are the recipe name, description, meal type, cooking time, number of servings, ingredient list and cooking instruction. Once these fields have been filled in all the user has to do click the create button which will add the recipe to the recipe collection and then the user will be taken to their account and a message will display to the user saying recipe successfully added. From the account page, the user will be able see their newly created recipe below. 

## Edit Recipe Page
Only a user who is logged in and has created a recipe can edit a recipe. This can be done in a number of way. The first way to edit a recipe can be done from the account page, all the user has to do is scroll down to their created recipe section and click on the edit button which will take the user to the edit recipe page. The second way to edit a recipe is from the all recipes page, all the user has to do is click the edit button within one of their created recipe cards. The last way a user can edit a recipe is by viewing one their own created recipes in the view page and then scrolling down and click on the edit button.

Once the user is on the edit recipe page, all of the recipe info will auto populate the fields and from there the user can make their changes to the recipe. The form validation still applies within the edit form and the key fields cannot be empty. Once a user has made the changes to the recipe, to finish it off all they need to do now is click the update button. Then they will be taken back to their account page and a message will display informing the user that the recipe has been updated.     

## Delete Recipe
If a user want to delete a recipe, the user has to be logged and be viewing one of their own created recipes. The delete button is located at the bottom next to the edit button of the view recipe page. Once the delete button is clicked a delete confirmation modal will open containing the important info for the user to read before they take action. To delete the recipe once the delete modal is open all the user has to do is click the delete button and the user will be taken to their account page and a message will display to the user saying the recipe has been deleted.

## Change Username
If a user wants to change their username, they need to be logged in to the website and then they need to click on the change username button. Once clicked the user will be taken to the change username page and the change username form, icons and buttons will show. Once on the page they will see the change username form, the first input field is the current username field which will auto fill and will be disabled and it’s only there to display to the user their current username.

Now all the user has to do is type in a unique username and click the change button, once clicked a username check will be done to make sure that the username is not already taken by another user. If the username is already taken they will be redirected back to the change username for and a message will display to them saying username already taken. If the username is not taken then the user will be logged out and redirected to the homepage where a message will display to the user informing them that the username has changed and for them to log in using the new username.

## Change Password
If a user wants to change their password, they need to be logged and visit the account page and click on the change password button. Once the button is clicked it will take the user to the change password page where they will see the change password form, icons and buttons. For a user to change their password they first need to enter their current password. 

Then they need to type in a new password and then after that they need confirm the new password. Once done they need to click on the change button and the user will be taken to their account page and a message will inform the user that their password has been changed. 

## Delete Account
If a user wants to delete their user account, they need to log into the website which will take them to the account page and from there they need to click on the delete account button. Once clicked a modal will open containing key info about the action the user is about to take. For the user to proceed ahead with deleting their account all they need to do is click on the delete button. Once clicked the user will be logged out of the account and taken to the homepage of the website where they will see a message informing them that their account has been deleted and all created recipes.  

## Error Pages
To trigger a 404 error all that needs to be done is manually mistype in a URL and the custom 404 page will load informing the user that the file is not found with two buttons. One button will link to the homepage and the other is a button connected to the contact modal. During development I could not simulate a 500 internal server error. 

## Unwanted Page Access  
In the app.py file I made sure that I added a script to prevent non-logged in users gaining access to the website without registering or logging in. There is also a script for logged and non-logged in users not being able to gain access to the admin pages.

# Admin Pages
Only the website administrator can access these pages and for the admin to access these pages, they need to login into their account and once logged in they will be able a manage recipe attributes section on their account page. Within the manage attributes section there are three button that are linked to three different but similar pages. 

The three buttons are manage meal types, mange cuisine types and manage diet types. When one of the buttons are clicked they will be taken to the manage page for the recipe attribute. Once on the page the admin can add more recipe attributes or they can edit or delete a specific attribute. 

These three recipe attributes pages are linked to three different collection within my MongoDB which are meals, cuisines and diets and these are linked to the add and edit recipe forms dropdown lists. So if new attribute is added, edited or deleted, they will automatically update within those dropdown lists.

## Manage Meals, Cuisines, Diets Types
Only the website administrator can access these pages and for the admin to access these pages, they need to login into their account and once logged in they will be able a manage recipe attributes section on their account page. Within the manage attributes section there are three button that are linked to three different but similar pages. 

The three buttons are manage meal types, mange cuisine types and manage diet types. When one of the buttons are clicked they will be taken to the manage page for the recipe attribute. Once on the page the admin can edit or delete a specific attribute and they can add more. 

## Add Meals, Cuisines, Diets Types
For the admin to add recipe attributes for meals, cuisines and diets, they simply need to click on one of the manage recipe types button, once clicked they will be on the manage page for one of those recipe attribute types. Then from there they need to click on the add button located at the top of the page. Once clicked they will be taken to the add attribute form. 

The form has validation and cannot be submitted empty, once on this page the admin can then add a new recipe attribute and then press add. Then they will be taken back to the manage page of the recipe attribute and message will appear informing them that the recipe attribute has been added.  

## Edit Meals, Cuisines, Diets Types
For the admin to edit recipe attributes for meal, cuisine and diet types, they simply need to click on one of the manage recipe types button, once clicked they will be on the manage page for one of those recipe attribute type. From there they need to choose a recipe type they want to edit and then click on the edit button.

Once clicked they will be taken to the edit recipe attribute form which will auto fill with the recipe attribute name they want to edit. Once the edit has been made they then have to click the edit button and once clicked they will be take back to the manage recipe attribute page and a message will display to them informing them of the update. 

## Delete Meals, Cuisines, Diets Types
For the admin to delete recipe attributes for meal, cuisine and diet types, they simply need to click on one of the manage recipe types button, once clicked they will be on the manage page for one of those recipe attribute type. From there they need to choose a recipe type they want to delete and then click on the delete button. Once clicked the recipe attribute will delete and the mange page will update and a message will appear informing the admin that the recipe attribute has been deleted.