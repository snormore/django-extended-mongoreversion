#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-extended-mongoreversion',
    version='0.0.1-prealpha',
    description='An extension to the Django web framework that provides version control facilities for mongoengine document models, as well as extended features through User model integration including User permissions checks and events for a ProposeUpdate -> Accept/Reject process, among other features.',
    author='Steven Normore',
    author_email='snormore@gmail.com',
    long_description=open('README.md', 'r').read(),
    url='http://github.com/snormore/django-extended-mongoreversion/',
    packages=[
        'extended_mongoreversion',
    ],
    install_requires=[
        'django', 
        'mongoengine', 
        'nose', 
    ],
)