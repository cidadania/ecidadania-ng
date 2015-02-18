Requirement files
=================

There is a multienvironment requirements file located inside the /requirements
folder.

Populating the requirements
---------------------------

To populate the requirements basically open the file related to the environment
that need the package and add it there. Usually the commons.txt is used for
dependencies that are required across all environments like django itself, or
core libraries that the project might use.

Installing requirements
-----------------------

The installation of the requirements is done the same way as with a standard
requirements file, but this time, calling the environment file.

An example of how to install the development requirements would be::

    $ pip install -r requirements/dev.txt

