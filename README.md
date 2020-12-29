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


- Wireframe made with Balsamic

#### Color scheme
![Colors-used](https://github.com/2tracks/shop-chichi-ms-4/blob/master/misc/colors.png?raw=true)
- Color example made with Adobe XD

## Features

- Shop
- Search by category
- Sort by price, rating, 
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

### Exiting Features

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
- Login as Admin from the Website

## Issues
While working in Gitpod is good it has also a downside, the internet connection 
is not very good where I live. As I performed a git push my Internet connection
got lost and I ended up with the message Master diverged. I could not push up to Github anymore.
I started to search online but there were so many different advices that I diceded to read
the Git docs. I checked the log files for differences - there was only one push.
I could pull the Github repo or do a hard reset but because I've never done it before and I didn't want to lose the histoty
I decided to start a know workspace, installed the requirements.txt, created a new superuser and loaded in the data.
If that wasn't my Milestone Project I probably would have downloaded a .zip from the Repo to have it save and then pulled the repo in.

## Deployment
- Create a new Heroku app - New app - chose closest region
- install pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt
- import dj_database_url in settings.py
- database settings to Heroku url
- Migrate
- create a superuser
- pip3 install gunicorn
- pip3 freeze > requirements.txt
- create Procfile
- heroku login -i
- heroku config:set Disable_COLLECTSTATC=1
## Credits
- For the Blog [Code with Stein](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg)
- For the e-commerce shop I used the Code Institute Dublin course on Boutique Ado.
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

