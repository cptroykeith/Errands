# Django-Todolist

[![Python application](https://github.com/cptroykeith/Errands/actions/workflows/python-app.yml/badge.svg)](https://github.com/cptroykeith/Errands/actions/workflows/python-app.yml)[![codecov](https://codecov.io/gh/cptroykeith/Errands/branch/main/graph/badge.svg?token=DTH0DWI54O)](https://codecov.io/gh/cptroykeith/Errands)
[![License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

Django-Todolist is a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.


## Explore
Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)

    pip install -r requirements.txt

Migrate:

    python manage.py migrate

And then start the server (default: http://localhost:8000)

    python manage.py runserver


Webapp is hosted on railway [Errands](https://errands-production.up.railway.app/auth/login?next=/)


[license-url]: https://github.com/rtzll/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/rtzll/django-todolist
[travis-image]: https://travis-ci.org/rtzll/django-todolist.svg?branch=master
