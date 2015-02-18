Settings
========

dboilerplate contains a multienvironment set of settings. Each settings file will load depending on the environment flags.

The settings files are located in `src/<project name>/settings` and there should
be five different files:

* __init__.py
* defaults.py
* development.example
* production.py
* staging.py


__init__
--------

The init file contains the main login to select the environment settings files.

It contains two variables, called `DEBUG` and `STAGING`, and the settings work
like this:

+-----------+-------+----------------+
| Variables | Value | Load settings  |
+===========+=======+================+
| DEBUG     | True  |                |
+-----------+-------+ development.py |
| STAGING   | False |                |
+-----------+-------+----------------+
| DEBUG     | True  |                |
+-----------+-------+ staging.py     |
| STAGING   | True  |                |
+-----------+-------+----------------+
| DEBUG     | False |                |
+-----------+-------+ production.py  |
| STAGING   | False |                |
+-----------+-------+----------------+
| DEBUG     | False |                |
+-----------+-------+ production.py  |
| STAGING   | True  |                |
+-----------+-------+----------------+

The variables can be set up in the `__init__.py` file itself, or you can set
the environment variables `DJANGO_IS_DEBUG` and `DJANGO_IS_STAGING` if you're
using a user-based deployment.

To add the environment variables to you environment and assuming you're using
bash, just open your `.bashrc` file and add:
::

    export DJANGO_IS_DEBUG="True"
    export DJANGO_IS_STAGING="True"

Replace the `"True"` values with the values that you want.

defaults.py
-----------

The defaults.py file contains the core of any project, it sets up the main settings for the application, applications to be loaded, middlewares, etc.

There is nothing special to say in this file, but you will find here the
settings for allauth as well as the logging and other minor global settings.

development, production and staging
-----------------------------------

These files contain the enviroment specific settings for each one. That includes
the database connections, language settings, django toolbar, email, caching,
fixtures, secret_key, allowed hosts, etc.

All of them are prepopulated with dummy data so you know what to modify. You
can add as well any other settings that you need for your environment or rewrite the ones loaded already in defaults.

development
-----------

By default we packa a `development.example` settings file. This is done on
purpose, so the project will fail to run until you set up the development
settings and rename the file to `development.py`.
