<h1 align="center">Clay & Fire Jewellery</h1>

<img src="assets/readme_images/responsive-img.png" height="400px">

### **Live Site**
[Clay & Fire Repository](https://github.com/SamanthaBooth81/foody-family)

### **Repository:**
[Clay & Fire Live Site](https://foody-family.herokuapp.com/)

# About

 

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

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)

# User Experience
## User Stories
### Superuser / Admin

### Shopper

# Features
- Landing Image

<img src="assets/readme_images/nav-landing.png" width="50%">

- Navbar 

<img src="assets/readme_images/nav-all.png" width="50%">

- Navbar - Account holders

<img src="assets/readme_images/navbar.png" width="50%">

- Filters

<img src="assets/readme_images/detail.png" width="50%">

- Products List

<img src="assets/readme_images/home-recipelist.png" width="50%">

- View Full Product Details 

<img src="assets/readme_images/detail.png" width="50%">

- Create an account

<img src="assets/readme_images/register.png" width="50%">

- Login

<img src="assets/readme_images/login.png" width="50%">

- Change Password

<img src="assets/readme_images/change-pw.png" width="50%">

- Footer

<img src="assets/readme_images/footer.png" width="50%">

## Admin Features
- Add products
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

<img src="assets/readme_images/ribeye-marrow.png" width="200px"> **ADD FONT IMAGE**


## Favicon 
I created a basic Favicon for this project using [Canva](https://www.canva.com/). 

<img src="assets/readme_images/favicon.png" height="150px"> **ADD FAVICON IMAGE**


# Features to be Implemented


# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Clay & Fire Wireframes for Mobiles, Tablets and Desktop devices can be viewed [here](assets/documents/Wireframes.pdf).

# Structure
I have kept the structure simple to not crowd the user with information. The homepage contains all of the recipes that are approved by the superuser/admin, which is also paginated therefore limits the recipe cards to 12 per page. 

The website is made of the following apps:
1. Home
2. Products
3. 

## Databases

### User

For this I project I used Django's User model to store registration information allowing the users to create an account. Once an account has been created the user is able to create, update and delete their own recipes on the site. 

### Recipes

For the user to be able to upload their own recipes I have created the below Recipe Model:

<img src="assets/readme_images/recipe-model.png" width="500px">

All fields are required apart from Author - which is based on the user who is currently logged in, Featured Image - which uses a placeholder if no image is uploaded and Excerpt - which is for the user to add any additional notes if required. 
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
## Manual Testing by User Story
### **Superuser / Admin**
**Add Product**
- 

**Delete Product**
- 

### **Buyer**
**View List of Products**
- 

**View Product Details**
- 

**Add Items to Shopping Bag**
The following scenarios were tested by checking the items added to the Shopping Bag:
- Add an item to the bag and check it is in there with the correct quantity.
- Increase the quantity before adding to the shopping bag and checking whether the quantity in the bag matches was was added.
All items were added as they should be to the shopping bag and tested through to order completion to ensure it the items added to the shopping bag matched in the completed order. 

**Amend Shopping Bag**
The following scenarios were attempted and tested by completing the order and checking what was submitted in the Admin.
- Increasing the Quantity of an item in the shopping bag.
- Decreasing the Quantity of an item in the shopping bag.
- Removing an item out of the shopping bag.

All of the above actions are reflected correctly in the Order database along with the correct total delivery and grand total prices. 

**Checkout**

The checkout function was tested using Stripes test card numbers. 

The following scenarios were tested to ensure the checkout went through securely:
- Submitting an order, completing only the required fields on the checkout form. The order went through both on Stripe and stored in the Database with a success Webhook message.
- Attempting to submit an order with incorrect card details. An error message appears underneath the card details form confirming the details are incorrect. 
- Attempting to submit an order with an expired card. An error message appears underneath the card details form confirming the card has expired.
- Submitting an order, completing only the required fields on the checkout form, with the form.submit() within the stripe_elements.js file commented out to simulate a user closing the page before the checkout success confirmation page has loaded. The order went through both on Stripe and stored in the Database with a success Webhook message.
- Attempting to submit an order with an incomplete order form. All empty required fields alert the user they must be filled to be completed and the form isn't submitted. 

The Order total was also compared on the checkout page, the successful checkout page, on Stripe and within the Order database to ensure all totals matched.

## General Manual Testing 
**User Registration**



**Peer Code Review**


# Validator Testing

- The HTML templates were validated using [W3 Validator](https://validator.w3.org/nu/#textarea). No errors were returned for the html segments.
- The CSS style sheet was validated using [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input), no errors were returned.
- The JavaScript files were run through [JSHint](https://jshint.com/), no errors were found.
- The code was validated using [PEP8](http://pep8online.com/). No errors were returned.
- The finished project was also run through [Wave](https://wave.webaim.org/) to check for issues with contrast styling and html structure. 

# Bugs Found 

I encountered the following issues whilst building this project:


# Deployment 

This project was deployed using Heroku. Some of the steps in this deployment process are used to get the bare minimum of this project up and running prior to adding functionality. 

See the following steps to deploy below:

1. Login to Heroku and Create a New App.

<img src="assets/readme_images/heroku_deployment_1.png" height="120px"> 

2. Give the App a name, it must be unique, and select a region. 

<img src="assets/readme_images/heroku_deployment_2.png" height="180px"> 

3. Click on 'Create App'. This will take you to a page where you can deploy your project. 

4. Next, click on the 'Resources' tab and search for 'Heroku Postgres' in the Add-ons section to add the Heroku Postgres database to the project. 

5. Click on the 'Settings' tab at the top of the page. The following steps must be completed before deployment.

<img src="assets/readme_images/heroku_deployment_3.png" height="180px"> 

6. Scroll down to Config Vars (also known as Environment Variables) and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py file within the same directory as the manage.py file. 

The env.py files is where the projects secret environment variables are stored. This file is then added to a gitnore file so it isn't stored publicly within the projects repository.  

7. Next, the secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.

8. Within the settings.py file you need to import os, import dj_database_url and then write an if statement to import the env.py file in production to avoid an error. 

9. Then, we need to replace the current insecure secret key with **os.environ.get('SECRET_KEY')**, that we set within the env.py file. 

10. Once the secret key is replaced, scroll down to DATABASES to connect to the Postgres database. Comment out the current code and add the following python dictionary:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

11. The next step is to connect the project to Cloudinary, which is where the media files will be stored. Log into Cloudinary and copy the API environment variable. This needs to be added to the Config Vars on Heroku and to the projects env.py file, removing the 'CLOUDINARY_URL = ' from the beginning of the copied API link. 

12. Then on Heroku add to the Config Vars, DISABLE_COLLECTSTATIC = 1, as a temporary measure to enable deployment without any static files, this will be removed when it is time to deploy the full project.


13. Back onto GitPod, the cloudinary libraries installed now need to be added to the list of installed apps within the settings.py file - 'cloudinary_storage' and 'cloudinary'

14. Next we need to tell Django to use Cloudinary to store our media and static files. Toward the end of our settings.py  file we can add:

- STATIC_URL = '/static/'
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

15. Then we need to tell Django where the templates will be stored. At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': []. 

16. Next, create the three above directories, media, static and templates, on the top level with the manage.py file. 

17. Now add our Heroku host name into allowed hosts in our settings.py file, APP_NAME.herokuapp.com, and then also add 'localhost' so the app can also run locally.

18. Finally, to complete the first deployment set up of the skeleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following:
web: gunicorn foody_family.wsgi
Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.


19. Now, go to the 'Deploy' section on Heroku. Find the 'Deployment Method' section and choose GitHub. Then, connected to the relevant GitHub Repository by searching the repository name and clicking 'Connect'.

<img src="assets/readme_images/heroku_deployment_6.png" height="120px"> 

<img src="assets/readme_images/heroku_deployment_6a.png" width="800px"> 

20. Scroll down to the Automatic and Manual Deploys sections. I then clicked 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed my code. 

<img src="assets/readme_images/heroku_deployment_7.png" height="180px"> 

21. Once the project is finished deploying, click 'view' to see the newly deployed project. 

22. Before deploying the final draft of your project you must: 
- Remove staticcollect=1 from congifvars within Heroku 
- Ensure DEBUG is set to false in settings.py file or:
    - Set DEBUG to development with: *development = os.environ.get('DEVELOPMENT', False)* above it.

23. To deploy re-do steps 19 - 21, minus reconnecting your GitHub account as it should still be connected to your App. 

# Credit
## Content 

I used the Code Institutes Boutique Ado Follow Along project to help with building this project along with the following websites:

- [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) to generate a new Django Secret Key.

- [Sculpey Blog Post](https://www.sculpey.com/create/blog/10-surprising-facts-about-polymer-clay#:~:text=Polymer%20clay%20is%20non%2Dtoxic,use%20around%20children%20and%20pets.) was used to gather information about polymer clay for the FAQ's page.

- I used [H&M](https://hmgroup.com/about-us/our-values/), [Oysho](https://www.oysho.com/gb/company.html) and [Accessorize](https://www.accessorize.com/uk/our-brand.html) to see how they shared their Policies and Frequently Asked Questions with their customers for content ideas.

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