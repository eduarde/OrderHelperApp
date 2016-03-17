# [OrderHelperApp] (http://orderhelper.pythonanywhere.com)


[![Build Status](https://travis-ci.org/eduarde/OrderHelperApp.svg?branch=master)](https://travis-ci.org/eduarde/OrderHelperApp)


Small bussiness application where you can track the orders managed in your company. 

## About:

Several topics to consider:

* Currently the registration is restricted.
* Users are added by admin from Administration page.
* Each user should belong to an existing group.
* Users have permission to add, manage and view orders for their specific group.  

## Pre-requisite:

* Install python 

## Installation:

* Clone the repository
* Create a virtual environment under your project. Run `python3 -m venv myvenv` ( you can choose a different name instead of myvenv)
* Activate your virtual environment. Run `myvenv\Scripts\activate`
* Install the required dependencies:
    * `pip install django==1.X`
    * `pip install django-widget-tweaks`
    * `pip install django-datetime-widget`
    * `pip install django-pure-pagination`
* Make migrations by running: `python manage.py makemigrations orderhelper`
* Migrate by running: `python manage.py migrate orderhelper`
* Create a super user in order to have access to administration page: `python manage.py createsuperuser`
* Start server: `python manage.py runserver`

## Usage:

* Navigate to the administration page `http:\\localhost:8000\admin`
* Select Groups from AUTHENTICATION AND AUTHORIZATION section
* Add a new group and assign permissions
 
* Select Users from AUTHENTICATION AND AUTHORIZATION section
* Create users and assign the previously created group to these users
* Log in to `http:\\localhost:8000\` and test the application


 

