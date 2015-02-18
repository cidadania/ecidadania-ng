Logging
=======

We improved a bit the logging mechanism of django to made our lifes easier.

Apart from the standard django mailer logging we added file logging that
will spit out a django.log file inside the project folder (that is: /src/projectname/django.log)

It will create a rotating file, so you will have available all the logs that you need. This logger also logs **absolutely everything** that happens in your code
so it can be properly debugged.

Configuring the logger
----------------------

By default the loger keeps three 2MB files in your installation, you can change
that in teh default.py settings file at the end of it. The parameters are:

* maxBytes
* backupCount

The first value is the amount of MB that a file can reach, in bytes. The second
is the number of files to keep, by default is three, and it should be enough,
but maybe you need more for your project.

How to log to the logfile
-------------------------

Instead of doing prints here and there you can now log to the file doing the
following:

Add this to the file where you want to log::

    import logging

    logger = logging.getLogger(__name__)

Then to log something you can use the standard python log levels (DEBUG, INFO,
ERROR, etc.)
::

    logger.error("This is a error message")
    logger.debug("This is a debug message")
    logger.info("Seems that something happened")
