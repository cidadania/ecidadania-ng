How to install
==============

Installing the boilerplate is easy, there's two possible ways to do it.

Clone the repository
--------------------

You can clone the boilerplate repository to your machine, and use it from your
machine, that will guarantee you that you always have access to the boilerplate
even if you don't have internet connection.

* Clone the repository
  ::

    $ git clone https://github.com/clione/dboilerplate3.git

* After cloning the repository to your machine you can start you project (we
  assume you already installed django either globally or in your virtual
  environment)
  ::

    $ django-admin startproject --template=/path/to/the/template <your_project_name>

Grab it from GitHub
-------------------

Downloading the boilerplate from GitHub guarantees you that you always have
the latest version, and you can do the installation automatically when you
create the project.
::
    $ django-admin startproject --template=https://github.com/clione/dboilerplate3/archive/master.zip myproject



