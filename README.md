# print(STATEMENTS)
Print statements is a safe haven that brings artists & consumers together in harmony. It allows artists to take control of the distribution of their work, and share their passions with the general public. As well as bringing an interactive, engaging platform for the public to find pieces from their favourite artists, as well as allowing them to discover new & upcoming figures within the art world.

![Site view across devices]()

The live link for "print(STATEMENTS)" can be found [HERE](https://print-statements.herokuapp.com/)

## Table of Contents
+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Site Goal](#site-goal "Site Goal")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
+ [User Stories](#user-stories "User Stories")
  + [Admin stories](#admin-stories "Admin stories")
  + [Artist stories](#artist-stories "Artist stories")
  + [Visitor stories](#visitor-stories "Visitor stories")
+ [Design](#design "Design")
  + [Colour Scheme](#colour-scheme "Colour Scheme")
  + [Typography](#typography "Typography")
  + [Imagery](#imagery "Imagery")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## UX

### Site Purpose:
The intent of the site is to bring Artists & Consumers together. [“print(STATEMENTS)”](https://print-statements.herokuapp.com/) Is an online printing service where known & aspiring artists can submit their work. In doing so, they will also select the medium in which they would like their work to be printed, along with the number of limited edition copies they would like to order. Upon doing so, the artwork will then be displayed on the site, available to the general public for purchase. Each unique piece of artwork will be signed & numbered, and issued with a statement of authenticity, so that enthusiastic collectors can own a piece of their favourite artist.

### Site Goal:
To build a platform that allows artists to easily share their work and passions with their fans, and art loves who have yet to discover their talents. As well as to bring an engaging experience to artists and consumers alike. By having a display of artwork from a range of individuals, art-lovers will be able to easily peruse through pieces that engage them in a way that only art can.

### Audience:
For everyone with a thirst for beauty in their lives. For the experiences art collectors who know what they are looking for, as well as those just discovering the art world with fresh new eyes. The ideal user age is between 20-50 years of age.

### Communication:
With a clean, easy to follow layout, the user - both artist and consumer alike - are guided through the features of the website with an ease of navigation.

### Current User Goals:
For Artists to easily be able to supply their work to the art world and be discovered by new & old collectors. For Collectors to not only find works by the artists they admire, but to also discover new artists along the way.

### New User Goals:
To become instantly engaged with the design of the site, and feel intrigued to play along.

### Future Goals:
To make the works purchasable through the platform directly.

## User Stories
Not all stories have been implemented. Some have been left for future implementations as the site grows and expands.

### Admin stories:
#### As an admin:
- I can **submit new blog posts** so that **I can inform site visitors & artists of new events, artists, and more**.
-- Story points:
- I can **moderate blog comments** so that **the feedback provided is appropriate**.
-- Story points:
- I can **create a log in / sign up page** so that **artists and visitors can sign up to the site**.
-- Story points:
- I can **** so that ****.
-- Story points:

### Artist stories:
#### As an artist:
- I can **create a user profile** so that **I can be found & viewed on the site**.
-- Story points:
- I can **upload artwork** so that **I can share it with art enthusiasts**.
-- Story points:
- I can **select a medium, and print size** so that **I can have the work printed**.
-- Story points:
- I can **choose how many prints I would like** so that **my work is sold as a limited edition run**.
-- Story points:
- I can **set a price** so that **I can sell my work**.
-- Story points:

### Visitor stories:
#### As a visitor:
- I can **visit the blog** so that **I can see what is new**.
-- Story points:
- I can **comment on blog posts** so that **I can give my feedback**.
-- Story points:
- I can **like blog posts** so that **I can easily share my enthusiasm**.
-- Story points:
- I can **peruse the gallery** so that **I can discover new artists, and new artworks by artists I already know**.
-- Story points:
- I can **follow artists** so that **I can be updated when new work is released**.
-- Story points:
- I can **like an artists** so that **I can show my appreciation**.
-- Story points:

## Design

### Wireframes:
![Desktop wireframe]()
![Smartphone wireframe]()

### Colour Scheme:

![Colour Palette]()

### Typography:
All fonts were obtained from the Google Fonts library. I chose the following fonts for the page:
1. 
2. 
3. 
4. 

### Imagery:
All photography for the fictional "artists" was supplied by me.

## Features

### Existing Features:

#### Landing Page:
![]()

#### Navigation Bar:
![]()

#### About Page:
![]()

#### Gallery:
![]()

#### Blog:
![]()

#### Log in & Sign up:
![]()

#### Online Shop:
![]()

#### Social Links:
![]()

### Features Left to Implement
- Home page
- About Page
- Sign-up/Log-in page
- Blog Page
- Artists gallery
- Online shop

## Testing
I was unable to load the home (index.html) page using the generic views. This was resolved with trial & error, and I realised that by changing the class to a function in views.py, as well as simply rendering the page, along with removing the ```.as_view()``` from the url path resolved the issue.

The css styles were not loading into my blog page, or my blog post page. Upon reviewing this [Django tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial06/), I discovered that I needed to update my href link to ```{% static 'css/style.css' %}```. This corrected the issue instantly.

After installing ```django-allauth``` I was unable to migrate my changes. Each time I tried, I encountered an error message in the terminal that I could not decipher. I checked & rechecked each of the commands I had used then installing the package, along with adding it to the requirements file, as well as triple checking lines added in settings and urls. Eventually I reached out to Tutor Support, and they informed me that Heroku often alters the DATABASE configvar for security reasons. Upon updating the value in my env.py file, the issue was instantly rectified.

After installing **crispy-forms**, an "Invalid syntx" error was displaying in the terminal. This was fixed by providing the missing comma within the BlogPostPage class.

Django was then throwing an error, as the CSRF token had been added incorrectly to the form field.


### Validator Testing
- html files pass through the [W3C validator](https://validator.w3.org/) with no issues found.

![W3C validator message]()

- CSS files pass through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/) with no issues found.

![Jigsaw validator message]()

- JS files pass through [JSHint](https://jshint.com/) with no issues found.

![JSHint overview]()

- page has an excellent Accessibility rating in Lighthouse

![Accessibility score]()

- Python files passed through [PEP8 Online](http://pep8online.com/) with no issues found.

- Tested the site opens in Brave, Chrome & Safari without issues.
- All links open to external pages as intended.

### Unfixed Bugs

## Technologies Used
### Main Languages Used
- HTML5
- CSS3
- Javascript
- Python
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- Google Fonts - for the font families: 
- Font Awesome - to add icons to the social links in the footer element.
- GitPod - to create my html files & styling sheet before pushing the project to Github.
- GitHub - to store my repository for submission.
- Balsamiq - were used to create mockups of the project prior to starting.
- Am I Responsive? - to ensure the project looked good across all devices.
- Favicon - to provide the code & image for the icon in the tab bar.
- Adobe Photoshop - for photo editing
- Django
- Bootstrap

### Installed Packages:
- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote [(link)](https://summernote.org/)
- django-allauth [(link)](https://django-allauth.readthedocs.io/en/latest/)
- django-crispy-forms[(link)](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

## Deployment
The site was deployed to Heroku. The steps to deploy are as follows:
- Creating the requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
- a django project was created using:
```
django-admin startproject printstatements .
```
- the blog app was then created with:
```
python3 manage.py startapp blog
```
- which was then added to the settings.py file within our project directory.
- the changes were then migrated using:
```
python3 manage.py migrate
```
- navigated to [Heroku](www.heroku.com) & created a new app called print-statements.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add the following key/value pairs to the configvars:
1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key:  | value: 
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- and connected my github project repository, and then clicked on the "Deploy" button

- The live link for "print(STATEMENTS)" can be found [HERE](https://print-statements.herokuapp.com/)

## Credits

### Content
Support was provided by my fellow student & friend [Mats Simonsson](https://github.com/Pelikantapeten).

Also a huge thank you to my mentor, [Martina Terlevic](https://github.com/SephTheOverwitch).

The initial setup and deployment of this project was done by following the “I think therefore I blog” walkthrough.

In addition to this, I also used the instructions they provided in order to implement a django blog into my app, following the walkthrough once again step-by-step. This also includes some formatting for the way each blog post is displayed on the blog page. Credits have been added as comments where code was used.

With the assistance of Sean at Tutor Support, I was able to add an if statement to my blog page that signled out the most recent blog post. They were very patient with me as I tried to be coherent and explain why I was stuck.

When encountering an error message that I could not decipher, let alone solve, I reached out to Tutor support, and Ger instantly pointed me in the right direction. This is my third encounter with this person over the course of my all my projects, and each time, they have been an invaluable help. 

The following Article on ['Simple is Better Than Complex'](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html), provided some insight into how to create different types of user groups.


### Media
- All photography displayed in the gallery was created by me.

##### Landing page image:
- Green photo frame downloaded from Pexels, Photo by [Barbara Wyrowińska](https://www.pexels.com/photo/green-photo-frame-2961734/)
- Photo wall downloaded from Pexels, Photo by [Tom Balabaud](https://www.pexels.com/photo/framed-photo-lot-1579708/)
- dark green gallery wall from Pexels, Photo by [¶Project Atlas](https://www.pexels.com/photo/three-paintings-hanging-in-gallery-1674049/)
- Default blog post image, Photo from Pexels, by [cottonbro](https://www.pexels.com/photo/person-holding-white-and-black-frame-4065183/)

DATA SETS:
Sign-up - visitor:
- first name
- last name
- phone number
- email

Sign-up - artist:
- first name
- last name
- phone number
- email
- artist name
- country
- description
- street name

Art submission:
- print height
- print width
- paper selection
- piece name
- number of copies
- number of copies remaining
- file
- price
