"""
Main trigger for the settings. This file determines what subset of the settings
should be loaded.
"""

#from state_control import *
from .defaults import *
import os

DEBUG = bool(int(os.getenv('DJANGO_IS_DEBUG', True)))
TEMPLATE_DEBUG = DEBUG
__version__ = "0.2.0"
__status__ = "alpha"

# Only valid if DEBUG=True. Sets the staging settings.
STAGING = bool(int(os.getenv('DJANGO_IS_STAGING', False)))

if DEBUG and not STAGING:
    from .development import *
elif DEBUG and STAGING:
    from .staging import *
else:
    from .production import *
