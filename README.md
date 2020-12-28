# Shop ChiChi
![Frontpage](misc/landingpage.jpg)

If you like little dogs in particular Chihuahuas than Shop ChiChi is the shop for you!
This is a E-commerce Shop for Chihuahua clothes with an Event site  were you can see which activites are planned
and a Blog site to see whats poeple say.

## UX
![Colors-used](misc/colors.jpg)

- Wireframe made with Balsamic
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
- Searcg by blog category

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
Linter
- Flake 8 - I choose to ignore the 'line to long warning'
- Problems tab in the Terminal
- https://jsonformatter.org/json-pretty-print

#### Validation
- [HTML validation](https://validator.w3.org/)
- [CSS validation](https://jigsaw.w3.org/css-validator/)

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

