django-extended-mongoreversion
==============================

An extension to the Django web framework that provides version control facilities for mongoengine document models, as well as extended features through User model integration including User permissions checks and events for a ProposeUpdate -> Accept/Reject process, among other features.

Warning
=======

This is a work in-progress, don't count on it working just yet.

Requirements
============

* Django 1.2+

        pip install Django

* MongoEngine

        pip install mongoengine

* django-mongotesting 

        pip install git+git://github.com/snormore/django-mongotesting#egg=django-mongotesting

* mongotesting requires the `nose` package

        pip install nose

* django-mongoreversion 

        pip install git+git://github.com/snormore/django-mongoreversion#egg=django-mongoreversion

Reference
==========

* http://mongoengine.org - https://github.com/hmarr/mongoengine
* http://github.com/snormore/django-mongoreversion

