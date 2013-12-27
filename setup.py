#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-base',
    version='1.0',
    description='{{ project_name }}',
    author='example',
    author_email='example@example.com',
    url='http://www.example.com/',
    install_requires=[
        # These dependencies are from requirements/produciton.txt
        # Note: pip is still not supported.
        'bcrypt',
        'Django>=1.6',
        'django_compressor',
        'bleach',
        # Message Queue
        'celery',
        'django-celery',
        # Caching
        'python-memcached',
        # Admin
        'django-debug-toolbar',
        # Migration
        'South'
        ],
)
