####################################################
# PLEASE REMEMBER TO CHANGE THIS FILE BEFORE GOING #
# TO PRODUCTION!!                                  #
####################################################

from .defaults import *

####################################################
# Database settings (default: mysql)               #
####################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'theuser',
        'PASSWORD': 'thepassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

####################################################
# Allowed hosts and security                       #
####################################################

ALLOWED_HOSTS = ['']  # Defaults to none

SECRET_KEY = ')i$+v3#q9)rxgcr!0vaxqlgcwj^*49-&weq7z^)eopjggnz^2r'


####################################################
# Internationalization                             #
####################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'


####################################################
# Email (default: deactivated)                     #
####################################################

#EMAIL_HOST = 'localhost'
#EMAIL_PORT= 25
#EMAIL_HOST_USER= ''
#EMAIL_HOST_PASSWORD= ''
#DEFAULT_FROM_EMAIL = ''
#EMAIL_USE_TLS = True


####################################################
# Caching (default: local cache)                   #
####################################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

####################################################
# Alerts                                           #
####################################################

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS


####################################################
# Fixtures (default: none)                         #
# Use this if you want to put test data in the DB  #
# on syncdb time                                   #
####################################################

FIXTURE_DIRS = (
    (BASE_DIR + '/fixtures/'),
)
