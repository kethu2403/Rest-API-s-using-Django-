# PROFILES REST API

REST API providing basic functionality of managing user profiles.

* Install vagrant, virtual box, ATOM(text editor)
* getting into the vagrant server
..1. vagrant up
..2. vagrant ssh
....* cd ../vagrant

* for creating a django project - django.admin.py startproject "proectname"
* for creating django app - python manage.py startapp "appname"
* for enabling app. Go to settings.py in project dir and add following in installed Apps
......* 'rest_framework', 'rest_framework.authtoken' and 'app name'

* go to server and create a virtual python env using cmd- mkvirtualenv "env name"
..* install django and djangorestframework with required versions
* below command - python manage.py runserver 0.0.0.0:8080 makes our api publicly available
