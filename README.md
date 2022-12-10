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
9. As user, I want to create/view/update/delete user account. (Delete profile html or route to delete_profile/<buyer_id> [name='delete_buyer_profile_route'] has not been setup in this project.)

##ERD

<img src="/p4-erd.png">

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
- Vendor delivery area (feature CRUD) - This is for **user story 3**. Vendors will only add in towns and postal codes that they want to deliver to. Cannot add similar towns/postal code again if already in the added list.
- Vendor Orders (feature Read/Update) - This is for **user story 4**. Vendor can checked on outstanding orders as completion status and will see the order moved down to completed orders table.
- Vendor Orders (feature search box) - allows vendor to search past history by food name, buyer name and date.
- My Account (feature AllAuth functionalities) - This is for update/view for **user story 9**. AllAuth offers functionality to change password and update email.
- Create Account (feature signup ) - This is create for **user story 9**.
- General (feature flash messages) - allows user to view flash messages for many process in the site.


### Features Left to Implement

- Adding reviews and comments functionality in buyer's order history page is good to have so that buyer can add in reviews and comments for the food he has ordered.
- Adding non-delivery report functionality in buyer's order history page is good to have so that buyer can report to vendor he has not received the food over the system.
- Refreshing vendor order page every minute so that vendor does not require to refresh his page to see any new orders.
- Add vendor photo in add vendor profile page is good to have.
- The commercial part between vendor and web abministrator are not resolved. Currently, payment by stripe are credited to my account. One possibility is payment to vendor directly and maybe certain commission I may receive monthly.
Another possibility is a system to credit payment to vendor according to their sales. Hence, commercial aspect is brief at this moment.
- Need to change block entry to allow alphabets entry. Currently, it only allows numbers entry. This is because some blocks in Singapore have number follows by Alphabets.
- Search function for buyer order history is good to have.

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
- [Stripe](https://stripe.com/en-sg)
    - The project uses **Stripe** for its payment API.


## Testing

The below tests are recommended for full functional tests of the website.

I will test as vendor with following account.
- User: Vendor
- email: vendor@email.com
- password: spidervenom123

1. Vendor page:
    - [x] Login as Vendor.
    - [x] Created new profile. Reference as vendor_profile_one. No entry for photo_url. (discussed previosly in Features Left to Implement) 
    - [x] Edit vendor profiles.
    - [x] Delete vendor profiles tested.
    - [x] For vendor_profile_one, go to Vendor Food Gallery.
    - [x] Add new foods. Reference as name vendor_profile_one_food_one & vendor_profile_one_food_two.
    - [x] Delete food tested.
    - [x] Edit food tested.
    - [x] For vendor_profile_one, go to Add delivery area.
    - [x] Added 10 towns.
    - [x] Delete towns tested.
    - [x] Added 10 postal codes.
    - [x] Delete postal code tested.
    - [x] Log Out as vendor.

Secondly, I will move on to test as customer with following account.
- User: Customer
- email: Customer@email.com
- password: tomjerry123

2. My Home page:
    - [x] Login as customer.
    - [x] Create two profiles for Yishun (123123) and Ang Mo Kio (999999).
    - [x] Delete profile tested.
    - [x] Edit profiles tested.
    - [x] Go Back to my Home.
    - [x] Check current profile changes when switch between both profiles
    - [x] Check filtering by vendors and food. Checked search box by vendor and food.
    - [x] Displayed vendors and foods also tally to the chosen profile. Matching towns and postal codes.
    - [x] Add foods to cart. Remember to add food item from vendor_profile_one. **The vendor_profile_one is default locked in database when just created. It needs an admin user to unlock it. While unlocked, the food display for 
        vendor_profile_one will show as "Unavailable". Upon unlock, add cart button is shown. This feature is for background check on vendor that they are legitimate by the site creator or administrator.**
    - [x] Open shopping cart page. Test the addition, minus, remove buttons. Ensure the qty, price updates are correct.
    - [x] Checkout shopping cart. After submission in Stripe,  redirects to "Checkout Success" page.
    - [x] Refresh shopping cart page. Ensure that shopping cart becomes empty.
    - [x] Go to My Orders page, the orders entry previously will appear here accordingly.
    - [x] Logout as customer.

3. Vendor page:
    - [x] Login as vendor.
    - [x] Go to vendor access page. Under vendor_profile_one,  go to check orders button. The food ordered can be seen in outstanding orders table.
    - [x] Checked on the deliver checkbox. The row of order will transfer to the completed orders table.

The website works for chrome, internet edge and firefox. 
The mobile responsiveness are checked for sizes e.g. iphone5/7/8, ipad etc. with no issues.
    
## Deployment

This website is deployed to hosting platform Heroku from this git origin master branch.
For running the codes locally, 
1. In terminal, enter pip3 install -r requirements.txt to install the required packages per stated in the txt file.
2. The project is built with django 2.2.6. Install django e.g. pip3 install django==2.2.6
3. Setup your own configurations keys which consist of ("STRIPE_PUBLISHABLE_KEY", "STRIPE_SECRET_KEY", "SIGNING_SECRET", "UPLOADCARE_PUBLIC_KEY", "UPLOADCARE_SECRET_KEY" & "DATABASE_URL")

### Testers account

The following accounts are available for running and trying out the website.
Alternatively, one can create an account and email notification will be sent to his/her email to confirm the email link. 

user: Customer
email : Customer@email.com 
password: tomjerry123

user: vendor
email: vendor@email.com
password: spidervenom123

## Credits

### Media
- The photos used in this site are obtained from [PixaBay](https://pixabay.com/).
- The 8bear logo is an original personal content.

### Acknowledgements

- Trent Global and Paul Chor Kun Xin for advises, guidances and helpful materials.
