# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2015 Clione Software
# Copyright (c) 2010-2013 Cidadania S. Coop. Galega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from .defaults import *

####################################################
# Database settings (default: sqlite3)             #
####################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

####################################################
# Allowed hosts and security                       #
####################################################

ALLOWED_HOSTS = ['*']  # By default in development we allow any host

SECRET_KEY = 'v*&#e(xgw-fs1l#e%^nm-gqju(%hx@my@!9w^e08xyd(31cv90'


####################################################
# Internationalization                             #
####################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'


####################################################
# Email (default: deactivated)                     #
####################################################

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# DEFAULT_FROM_EMAIL = 'noreply@tipexchange.vanish.co.uk'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True


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

####################################################
# Extra applications. Put here extra apps that are #
# only required in development                     #
####################################################

# INSTALLED_APPS += (
#     'sampledatahelper',
# )

##########################################################
# Sample data helper, this will fill the db              #
# Please take a look to sampledatahelper docs            #
# at https://github.com/kaleidos/django-sampledatahelper #
##########################################################

# SAMPLEDATAHELPER_SEED = 21341245334214213498921347890

# SAMPLEDATAHELPER_MODELS = [
#     {
#         'model': 'feature.Feature',
#         'number': 1,
#         'fields_overwrite': [
#             ('title', 'The Vanish Gold Range'),
#             ('status', 1),
#             ('description', 'Lorem ipsum dolor sit amet, consectetur adipisicing'),
#             ('link', 'http://example.com'),
#             ('linkname', 'Buy Vanish'),
#         ]
#     },
#     {
#         'model': 'videos.Video',
#         'number': 1,
#         'fields_overwrite': [
#             ('status', 3),
#             ('provider', 0),
#             ('provider_id', 'fDa9DVuwRDc'),
#         ]
#     },
#     {'model': 'newsletter.Newsletter', 'number': 5, },
#     {'model': 'newsletter.NewsletterArticle', 'number': 5, },
# ]

#######################################################
#
# Debug!
#
#######################################################

print("""
#####################################################################\n\
                            Debug info\n\n\
 * BASE_DIR: {}\n\
 * MEDIA_DIR: {}\n\
 * STATIC_DIR: {}\n\
 * TEMPLATE_DIRS: {}\n\n\
#####################################################################\n\
""".format(BASE_DIR, MEDIA_ROOT, STATIC_ROOT, TEMPLATE_DIRS))
