# Full Stack Frameworks with Django MileStone(Project4) : 8Bear

8Bear is a website for the food industry and consumers in Singapore. The current food delivery systems and companies draw up to 30% commission or more from vendors who user their services to connect to customers.
8Bear offers a platform for food vendors to take charge of the delivery themselves and cater their foods for certain towns or postal codes. Their customers can order their food from home through this website and
vendors can read the orders from their order view page.  

My deployed website is [here](https://nks-8bear.herokuapp.com/).

## UX
 

User Stories

1. As a vendor, I want to create/view/update/delete profile.
2. As a vendor, I want to create/view/update/delete food.
3. As a vendor, I want to create/view/update/delete delivery areas.
4. As a vendor, I want to view/update orders.
5. As buyer, I want to create/view/update/delete profile.
6. As buyer, I want to view orders history.
7. As buyer, I want to create/view/update/delete orders in shopping cart
8. As buyer, I want to view foods info and vendors info by filtering by categories and search box.
9. As user, I want to create/view/update/delete user account. (Delete user is not created in this project.)

##Wireframes

##ERD

## Features
### Existing Features

- General (feature navigation bar) - allows user always use similar navigation bar whichever views he is in.
- General (feature User display) - allows user to see his username on top right when he is login.
- Landing Page (feature information on vendors) - allows user to know how many vendors existing in this system.
- Landing Page (feature information on towns) - allows user to scroll through the towns to understand his town have how many possible vendors serving.
- Landing Page (feature get started flowchart) - allow users to understand the site better.
- My Home (feature secondary navigation bar) - allows user with consistant navigation experience in buyer page.
- My Home (feature profile display) - allows user to see the current profile he is in for viewing the offered vendors and foods.
- My Home (feature switch profile) - allows user to switch between profiles. Only Foods and Vendors that match user selected profiles' town and postal code will then appear in the vendor section and food section.
- My Home (feature category dropdowns and search box) - allows user to have better experience filtering and searching more quickly. This is for **user story 8**.
- My Home (feature add to cart button) - allows user to add food to cart.
- My Profile (feature CRUD for profile) - allows user to CRUD on his profiles. This is for **user story 5**.
- My Orders - This is for **user story 6**.
- My Shopping Cart (feature Checkout button) - allows user to checkout to stripe payment page.
- My Shopping Cart (feature CRUD) - This is for **user story 7**.
- Vendor Profiles (feature CRUD) - This is for **user story 1**.
- Vendor Food Gallery (feature CRUD) - This is for **user story 2**.
- Vendor delivery area (feature CRUD) - This is for **user story 3**. Vendors will only add in towns and postal codes that they want to deliver to.
- Vendor Orders (feature Read/Update) - This is for **user story 4**. Vendor can checked on outstanding orders as completion status and will see the order moved down to completed orders table.
- Vendor Orders (feature search box) - allows vendor to search past history by food name, buyer name and date.
- My Account (feature AllAuth functionalities) - This is for update/view for **user story 9**. AllAuth offers functionality to change password and update email.
- Create Account (feature signup ) - This is create for **user story 9**.


### Features Left to Implement

- Adding reviews and comments functionality in buyer's order history page.
- Adding non-delivery report functionality in buyer's order history page.
- Refreshing vendor order page every minute.
- Add vendor photo in add vendor profile page.
- The commercial part between vendor and web abministrator are not resolved. Currently, payment by stripe are credited to my account. One possibility is payment to vendor directly and maybe certain commission I may receive monthly.
Another possibility is a system to credit payment to vendor according to their sales. Hence, commercial aspect is brief at this moment.
- email API to send to login users.

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [BootStrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    - The project uses **BootStrap 4.5** for its framework of HTML,CSS styling & mobile responsiveness.
- [FontAwesome 4.7](https://fontawesome.com/v4.7.0/)
    - The project uses **FontAwesome 4.7** for various fonts icons.
- [UploadCare](https://uploadcare.com/docs/quick_start/)
    - The project uses **Uploadcare** for uploading images management.
- [Django 2.2.6](https://www.djangoproject.com/start/overview/)
    - The project uses **Django 2.2.6** for its application frameworks.
- [Python 3.8.2](https://www.python.org/downloads/release/python-382/)
    - The project uses **python 3.8.2** for its python languages.
- [Heroku](https://www.heroku.com/home)
    - The project uses **Heroku PostgreSQL** for its deploymetn and database.


## Testing

1. Home page:
    - [x] Click sample recipe will show a sample recipe pop out.
    - [x] Click "Uncover Treasures", "Login to My Account", "New Account" brings me to the desired pages.

2. Recipes (table) page:
    - [x] Navigiation bar links bring to desired pages.
    - [x] Picture font link brings to desired page.
    - [x] Search box by "Char" shows results of recipe "Char Kway Teow" and flash message "Search results for 'Char' ".
    - [x] Search box by "a" shows flash message "No results for 'a' " .
    - [x] Table sort buttons for Recipe Name able to arrange recipe name in ascending/descending order.
    - [x] Table sort buttons for Cuisine Name able to arrange cuisine in ascending/descending order.
    - [x] Table sort buttons for Self-rating able to arrange self-rating in ascending/descending order.
    - [x] Table sort buttons for date Posted able to arrange dates in ascending/descending order.
    - [x] Table sort buttons for Self-rating able to arrange self-rating in ascending/descending order.
    - [x] Table sort buttons for Ratings able to arrange ratings in ascending/descending order.
    - [x] Table sort buttons for Reviews able to arrange reviews in ascending/descending order.
    - [x] Recipe Name blue link brings me to the recipe page.
    - [x] Review number blue link brings me to the the recipe's reviews page.

3. Recipes (pictures frames) page:
    - [x] Photos displaying for individual recipes fine.
    - [x] With visiting the page, Photo for each recipe will refresh randomly if the recipe have more than one photo submission.
    - [x] No photo text will display in the recipe which does not have photo submission.
    - [x] Recipe name links in red button brings me to its recipe page. 
    - [x] Search box and navigation bar working similarly to the recipes table page mentioned above.

4. Individual Recipe page:
    - [x] The ratings/reviews button brings me to the recipe's reviews/ratings page.
    - [x] The ratings/reviews count tallies with the number of average ratings and the number of reviews made.
    - [x] The bookmark button pops out a fill in form.
    - [x] If the add bookmark without entering registered email & password, flash message shows "No matching email and password record."
    - [x] If the user has already bookmarked, flash message shows "already bookmarked."
    - [x] For success in adding bookmark, flash message shows "Added to your bookmark."
    - [x] Other recipes names blue links brings me to their respective recipe page by same contributor.

5. Login page:
    - [x] If login without entry of email address and password, the flash message shows "No matching email and password for account. Please try again."
    - [x] If login with entry of email address only and without password, the flash message shows "No matching email and password for account. Please try again."
    - [x] If login with registered email address and password, page brings me to my recipes page.

6. My Recipes page:
    - [x] Navigiation bar links checked.
    - [x] The recipe name blue link opens in a new tab for the recipe page.
    - [x] The edit blue link brings me to edit the recipe page.
    - [x] The delete blue link brings me to a Modal box to verify again if ok to delete or cancel.
    - [x] Clicking cancel in the Modal box, brings me back to my recipes page.
    - [x] Clicking ok in the Modeal box, brings me back to my recipes page and the recipe to be deleted is no longer appearing.
    - [x] The add recipe blue linke brings me to the add recipe page.
    - [x] My favourites dropdown buttons shows recipes I have bookmarked.
    - [x] Clicking remove in the favourites dropdown, will refresh My Recipes page and the recipe will no longer appear in the favourites dropdown.

7. Edit page:
    - [x] Navigiation bar links checked.
    - [x] The add/remove buttons can add new step rows or delete last step rows accordingly. Clicking on remove button will shows a popout box to verify with user ok/cancel. Ok will remove the last step. Cancel the last step will be intact.
    - [x] The edit photos bring me to edit photos page.
    - [x] In edit photos page, able to remove photo by checking, submitting and the page will refresh and the photo will no longer appears.
    - [x] In edit photos page, able to add/remove more Upload image buttons by clicking on the add/remove buttons.
    - [x] In edit photos page, able to upload image and the page will refresh with the new image appearing.
    - [x] In edit photos page, able to return to edit page with back button.
    - [x] Editing the every form textboxes and clicking submit return me to My Recipes page. Changes can be seen from the table. Date last edited will also be update. Re-entering the edit recipe page will still show that the changes have been stored.
    - [x] Back button returns me to My Recipes page.

8. Add Recipe page:
    - [x] Navigiation bar links checked.
    - [x] Populate the form and submit. Steps can be added via the add/remove buttons. Photos can be added via Upload Image button. More images can be uploaded with red add/remove buttons. After submitting, page will redirect to My Recipes page and new recipe is shown in table.
    - [x] Back button brings me back to My Recipes page.
    - [x] Not populating recipe name/cuisine/my rating and proceed to submit will result in fail flash message.

9. My Account page:
    - [x] Not filling UserName , password which doesn't matches, not fill email & country. Any of the above will result in submit button to turn semi-opaque or unclickable.
    - [x] Switching email that coincides with another existing user account will prompts error message "Failed to update account because email already registered by an existing user."
    - [x] Changing email with upperlettercase characters will always saved in system in lowercases.
    - [x] If password does not match, a red prompt will show "Passoword does not match".
    - [x] If password matches, a green prompt will show "Password matches".
    - [x] Upon success submission by clicking submit button, will return to My account page with flash message "Your Account has been updated" and all changes updated too.
    - [x] Exit button brings me back to My Recipes page.

10. New Account page:
    - [x] The required placeholder fields need to be filled in and passwords need to match for the submit button to be activiated or clickable.
    - [x] If password does not match, a red prompt will show "Passoword does not match".
    - [x] If password matches in both textboxes, a green prompt will show "Password matches".
    - [x] If Password textbox is empty, a red prompt will show "Password missing".
    - [x] Upon clicking submit button and if email already been used before in database, a flash message will show " Existing account with this email already in use".
    - [x] Upon successful submission on clicking submit button, user will be redirected to "My recipes page". Going to My Account page, I can see that the create to database and read from database is successful.
    - [x] Exit button brings me back to My recipes page.

The project looks fine across different browsers like edge, chrome or firefox. I am using chrome primarily most of the time when debugging.
In smaller devices, I have reduce the columns in the tables in "My recipes page" & "Recipes page" so that the table of content will generally be confined in the constraint of the device width.
Due to associating most of the primary tags with bootstrap CSS, hence the contents mobile responsives are pretty much organised and set by bootstrap already.
    
## Deployment

This website is deployed to hosting platform Heroku from this git origin master branch.
For running the codes locally, advise to run "pip3 install -r requirements.txt" in your IDE first to install the necessary libraries.

### Testers account

user: Customer
email : Customer@email.com 
password: tomjerry123

user: vendor
email: vendor@email.com
password: spidervenom123

Superuser for allowing vendor validation??

## Credits

### Content
- The recipes are copied from a book "Patchwork of Flavours, A collection of recipes from the generation before" by NTU Welfare Services Club published in 2007.

### Media
- The photos used in this site were obtained from [PixaBay](https://pixabay.com/).

### Acknowledgements

- I received inspiration for this project from project example idea for Data Centric Development Milestone Project by [Code Institute](https://codeinstitute.net/).