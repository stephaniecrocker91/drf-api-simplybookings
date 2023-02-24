SIMPLY BOOKINGS - BACKEND API
==================================

* * *

ABOUT THE API:
------------------

* * * 


[DEPLOYED API HEROKU LINK]()

[DEPLOYED FRONTEND HEROKU LINK - LIVE SITE]()

[DEPLOYED BACKEND GITHUB REPOSITORY]()



_Simply Bookings_ is a Booking Software created in two separate projects using React, Django, Django Rest Framework.

The Front End project, consists on a stand alone React App. From within the React APP we make HTTP requests to the back-end Django REST Framework API. Instead of rendering the HTML template context object with JSON data responses. 

The Back End API was created using Django REST Framework. This back end, will return only JSON data.

This is the Back-End API project.


<img src="src/assets/amiresponsive.png" width="500px">
<img src="src/assets/home.png" width="500px">

So what do we need from our API?

JSON data, which React uses to then render the UI.
CRUD functionality! Create, Retrieve, Update or Delete things like a profile, a class, a booking, etc. This is through the HTTP requests.
Receive responses such as 2xx OK, 4xx ERROR, 5xx SERVER ERROR.

<img src="assets/crudtable.png" width="500px">


* * *

## DJANGO REST FRAMEWORK

* * *

I decided to use Django REST Framework as I can eaisly make use of its serializers, APIVIew & generics, permissions and authentications. It cans erve both mobile and web apps.



* * * 


## DATABASE:

* * *
# PROFILE APP & MODELS:

We have made use of the standard Django user Model and referenced it in our models.

Profile Model Table:

<img src="assets/profiletable.png" width="500px">


USING DJANGO SIGNALS:
Every time a profile is created, a User is created. 

* * *

## VIEWS:

* * *
# PROFILE APP:

What functionality to we want?
* List all profiles
* Option to view data in JSON 
* 

Profile List Views:
* get method: creates profile serializer instance, and response data returned from our serializer displaying Profile.objects.all()


* * *

## SERIALIZERS:

* * *

Will handle validation of our data, and handle all the conversions between our data types. 

# PROFILE SERIALIZER CLASS:

* Owner => ReadOnlyField
By default the owner field will always returm the users ID number.
For readibility, we override this by retrieving the users username instead.

owner= serializers.ReadOnlyField(
    source= 'owner.username
)


* Meta class model=Profile


* * *


## TESTING:

* * *

I extensively tested manually to ensure that the API was working as intended for my projects purpose. For example...

* Manually verified each url path created to confirm they work and open without error.
* From my api, when searching for a post/profile that exist (using our posts/id or profile/id), the data is retrieved. 
*  When attempting to search for a post/profile that does not... "detail: not found." and we get a 404 not found.
* Verified that the CRUD functionality is available in each app: User, Post, Profile, Comments, Followers, Likes, Bookmarks.
* Creating a new item and checking new item URL path.
* Checked that editing a post works.
* Deleting the item works.
* Ensured search feature returns results.
* When logging into my superuser  administrator in my back-end deployed verison of the api: I can confirm all data entered from the front end is displaying!

* * *

## PEP8 testing:

* * *




 * * *


## TECHNOLOGIES USED:

* * *

### MAIN LANGUAGE:

* * *

PYTHON

* * *

### Frameworks, Libraries, Programs:

* * * 

* Django
* Django RestFramework
* Cloudinary
* Heroku
* Pillow
* Django Rest Auth
* PostgreSQL

* * *


## BUGS, ISSUES & FIXES:

* * *

* Initially intalled django 4.1
pip3 install 'django<4'

Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4


