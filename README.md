# Shop ChiChi
![Frontpage](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/landingpage.png?raw=true)

If you like little dogs in particular Chihuahuas then Shop ChiChi is the shop for you!
This is a E-commerce Shop for Chihuahua clothes with an Event site  were you can see which activites are planed
and a Blog site to see what people say. This Project is made with Django3 - Python - Bootstrap hosted on Heroku and the static files on AWS S3 Bucket.

[You can visit the Live Demo here](https://shop-chichi-ms-4.herokuapp.com/)

## UX
### User Stories

Who             | What                      | Why
----------------|---------------------------|----------------
Shopper / User  |View a list of products   | To be able to buy a product
Shopper / User  |Search by different criterias |Find the desired product
Shopper / User  |View product details page|Containing price, description, product rating product image and sizes
Shopper / User  |Quickly find deals, clearance and special offers|Take advantage of special savings on products
Shopper / User  |View the total of the purchases at any time|To keep track on the amount
Shopper / User  |See the Events |To join en event if wanted
Shopper / User  |See blog posts|See what other Users say
Shopper / User  |Visit the details page of a post|If interested read the whole blog post
Shopper / User  |Leave a comment on a particular post|Say something to other users
Shopper / User  |See posts by category|Search for a particular topic
Shopper / User  | Register for an account|To have all your details stored
Shopper / User  |Login and logout|To access your details
Shopper / User  |Receive an email confirmation after registering|To make sure it worked
Shopper / User  |Sort the available products|By best rated, best prices and by category
Shopper / User  |Search for a product by name or description - searchbar|Find a specific product
Shopper / User  |Select the size and quantity of a product when purchasing it|So the user get the right size
Shopper / User  |View items in the chart|So the user can check if it's correct
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
- Wireframe made with Balsamic

## Features

- Shop
- Search by category or topic
- Sort by price, rating 
- View all products
- View all clothes
- Search for different topics
- Searchbar
- Events - see what's planned in the shop community
- Blog
- Blog overview
- Blog detail Page
- Add comments on the blog post 
- Search by blog category

### Features left to implement
- Newsletter
- Review - the ability to leave a review.
- Footer - with an impressum and copyright and legal requirements
- Blog - the ability to leave comments on the comment.

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
I tested this site with Goggle Chrome Developer tools and in Safary and Firefox.

#### General testing
Linter
- python -m flake8
- Flake 8 - I choose to ignore the 'line to long warning'
- Problems tab in the Terminal
- https://jsonformatter.org/json-pretty-print

#### Validation
- [HTML validation](https://validator.w3.org/)
- [CSS validation](https://jigsaw.w3.org/css-validator/)
- [Lavascript validation](https://jshint.com/)
- [Python Pip8 validation](http://pep8online.com/)

#### Test as a User
- The user cklicks the ...
- Ckick Register and fill in the form, received cornfimation email and have been forwarded to corfim email page and chlicked connection
confirm got redirected to Login page.

#### Test as a Admin
- Login as Admin from the Website ```click My Account - Login``` Sign in with user name and password, when loged in under My Account a link Product Management
appears which is not visible when loged in as user. 
- Click on Product Management and add a product with image, a succsess message appears. I tested the form by adding a product without image or a invalid price.
- Keep shooping button takes you back to the products page
- I search for the same product in the searchbar and edit it by changing the price, Success message
- Finaly I delete the same product and search for it and get the message 0 Products found for "test".
- As a superuser I can see the Edit/Delete option under the Product.
- I've loged in to the Admin panel via ```https://shop-chichi-ms-4.herokuapp.com/admin/``` and tested if all the functions are there 
- Site administration: The admin is able to CRUD a product or category the same goes for checkout/orders, blog/posts, comments and categories and Events
- The Admin is able to CRUD Users and Groups and Email 
- When logout I get a success message
- I can only create Events as an Superuser in the Admin panel same goes for Blog posts

#### Test as a User
- Register as a User type your email, username and password and submit
- I get a message to verify my email address as well as an alert that a cormimation email has been sent.
- Verify your email and you can now successfullly login
- As a User you have a MY Profile Page under My Account, I filled out the form and successfully updated my account
- Adding a product to the chart, I can increase or decrease the quantity and select a size by clicking add to chart a preview of the checkout page appears
with a product image, title, quantity and size and if i am under $40 I get a message how much I would have left to spend to get free delivery.
- On the checkout page I can increase or decrease the quantity, update the price or remove the product, success message appears.
- Following the secure checkout I have a Order Summery and a checkout form by submitting the form I get redirected to a thank you page with
Order Info, Order Details, Delivering To, and Billing Info and a message that a order confirmation has been send and a Success message.
I checked the database with the Admin account and the order was successfully created. I also checked on Stripe and the payment was succesfully created.
- I can add multiple products to the chart and see the price updated in the navigaten background
 
- I can click on the Event tap and see all the Events
- I can chlick on the Blog tap and see and overview of all the posts the Read more button take me to the detail page were I can write a comment and add it.
- The category tap under the image takes my to all the posts by category.
- The Logo take my back to the Frontpage



## Issue 1
While working in Gitpod is good it has also a downside, the internet connection 
is not very good where I live. As I performed a git push my Internet connection
got lost and I ended up with the message Master diverged. I could not push up to Github anymore.
I started to search online but there were so many different advices that I diceded to read
the Git docs. I checked the log files for differences - there was only one push.
I could pull the Github repo or do a hard reset but because I've never done it before and I didn't want to lose the history
I decided to start a know workspace, installed the requirements.txt, created a new superuser and loaded in the data.
If that wasn't my Milestone Project I probably would have downloaded a .zip from the Repo to have it save and then pulled the repo in.
## Issue 2
Very important name your Github Repo not with underscores use dashes or you will run into trouble when deploying.

## If you would like to use this Project
1. Download the project
2. You can create a virtuell environment in python (venv) or you can work on Gitpod
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
- If that's ready go back to Gitpod

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
with public access. You have to create a usergroup and add a user to it create a folder and upload the files.
Make sure to variables are set in settings .py and on Heroku. I recommend you read the docs or watch a tutorial on AWS as these
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
- Die Pictures of the Chihuahua clothes are my own
- The background pictures are from [Freepick.com](https://de.freepik.com) which I hold a license so please make sure to lookup the licens.
- The picture on the Landing Page is from [Mike Foster on Pixabay](www.Pixabay.com)

### Acknowledgement
- Many thanks to all the great Tutors who make free videos on Youtube :)
- Thanks to the Tutors and my Mentor on Code Institue Dublin.

## My own thoughts

I was curious about UUID and Slug when to use which one and why, so that's a good chat about it. [UUID or SLUG Chat. ](https://djangochat.com/episodes/urls-slugs-uuids-P9CPo6pA)
I honesly never thought about it - how my Url has to look like and how this could be helpful or a potential security whole.


Free CodeCamp Security Issue Read - very interesting:

[How I Stopped a Credit Card Thief From Ripping Off 3,537 People – and Saved Our Nonprofit in the Process](https://www.freecodecamp.org/news/stopping-credit-card-fraud-and-saving-our-nonprofit/)

