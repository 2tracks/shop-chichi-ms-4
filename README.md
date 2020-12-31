# Shop ChiChi
![Frontpage](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/landingpage.png?raw=true)

If you like little dogs, Chihuahuas in particular, then our Shop ChiChi is the shop for you!
This is an E-commerce Shop for Chihuahua clothes with an Event site, where you can see which activites are planned
and a Blog site to see what people have been up to. This Project is made with Django3 - Python - Bootstrap hosted on Heroku and the static files on AWS S3 Bucket.

[You can visit the Live Demo here](https://shop-chichi-ms-4.herokuapp.com/)

## UX
### User Stories

Who             | What                      | Why
----------------|---------------------------|----------------
Shopper / User  |View a list of products   | To be able to buy a product
Shopper / User  |Search by different criterias |Find the desired product
Shopper / User  |View product details page|Containing price, description, product rating, product image and sizes
Shopper / User  |Quickly find deals, clearance and special offers|Take advantage of special deals on products
Shopper / User  |View the total of your purchases at any time|To keep track on the amount
Shopper / User  |See the Events |To join an event if wanted
Shopper / User  |See blog posts|See what other users have been up to
Shopper / User  |Visit the details page of a post|If interested read the whole blog post
Shopper / User  |Leave a comment on a particular post|Say something to other users
Shopper / User  |See posts by category|Search for a particular topic
Shopper / User  |Register for an account|To have all your details stored
Shopper / User  |Login and logout|To access your details
Shopper / User  |Receive an email confirmation after registering|To make sure it worked
Shopper / User  |Sort the available products|By best rated, best prices and by category
Shopper / User  |Search for a product by name or description - searchbar|Find a specific product
Shopper / User  |Select the size and quantity of a product when purchasing|So the user gets the right size
Shopper / User  |View items in the chart|So the user can check if it's the correct item
Shopper / User  |Adjust the quantity|So the user can order the quantity he wants
Shopper / User  |View an order confirmation after checkout|Verify that I haven't made any mistakes
Shopper / User  |Receive an email confirmation|For the users record
Manager / Admin |Add product|Must be able to add a new item to the store via form.
Manager / Admin |Edit / Update a product|The responsible person must be able to modify a record 
Manager / Admin |Delete a product|The responsible person must be able to delete an item/record.
Manager / Admin |Add an event|The responsible person must be able to add an event via django admin board. 
Manager / Admin |Edit / Update an event|The responsible person must be able to modify an event via django admin board. 
Manager / Admin |Delete an event|The responsible person must be able to delete an event via django admin board. 
Manager / Admin |Edit a comment|Must be able to modify a comment in the django admin
Manager / Admin |Delete a comment|Must be able to delete a comment in the django admin
Manager / Admin |Add blog post|Must be able to add a blog post in the django admin
Manager / Admin |Edit a blog post|Must be able to modify a blog post in the django admin
Manager / Admin |Delete a blog post|Must be able to delete a blog post in the django admin

#### Color scheme
![Colors-used](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/colors.png?raw=true)
![Colors-example](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/colorexample.png?raw=true)
- Color example made with Adobe XD
- [You can find Mockups 1 here:](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/mockup1.png?raw=true)
- [You can find Mockups 2 here:](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/mockup2.png?raw=true)
- [You can find Mockups 3 here:](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/mockup2.png?raw=true)


### Databse design
I designed the database on [dbdiagram.io](https://dbdiagram.io/home)
![Database-ShopChiChi](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/db_shopchichi.png?raw=true)
- On dbdiagram.io every tablename has to be unique, but in django every model belongs
 to on app path. I named the Blog - Category and not Category_post. I realised that you really should think about the names you give,
 this seems obvious but, it makes even more sense once you created it - the same goes for database fields :)

## Features

- E-commerce Shop - The ability to buy dog clothes
- Payment is made via Stripe the shopper can fill in a form with pre populated information and a shooping summary
 and the ability to add a different shipping address.
- You can access My Account and Chart everywere throughout the site.
- The Admin has the ability to Edit or Delte a product directly through a link on the Products page.
- The Admin can add a product with a form via My Account/ Product Management.
- Search by category or topic
- Search by new arrivals, deals, clearance and all specials
- Sort by price and rating 
- View all products by clicking on ALL PRODUCTS/All Products.
- View all clothes
- Register or Login - You can register/login with your Email addess and Username and Password, autentication is made with django allauth.
- My Profile page - With Default Delivery Information and an Order History.
- Search for different topics such as Shirts and Jumpers
- Search in the searchbar for name or description in products.
- Events - see what's planned in the shop community the events are added via Django admin pannel.
- Blog - Here you can read the different posts it has an overview site with all the posts listet with a short intro.
 From the overview page you can follow the ```Read more``` button to the details page were you can read the full post.
 Under the image you can click on the category which will take you to a page were all the posts are listet that belogs to that category.
- Blog detail page - Here you'll find a form were you can leave a comment on the post.


### Features left to implement
- Newsletter
- Review - the ability to leave a review.
- Footer - with an impressum and copyright and legal requirements
- Blog - the ability to leave comments on the comment.
- Searchbar for the whole Site with Blog and Event in a Search APP independent and addaptable.

## Technologies Used
- GitHub
- Gitpod

#### Front-End Technologies
- HTML5
- CSS
- JavaScript
- jQuery
- Font Awesome
- Bootstrap

#### Back-End Technologies
- Python 3
- Django 3
- Django-storage
- Boto 3
- Gunicorn
- Sqlight
- PostgreSQL

#### Payment
- Stripe

#### Deployment Server
- AWS S3 Bucket - for static files
- Heroku App

## Testing
I tested this site with Goggle Chrome Developer tools and in Safary as well as Firefox.
I used Lighthouse to perform a test.

![Lighthouse](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/lighthouse.png?raw=true)

#### General testing

- I used the command ```python -m flake8`` to see all problems and correct if possible.
- Flake 8 - I've chosen to ignore the 'line to long warning'
- [Json formatter](https://jsonformatter.org/json-pretty-print) I used a json formatter to check the json code.

#### Validation

- [HTML validation](https://validator.w3.org/)
- [CSS validation](https://jigsaw.w3.org/css-validator/)
- [Lavascript validation](https://jshint.com/)
- [Python Pip8 validation](http://pep8online.com/)

I tried to validate my code as good as possible with the different validaters by copy and pasting the code.

#### Test as a Admin
- Login as Admin from the Website ```click My Account - Login``` Sign in with user name and password, when logged in under My Account a link Product Management
appears which is not visible when logged in as User. 
- Click on Product Management and add a product with image, a succsess message appears. I tested the form by adding a product without image or an invalid price.
- Keep shopping button takes you back to the products page
- I searched for the same product in the searchbar and edited it by changing the price, Success message
- Finally I deleted the same product and searched for it and got the message 0 Products found for "test".
- As a superuser I can see the Edit/Delete option under the Product.
- I've logged in to the Admin panel via ```https://shop-chichi-ms-4.herokuapp.com/admin/``` and tested if all the functions are there 
- Site administration: The admin is able to CRUD a product or category the same goes for checkout/orders, blog/posts, comments and categories and Events
- The Admin is able to CRUD Users and Groups and Email 
- When I logged out I got a success message
- I can only create Events as an Superuser in the Admin panel same goes for Blog posts

#### Test as a User
- Clicked Register and filled in the form, received cornfimation email and
 have been forwarded to the ```confirm email page``` and clicked confirm connection - got redirected to Login page.
- Register as a User, type your email, username and password and submit
- I got a message to verify my email address as well as an alert that a cormimation email has been sent.
- Verify your email and you can now successfully login
- As a User you have a MY Profile Page under My Account, I filled out the form and successfully updated my account
- Adding a product to the chart, I can increase or decrease the quantity and select a size by clicking add to chart a preview of the checkout page appears
with a product image, title, quantity and size and if the total is under $40 I get a message how much I would have left to spend to get free delivery.
- On the checkout page I can increase or decrease the quantity, update the price or remove the product, success message appears.
- Following the secure checkout I have an Order Summary and a checkout form, by submitting the form I get redirected to a thank you page with
Order Info, Order Details, Delivery address, and Billing Info and a message that an order confirmation has been sent and a Success message.
I checked the database with the Admin account and the order was successfully created. I also checked Stripe and the payment was succesfully created.
- I can add multiple products to the chart and see the price updated in the navigation background
 
- I can click on the Event tap and see all the Events
- I can click on the Blog tap and see and overview of all posts, the Read more button takes me to the detail page, where I can write a comment and add it to the comment section.
- The category tap under the image takes me to all the posts by category.
- The Logo takes me back to the Frontpage



## Issue 1
Whilst working in Gitpod is good, it also has its downside, the internet connection 
is not very good where I live. As I performed a git push my Internet connection
failed and I ended up with the message Master diverged. I could not push up to Github anymore.
I started to search online, but there were so many different advices that I decided to read
the Git docs. I checked the log files for differences - there was only one push.
I could pull the Github repo or do a hard reset, but because I've never done it before and I didn't want to lose the history
I decided to start a new workspace, installed the requirements.txt, created a new superuser and loaded the data.
If that wasn't my Milestone Project I probably would have downloaded a .zip from the Repo to have it saved and then pulled the repo in.
## Issue 2
Very important - name your Github Repo with dashes instead of underscores or you will run into trouble when deploying.

## If you would like to use this Project
1. Download the project
2. You can create a virtual environment in python (venv) or you can work on Gitpod
3. Install Django, python -m pip3 install Django
4. Install the requirements.txt, pip3 install -r requirements.txt
5. create a superuser, python3 manage.py createsuperuser
6. Migrate the database, python3 manage.py migrate
7. Loaddata for the project, python3 manage.py loaddata categories
8. Loaddata for the project, python3 manage.py loaddata products

## Deployment
I assume the Project is up and running.
### On Heroku
- Create a new Heroku app
- Navigate to www.Heroku.com - Login - New app - Choose closest region to you
- The name of the app has to be unique
- Copy over the environment variables and the secret keys
- Under Resources select Heroku Postgres
- If that's ready, go back to Gitpod

### Deploying to Heroku
- On Gitpod install, ```pip3 install dj_database_url```
- ```pip3 install psycopg2-binary```
- ```pip3 freeze > requirements.txt```
- import dj_database_url in settings.py
- In settings.py set ```ALLOWED_HOSTS = ['shop-chichi-ms-4.herokuapp.com', 'localhost']```
- Migrate, ```python3 manage.py migrate```
- Create a superuser, ```python3 manage.py create superuser```
- On Gitpod install the webserver, ```pip3 install gunicorn```
- pip3 freeze > requirements.txt
- create Procfile write ```web: gunicorn shop_chichi.wsgi:application```
- heroku login -i
- heroku config:set Disable_COLLECTSTATC=
- ```heroku git:remote -a <your app name here>```
- You can push it to Heroku now ```git push heroku master```

### Deploy the static files to ASW S3 Bucket
To host your static files you have to create an account on AWS Amazon Web Services. Create an S3 Bucket and
with public access. You have to create a usergroup and add a user to it, create a folder and upload the files.
Make sure variables are set in settings .py and on Heroku. I recommend you read the docs or watch a tutorial on AWS as these
things change over time when AWS is performing an update.
```
# Bucket Config in settings.py
    AWS_STORAGE_BUCKET_NAME = 'shop-chichi-ms-4'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' ```


# On Heroku
    USE_AWS (set to True)
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
```


## Credits
- For the Blog [Code with Stein](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg)
- For the E-commerce Shop I used the Code Institute's Course on Boutique Ado.

### Content
- The content is my own.

### Media
- The Pictures of the Chihuahua clothes are my own
- The background pictures are from [Freepick.com](https://de.freepik.com) which I hold a license for, so please make sure to look up the license.
- The picture on the Landing Page is from [Mike Foster on Pixabay](www.Pixabay.com)

### Acknowledgement
- Many thanks to all the great Tutors who make free videos on Youtube :)
- Thanks to the Tutors and my Mentor on Code Institue Dublin.

## My own thoughts

I was curious about UUID and Slug, when to use which one and why, so that's a good chat about it. [UUID or SLUG Chat. ](https://djangochat.com/episodes/urls-slugs-uuids-P9CPo6pA)
I honesly never thought about it - how my Url has to look like and how this could be helpful or a potential security hole.


Free CodeCamp Security Issue Read - very interesting:

[How I Stopped a Credit Card Thief From Ripping Off 3,537 People – and Saved Our Nonprofit in the Process](https://www.freecodecamp.org/news/stopping-credit-card-fraud-and-saving-our-nonprofit/)

