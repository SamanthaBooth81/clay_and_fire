<h1 align="center">Clay & Fire Jewellery</h1>

<img src="assets/readme_images/responsive-img.png" height="400px">

### **Live Site**
[Clay & Fire Live Site](https://clay-and-fire.herokuapp.com/)

### **Repository:**
[Clay & Fire Repository](https://github.com/SamanthaBooth81/clay_and_fire)

# About
This website was created to sell handmade clay jewellery to shoppers. It is an E-commerce shop that provides a platform for the seller to sell their handmade jewellery to those who support small businesses and would like to purchase something different.
 

# Table of Contents

[User Experience](#user-experience)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

[Wireframes](#wireframes)

[Databases](#databases)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Validator Testing](#validator-testing)

[Bugs Found](#bugs-found)

[Marketing Strategies](#marketing-strategies)

[Search Engine Optimisation (SEO)](#search-engine-optimisation-seo)

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)

# User Experience
## User Stories
### Superuser / Admin
1.	As a Site Owner I want to be able to add a product so that I can add more items to my store.
2.	As a Site Owner I want to be able to Edit/Update a product so that I can change the price, description, and other product criteria.
3.	As a Site Owner I want to be able to delete a product so that I can remove items that are no longer available.
4.	As a Site Owner I want to be able to send email to customers with a. subscription, notifying customers of any deals, sale and new arrivals.

### Shopper
1.	As a Shopper I want to be able to view a list of items so that I can add to me basket.
2.	As a shopper I want to be able to click into an item so that I can view a product description and add to the basket.
3.	As a shopper I want to be able to add items to my basket so that I can keep track of what I am spending.
4.	As a shopper I want to be able to be able to adjust the quantity of products in my basket so that I can make changes to my purchases before checkout.
5.	As a shopper I want to be able to be able to enter payment information so that I can check out quickly and hassle free.
6.	As a shopper I want to be able to be able to feel that my personal and payment details are safe and secure so that I can confidently carry out my purchase.
7.	As a shopper I want to be able to be able to view an order confirmation so that I can verify my order is correct.
8.	As a shopper I want to be able to receive an email confirmation of my order so that |I have proof of my order for my records.
9.	As a shopper I want to be able to be able to order without creating an account so that I can make one off orders.
10.	As a shopper I want to be able to be able to sort a specific category of a products so that I can find the best price quickly for the product I am looking for.
11.	As a shopper I want to be able to be able to sort multiple categories and products simultaneously so that I can find the best priced product over a broader range of categories
12.	As a shopper I want to be able to be able to easily see what I’ve searched for and the number of results so that I can quickly see whether the product is available.
13.	As a shopper I want to be able to be able to easily register for an account so that I can have a personal account and view my profile and purchase history.
14.	As a shopper I want to be able to be able to recover my password so that I can recover my account access.
15.	As a shopper I want to be able to be able to receive a registration confirmation email so that I can confirm registration.
16.	As a shopper I want to be able to be able to sign up for email so that I can be notified of new releases, deals and upcoming sales.

# Features
- Logo / Shop Name

<img src="assets/readme_images/nav-landing.png" width="50%">

- Search Bar 

<img src="assets/readme_images/nav-all.png" width="50%">

- My Profile 

<img src="assets/readme_images/nav-all.png" width="50%">

- Account Registration

<img src="assets/readme_images/register.png" width="50%">

- Login

<img src="assets/readme_images/login.png" width="50%">

- Change Password

<img src="assets/readme_images/change-pw.png" width="50%">

- Shopping Bag

<img src="assets/readme_images/nav-all.png" width="50%">

- Navbar

<img src="assets/readme_images/navbar.png" width="50%">

- Landing Image

<img src="assets/readme_images/nav-landing.png" width="50%">

- Homepage Message

<img src="assets/readme_images/home-recipelist.png" width="50%">

- Products Page 

<img src="assets/readme_images/detail.png" width="50%">

- View Full Product Details 

<img src="assets/readme_images/detail.png" width="50%">

- Footer

<img src="assets/readme_images/footer.png" width="50%">

- Footer Subscription Sign Up

<img src="assets/readme_images/footer.png" width="50%">

- Contact Form

<img src="assets/readme_images/footer.png" width="50%">

## Admin Features
- Product Management
<img src="assets/readme_images/footer.png" width="50%">

- Edit Products
<img src="assets/readme_images/footer.png" width="50%">

- Delete Products
<img src="assets/readme_images/footer.png" width="50%">

## Colour Scheme 

The colour scheme for the project was put together using [Adobe Color](https://color.adobe.com/create/image) by uploading the landing page image. The colour scheme decided is:

<img src="assets/readme_images/color-choice.png" width="500px">

## Font Choice

I chose the Google Font Raleway to act as the primary font for the website, including for the logo.

<img src="assets/readme_images/raleway.png" width="200px"> **ADD FONT IMAGE**


## Favicon 
I created a basic Favicon for this project using [Canva](https://www.canva.com/). 

<img src="assets/readme_images/favicon.png" height="150px"> **ADD FAVICON IMAGE**


# Features to be Implemented
The following features can be implemented to enhance the project:

- Feedback Board for Shoppers
- Save items to favourites
- Instagram Carousel to show products on shoppers
- Featured items on homepage

# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Clay & Fire Wireframes for Mobiles, Tablets and Desktop devices can be viewed [here](assets/documents/Wireframes.pdf).

# Structure
This project is structured with a homepage that greets the user with a clear navigation at the top of the page to search for the item required or to browse all products. There is the ability to sort items by price, alphabetically and by category as well as the ability to search for a product by typing in keywords into the search bar.

Furthermore, users have the option to checkout as guests or create a profile for themselves which can contain their delivery address and does contain their order history.

The website is made of the following apps:
1. Home
2. Products
3. Profile
4. Bag
5. Checkout
6. Company Info

## Databases
### Category
<img src="assets/readme_images/category-model.png" width="350px">

### Products
<img src="assets/readme_images/products-model.png" height="130px">

### Order
<img src="assets/readme_images/order-model.png" width="350px">

### Order Line Items
<img src="assets/readme_images/order-line-item-model.png" height="100px">

### User Profile
<img src="assets/readme_images/user-profile-model.png" width="350px">

### User

For this I project I also used Django's User model to store registration information allowing the users to create an account. Once an account has been created the user is able to create, update and delete their own recipes on the site. 

# Technologies Used
## Languages Used

[html](https://en.wikipedia.org/wiki/HTML)

[CSS](https://en.wikipedia.org/wiki/CSS)

[Python](https://www.python.org/)

[JavaScript](https://www.javascript.com/)

## Frameworks, Libraries and Programmes Used 

[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project, reducing time spent getting the project setup and prevent re-writing existing code.


[Bootstrap](https://getbootstrap.com/) - Used to quickly add design and responsiveness to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes.

# Testing
## **Manual Testing by User Story**
### **Superuser / Admin**
### 1. As a Site Owner I want to be able to add a product so that I can add more items to my store.
- Products can be added both via the project management page found by clicking on 'My Account' or vis the Admin Panel.
- The required fields are validating correctly and error messages are explicit and related to each required field.
- All required fields are indicated with an asterisk.
- Number fields can only contain numbers.
- Images can be left out and a placeholder image takes its place.
- Images, when uploaded, are stored in the appropriate Amazon Web Services Bucket and Folder.
- Buttons are highlighted on hover and take the user to the correct page:
    - Cancel takes the user back to the Products Page
    - Add product add the product and returns the user to the Products Page
- An alert message appears in the top right of the page to notify the user that the product has successfully been added.

### 2.	As a Site Owner I want to be able to Edit/Update a product so that I can change the price, description, and other product criteria.
- Edit buttons are located on the product cards on the products page which are only accessible if you are a super user. 
- Clicking the Edit button takes the user to the product form which is already populated with the current information.
- The fields are validated the same was as if a new product was being added, all number fields must be numbers and required fields filled in. 
- The image can also be removed an the placeholder image will replace it upon saving.
- If the image is replace with a new image it is stored in the correct Amazon Web Services Bucket and Folder.
- The name of the image uploaded can be the same as an image that exists.
- An alert message appears in the top right of the page to notify the user which product they are currently editing.
- Buttons are highlighted on hover and take the user to the correct page:
    - Cancel takes the user back to the Products Page
    - Update product saves the updated product information and returns the user to the Products Page. This is confirmed via the admin panel and the details viewed on the Product Details page.

### 3.	As a Site Owner I want to be able to delete a product so that I can remove items that are no longer available.
- Clicking delete removes the product from the product model.
- The product is no longer listed with the live products.
- The user cannot view the product with the url. Using the link for a product that no longer exists takes the user to a 404 error page.
- Success message at top right of page when product successfully deleted.

### 4.	As a Site Owner I want to be able to send email to customers with a subscription, notifying customers of any deals, sale and new arrivals.

- Customers who sign up for emails are added to the businesses mailchimp contacts list where they can be unsubscribed. Users can contact the owner via the 'contact us' form in the footer to unsubscribe. 
- Unsubscribed users can re-subscribe by submitting their email again.
- An error message is displayed underneath the email box if there is an issue with the email provided
- A success message is displayed underneath the email box to confirm subscription


### **Shopper**
### 1. As a Shopper I want to be able to view a list of items so that I can add to me basket.

- All products are displayed using Bootstrap Cards and Responsiveness classes to ensure the card layout changes dependant on screen size.

- Products can be viewed together or by category and can be further filtered using the sort box on the top right of the products pages. 

- All product images are displayed and where they do not exist there is a placeholder.

- All products have a required title, price and category attached to the product card.

- Edit and Delete buttons are unavailable to non-superusers.

###	2. As a shopper I want to be able to click into an item so that I can view a product description and add to the basket.

- On clicking an item you are taken to the correct item as the product image, title and price matches that product card.

- The user can see a description of the item they are viewing.

### 3. As a shopper I want to be able to add items to my basket so that I can keep track of what I am spending.

The following scenarios were tested by checking the items added to the Shopping Bag:

- Add an item to the bag and check it is in there with the correct quantity.

- Increase the quantity before adding to the shopping bag and checking whether the quantity in the bag matches was was added.

- If the user types 0 or a quantity over 99, an error message by the quantity field notifies the user that the quantity can be between 1-99 only. If the user uses the buttons, they are disabled if attempting to decrement to 0 or increment above 99. 

- Once an item has been added to the shopping bag a success message appears in the top right corning, notifying the user of the specific product and quantity added, how much more to spend to save on delivery and a link to the shopping bag.

All items were added as they should be to the shopping bag and tested through to order completion to ensure it the items added to the shopping bag matched in the completed order. 

### 4. As a shopper I want to be able to be able to adjust the quantity of products in my basket so that I can make changes to my purchases before checkout.

The following scenarios were tested by completing the order and checking what was submitted in the Admin:

- Increasing the Quantity of an item in the shopping bag.

- Decreasing the Quantity of an item in the shopping bag.

- Removing an item out of the shopping bag.

All of the above actions are reflected correctly in the Order database along with the correct total delivery and grand total prices. 

### 5. As a shopper I want to be able to be able to enter payment information so that I can check out quickly and hassle free.

The checkout function was tested using Stripes test card numbers. 

The following scenarios were tested to ensure the checkout went through securely:

- Submitting an order, completing only the required fields on the checkout form. The order went through both on Stripe and stored in the Database with a success Webhook message.

- Attempting to submit an order with incorrect card details. An error message appears underneath the card details form confirming the details are incorrect.

- Attempting to submit an order with an expired card. An error message appears underneath the card details form confirming the card has expired.

- Submitting an order, completing only the required fields on the checkout form, with the form.submit() within the stripe_elements.js file commented out to simulate a user closing the page before the checkout success confirmation page has loaded. The order went through both on Stripe and stored in the Database with a success Webhook message.

- Attempting to submit an order with an incomplete order form. All empty required fields alert the user they must be filled to be completed and the form isn't submitted. 

The Order total was also compared on the checkout page, the successful checkout page, on Stripe and within the Order database to ensure all totals matched.

### 6. As a shopper I want to be able to be able to feel that my personal and payment details are safe and secure so that I can confidently carry out my purchase.

- Address details can be saved if the user has an account and updated/removed if the user wishes. 

- The project uses Stripe to process payments, keeping the users payment information safe and not stored within their user profile. 

- Payment information isn't stored in the projects models.

### 7. As a shopper I want to be able to be able to view an order confirmation so that I can verify my order is correct.

- Users with a profile have a list of orders made on their profile page. Clicking the order number takes the user to view the confirmation page that was displayed directly upon checkout. The confirmation contains the following details of the purchase:
    - Order Number
    - Order Date
    - Product Name and Quantity
    - Price per item
    - Delivering to
    - Phone Number
    - Address
    - Order Total
    - Delivery Cost
    - Grande Total

- The above details contained within the order confirmation matched the bag items, order total and the order in the database.

### 8. As a shopper I want to be able to receive an email confirmation of my order so that |I have proof of my order for my records.

- Email confirmation was tested by placing an order to an email address that can be checked. An email confirmation matching the template set up in the checkout app was received with the correct order details within and a contact email for if there was an issue with the order.

### 9. As a shopper I want to be able to be able to order without creating an account so that I can make one off orders.

An order was placed without being logged into an account. It was tested by comparing the the order confirmation, email confirmation and the order within the order model to ensure it matched what was placed in the bag and then checked out. Also the order event on Strip matched the total cost of the order. 

### 10. As a shopper I want to be able to be able to sort a specific category of a products so that I can find the best price quickly for the product I am looking for.

- The navigation contains the multiple categories on offer. It was tested by clicking through and ensuring the category tag on each product card matched the category the page was displaying. 

- within the following Nav headings, their particular categories are listed at the top when all of that selected is clicked into allowing for further filtering per section:
    - Earrings
    - Necklaces
    - Special Offers

### 11. As a shopper I want to be able to be able to sort multiple categories and products simultaneously so that I can find the best priced product over a broader range of categories

Testing the sort functionality was done within the all products tab as it contained the majority of products. The sort options tested were:

- Price (Low to High)
- Price (High to Low)

These were tested by checking the first and last price of the items on the page to check they sorted correctly. 

- Rating (Low to High)
- Rating (High to Low)

These were tested by checking the first and last rating of the items on the page to check they sorted correctly. 

- Name (A to Z)
- Name (Z to A)

These were tested by checking the first and last Name of the items on the page where in alphabetical order. 

- Category (A to Z)
- Category (Z to A)

These were tested by checking the through the list items on the page, checking the categories where in alphabetical order. 

### 12. As a shopper I want to be able to be able to easily see what I’ve searched for and the number of results so that I can quickly see whether the product is available.

This was tested by:

- Searching via the search box
- Searching through the categories 

The quantity for the search is displayed at the top left of the page, the number displayed matched the number of searches on each page. 

### 13. As a shopper I want to be able to be able to easily register for an account so that I can have a personal account and view my profile and purchase history.

This was tested by registering a couple of user accounts and:

- logging out and back in to ensure they worked
- Confirming the account via email
- Checking the Admin panel for confirmed email addresses

The above ensured the user accounts were generated. 

To test profile information I added an address and attempted to checkout an item. This ensured that the address saved in the profile auto filled on the checkout page. To test this further, I made an order ensuring the save details to profile checkbox is ticked, and checked the address saved to the profile. 

To test the order history, I checked whether the orders placed to test the profile information had saved to the profile and the information contained in the order matched what was placed in the bag and checked out.

### 14. As a shopper I want to be able to be able to recover my password so that I can recover my account access.

This was tested by clicking the 'Forgot Password' link at the bottom of the login page. The user then receives a link via email, therefore I tested this with an existing email to ensure the link was received.

There is a wait for the password re-set link to be sent but when it comes through, the user is taken to a page where they reset the password by entering it twice. After the new password has been entered, the user is re-directed to a confirmation page with a bootstrap toast displaying a success message. If the passwords do not match then an error message notifies the user so they can try again.

Once reset, the user must then re-login with the new password, which was tested to confirm the password change and that the correct user is now logged in.

### 15. As a shopper I want to be able to be able to receive a registration confirmation email so that I can confirm registration.

This was tested by registering for an account. In order to complete registration the user must receive an email with a link that confirms their email address. This was tested with an outlook email address that was created for testing. The email was received and the account was confirmed via the link.
### 16. As a shopper I want to be able to be able to sign up for email so that I can be notified of new releases, deals and upcoming sales.

Contained in the footer, the user can subscribe by entering their email and clicking submit. If there is an error with the email, an error message appears underneath the email box. If successful then there is a success message under the email box. 

The subscription was tested by using a test email to subscribe and logging into mailchimp and checking the contacts. Once confirmed the contact was there I scrolled across to see if they were subscribed. From here I also tested unsubscribing a user to ensure it is possible if a request came in. 

### 17. As a shopper I want to be able to be able to contact the site owner so that I can ask about my order or for further information not contained within the Footer Pages.

The contact form link is placed within the footer and takes the user to the contact page. The form was tested by ensuring:

- the required fields must be completed before submittal.
- The form fields took the correct information:
    - the email input took only emails
- The message box could hold enough text for a message.
- the form submitted the message to a working email for the site owner to respond.

**Peer Code Review**

My project was shared on Slack with other Code Institute students. The feedback received was: 

# Validator Testing

- The HTML templates were validated using [W3 Validator](https://validator.w3.org/nu/#textarea). No major errors were returned for the html segments.
- The CSS style sheet was validated using [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input), no errors were returned.
- The JavaScript files were run through [JSHint](https://jshint.com/), errors were found.
- The code was validated using [PEP8](http://pep8online.com/). No errors were returned.
- The finished project was also run through [Wave](https://wave.webaim.org/) to check for issues with contrast styling and html structure. 

# Bugs Found 

I encountered the following issues whilst building this project:
- The Footer wasn't sticking to bottom on some of the pages. To fix this I added a 'h-100' Bootstrap class to the container divs. 

- The Success Message wasn't working when removing items from cart. To fix this I needed to get the product ID to identify which Item was being deleted in the message

- The Shopping bag was repeating 'Continue Shopping' and 'Add to Bag' buttons after every item in the bag. To fix this I moved the {% endfor %} for the {% if bag_items %} to be before the buttons.

- Incorrect Stripe public key in checkout view. I accidentally wrote the public key in the context in capitals. 

- I was able to add products to categories not on dropdown list. To fix this I had to remove the non-existing categories in the admin panel and remove/change to category of the products added to these categories.

- Deploy not completing - message received: ERROR: Could not find a version that satisfies the requirement python-apt==2.0.0+ubuntu0.20.4.7 (from versions: 0.0.0, 0.7.8). To fix this I removed the un-required installs from requirements.txt file.

- The Webhook for the live site was generating a 301 error. To fix this I had to add a / at the end of the url the webhook was set up to.

- The delivery confirmation page image wasn't Loading on the deployed site. To fix this I changed the image source to the images [AWS](https://aws.amazon.com/?nc2=h_lg) url to display the image.

# Marketing Strategies

1.	Who are your users?

- Woman who enjoy fashion and accessorising
- Loved ones looking for gifts
- Woman ages between 15 and 45 roughly

2.	Which online platforms would you find lots of your users?

- Facebook
- Instagram
- Tiktok
- Etsy

3.	Would your users use social media? If yes, which platforms do you think you would find them on?

- Facebook
- Instagram
- Tiktok

4.	What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?

- Style Inspiration: 
    - Instagram Posts of our jewellery styled and possible combinations
    - TikTok Videos following current editing trends
- Gift Inspiration
    - Instagram Posts of gift ideas and product combinations
    - Emails with gift ideas, particularly around Christmas or other holidays

5.	Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?

- Email deals for subscribers
- Sale Emails and Instagram Posts/Stories

6.	What are the goals of your business? Which marketing strategies would offer the best ways to meet those goals?

- Make Sales
- Gather repeat customers

7.	Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?

- Free/low cost marketing as the budget would need to go towards materials required to create and deliver high quality products

The below business both sell polymer clay jewellery. As you can see from both of these examples their most successful Social Media platform in terms of following is TikTok, followed by Instagram and lastly Facebook. 
### Shopmalcreates: 
FB Page 535 likes, Instagram 32.7k followers, TikTok 1232 followers
### Indigo Sands: 
FB Page 4037 likes, Instagram 92.4K followers, TikTok 225.7K followers

Although seemingly a successful tool for building a following, as TikTok is a fast-paced video based platform, I have created Instagram and Facebook accounts to act as the Social Media platform this business uses alongside email marketing. 
# Search Engine Optimisation (SEO)
In order to find the relevant keywords for my project I made the following searches on [Google](www.google.co.uk) and [Word Tracker](www.wordtracker.com)  along with a few combinations:

-	Clay Jewellery
-	Polymer Clay Jewellery
-	Baked Clay Jewellery
-	Handmade jewellery
-	Handmade clay jewellery
-	Handmade gifts
-	Ladies handmade gifts
-	Gift ideas for woman

Of the above, the top combination of searches  I found were:

-	Handmade Polymer Clay Jewellery
-	Handmade Jewellery Gifts 
-	Handmade Women’s Jewellery
-	Handmade Jewellery UK
-	Handmade Jewellery

Of the above searches, Handmade Polymer Clay Jewellery best suited what my project is selling and had the highest search rate of all keywords attempted. With that in mind, I have selected the following to be included in my projects metadata:

-	Handmade Jewellery Gifts
-	Handmade Polymer Clay Jewellery
-	Handmade Jewellery
-	Polymer Clay Jewellery

Also, I included ‘Handmade Jewellery’ within the homepage message’ along with a subheading of ‘Find the perfect gift today!’ 

# Deployment 

This project was deployed using Heroku. At the time of deployment Heroku was facing a security issue, therefore this project was deployed via the command line in GitPod and those are the steps detailed below. As this was the case I was unable to allow automatic deployments in Heroku each time a commit was pushed into the repository.

See the following steps to deploy below:

1. Login to Heroku and Create a New App.

2. Give the App a name, it must be unique, and select a region closest to you. 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Next, click on the 'Resources' tab and search for 'Heroku Postgres' in the Add-ons section to add the Heroku Postgres database to the project. 

5. Click on the 'Settings' tab at the top of the page. The following steps must be completed before deployment.

6. Within the settings.py file you need to import os and import dj_database_url at the top. Then, in the command line install dj_database_url and psycopg2 so that we can use Postgres. Freeze these installs into the requirements.txt file.

7. Scroll down to Config Vars (also known as Environment Variables) and click 'Reveal Config Vars'. Here the database URL is stored to run my app on Heroku. 

I used an if statement in settings.py (see below), so that when our app is running in Heroku, we connect to Postgres but in our local environment, we connect to sequel light:

    development = os.environ.get('DEVELOPMENT', False)

    if development:

            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

        else:

            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }


8. Next I ran the migrations again to set up my Postgres Database by running **Python 3 manage.py migrate** within the command line and then create a Superuser using **python3 manage.py create superuser**.

9. Following setting up the database I generated a new Secret Key, to replace the insecure key that was in settings.py and added: **os.environ.get('SECRET_KEY')**. I then added the new generated key to the Config Vars on Heroku. 

10. We must then need to install gunicorn, which will act as our webserver and freeze that into our requirements file.

11. I then created a Procfile to tell Heroku to create a web dyno which will run gunicorn and serve our django app.

Within this file add the following:

    web: gunicorn clay_and_fire.wsgi

Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.

12. I then told Heroku temporarily disabled collectstatic by using Heroku config set, disable collectstatic = 1. I added this via Heroku's Config Vars but this can also be added via the command line. This was to prevent Heroku from attempting to deploy the static files, causing an error, until Amazon Web Services was set up. 

13. Then add the hostname of our Heroku app to allowed hosts in settings.py as well as localhost so that GitPod will still work too.

14. I then committed and pushed these changes into my GitHub repository so that I could start my first deployment. Once complete, log into Heroku using the following command in the terminal, **heroku login -i**,  and entering your login details.

15. Once logged in, add a remote to your local repository with heroku git:remote command and your Heroku app’s name: **heroku git:remote -a clay-and-fire**

16. Finally, to deploy use the following command: **git push heroku main**. Once deployed you can open the app from the command line to ensure it was successfully deployed.

17. Once we can confirm the app deployed successfully, we need to set-up Amazon Web Services as this will be where my media and static files are stored. To do this I first created an account with Amazon Web Services. Then, I searched for the service, S3, using the search bar at the top of the page. 

18. Click into it and then click the orange 'Create a Bucket' button. I named this bucked to match my clay-and-fire Heroku app name to keep things simple. Then, I selected my region and changed the 'Object Ownership' setting to **ACLs enabled**. Then, I unchecked block all public access, acknowledged that the bucket will be public and click on the 'Create Bucket' button.

19. Next, on the properties tab, I scrolled to the bottom and turned on static website hosting.
This gave me a new endpoint that I can use to access it from the internet. For the index and error document, I filled in some default values and then click save.

20. Now on the permissions tab I pasted in the following coors configuration:

    [
        
        {
            "AllowedHeaders": [
            "Authorization"
            ],

            "AllowedMethods": [
            "GET"
            ],

            "AllowedOrigins": [
            "*"
            ],

            "ExposeHeaders": []
        }
        
    ]

which is going to set up the required access between our Heroku app and this s3 bucket.

21. Next I'll go to the bucket policy tab a select, policy generator so we can create a security policy for this bucket. The policy type is going to be s3 bucket policy and then allow all principals by using a '*' and the action will be, get object. Next I'll copied the ARN which stands for Amazon resource name from the other tab pasted it into the ARN box here at the bottom. I then clicked 'Add statement' and then 'Generate Policy'.

22. I then copied this policy into the bucket policy editor. I then added '/*' at the end of the resource key to allow access to all resources in this bucket and then saved it.

23. Finally, to complete configuration, I went to the 'access control list' tab and checked edit and enable List for Everyone (public access) and accepted the warning box..

24. Next I created a group and a user to access the bucket by searching for the service IAM (Identify and Access Management). I clicked on 'User Groups' and then 'Create User Group' giving it the name 'manage-clay-and-fire'. 

25. I then created the Policy used to access our bucket by clicking policies and then create policy. I clicked onto JSON tab and then selected import managed policy in order to
import one that AWS has pre-built for full access to s3.

26. I searched for s3 and then import the s3 full access policy. I then got the bucket ARN from the bucket policy page in s3 and pasted that into the 'Resource' section on the JSON tab.

I then clicked the next tabs until I reached 'Review Policy' and gave it a name and a description and then clicked 'Create Policy'. This took me back to the policies page.

27. Next I attached the policy to the Group I created by return to the Create User Group page and refreshing the Policies box. I then was able to attach the new policy created by selecting it and finally clicking 'Create Group'.

28. Finally I'll created a user to put in the group by going to the User's page and clicking 'Add User'. I created a user named **clay-and-fire-static-files-user**, gave them Programmatic Access and clicked 'Create User'. 

29. I then downloaded the CSV file which contained this users access key and secret access key which I used to authenticate them from my Django app. It is important to download this file as you cannot be re-downloaded and contains the new users credentials which I next add to the Config Vars on Heroku.

30. Next, I connected Django to the new S3 bucket. To do this I installed two new packages:
- boto3
- django-storages 

31. I then pip3 freezed these to the requirements.txt file to ensure they're installed on the next Heroku Deploy and added **storages** to our installed apps in settings.py. 

32. To connect Django to S3 (only on Heroku) I then added the following in if statement settings.py:

        if 'USE_AWS' in os.environ:
            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = 'clay-and-fire'
            AWS_S3_REGION_NAME = 'eu-west-2'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


33. I then added the following to our Config Vars on Heroku:
- USE_AWS = True
- AWS_ACCESS_KEY_ID, taken from the new user credentials
- AWS_SECRET_ACCESS_KEY, taken from the new user credentials

and removed:
- Remove staticcollect=1 from congifvars within Heroku 

I also set DEBUG Set DEBUG to 'DEVELOPMENT' in os.environ as it cannot be set to True as it is locally on the deployed version. 

34. The next step is to tell django that in production we want to use s3 to store our static files whenever someone runs collectstatic and that we want any uploaded product images to go there also. To do that I created a file called custom_storages.py.

35. Within this file I imported both our settings from django.conf and the s3boto3 storage class from django storages. Then I created custom classes for static storage and media storage which inherited the imported class from django storages to give it all its functionality. Then I set the class to store static and media files in the location specified in the USE_AWS if statement within settings.py.

36. Finally, to complete deployment of AWS setup, I committed the changes and pushed them to GitHub. In the command line I then typed the following command: **git push heroku main**. If you need to login to Heroku again completed steps 14 - 16 to re-deploy. Once Heroku is allowing users to connect to their GitHub accounts you can set up automatic deploys which will remove the need to repeat these steps.
# Credit
## Content 

I used the Code Institutes Boutique Ado Follow Along project to help with building this project along with the following websites:

- [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) to generate a new Django Secret Key.

- [Sculpey Blog Post](https://www.sculpey.com/create/blog/10-surprising-facts-about-polymer-clay#:~:text=Polymer%20clay%20is%20non%2Dtoxic,use%20around%20children%20and%20pets.) was used to gather information about polymer clay for the FAQ's page.

- I used [H&M](https://hmgroup.com/about-us/our-values/), [Oysho](https://www.oysho.com/gb/company.html) and [Accessorize](https://www.accessorize.com/uk/our-brand.html) to see how they shared their Policies and Frequently Asked Questions with their customers for content ideas.

- [GDPR Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to generate the Privacy Policy that was added to the footer.

- [Scottish Coder YouTube Tutorial](https://www.youtube.com/watch?v=1DcySa35fXw) was used to help with creating a working contact form view.

### Styling
- [Unsplash - Landing Image](https://unsplash.com/photos/uRuF9ABj0NY)
- [Logo Font - Google Fonts](https://fonts.google.com/specimen/Raleway?query=raleway)
- [Font Awesome Icons](https://fontawesome.com/)
- [CSS-Tricks - Flexbox Sticky Footer](https://css-tricks.com/couple-takes-sticky-footer/), for the sticky footer code.
- [Bootstrap](https://getbootstrap.com/docs/4.2/components/spinners/) - Overlay Spinner on checkout page.

### Product Images
- 'noimage.png' taken from Code Institutes Boutique Ado Follow Along Project
- [Pexels - Carpe Jugulum](https://www.pexels.com/photo/orange-and-black-ladybug-on-green-leaf-5035921/)
- [Pexels - Lisa Fotios](https://www.pexels.com/photo/a-woman-with-a-face-shaped-earring-7016917/)
- [Pexels - cottonbro](https://www.pexels.com/photo/close-up-shot-of-a-woman-wearing-a-blue-earring-8541542/)
- [Unsplash - Svitlana](https://unsplash.com/photos/J7ydFF1WyGQ)
- [Unsplash - Kate Hliznitsova](https://unsplash.com/photos/P6NiFTyI294)
- [Unsplash - Sincerely Media](https://unsplash.com/photos/8WebmlRgMp0)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/YGIPzuiD1jc)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/YbA4hHxkSrg)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/O7l3PmbGxF0)
- [Unsplash - Gabrielle Henderson](https://unsplash.com/photos/fR3PIa-WtBg)

### Website Images
- [Pexels - Delivery Image](https://www.pexels.com/photo/person-holding-green-and-white-floral-book-5486791/)


# Acknowledgments
Thank you to all who encouraged and supported me as I created my first full stack E-Commerce website, especially to my mentor at Code Institute, Antonio, for his guidance, patience, encouragement and constant support. Also a massive thank you to Tutor Support at the Code Institute for never giving up on the difficult issues I found myself facing.  