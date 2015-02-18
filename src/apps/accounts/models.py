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

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from libs.utils.abstract_models import BaseFields


GENDER = (
    (0, _('Male')),
    (1, _('Female')),
)


class Interest(models.Model):

    """User interests
    """
    name = models.CharField(_('Interest'), max_length=50)


class UserAddress(BaseFields):

    """User address records
    """
    country = models.CharField(_('Country'), max_length=255, blank=True,
                               null=True)
    city = models.CharField(_('City'), max_length=255, blank=True, null=True)
    county = models.CharField(_('County'), max_length=255, blank=True, null=True)
    address_1 = models.CharField(_('Address 1'), max_length=255, blank=True, null=True)
    address_2 = models.CharField(_('Address 2'), max_length=255, blank=True, null=True)
    phone_1 = models.IntegerField(_('Phone number'), null=True, blank=True)
    phone_2 = models.IntegerField(_('Mobile number'), null=True, blank=True)
    website = models.URLField(_('Website'), null=True, blank=True)


class UserProfile(BaseFields):

    """User profile
    """

    user = models.OneToOneField(User, related_name='profile')
    firstname = models.CharField(_('Name'), max_length=50, blank=True)
    lastname = models.CharField(_('Last name'), max_length=200, blank=True)
    gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDER,
                                              blank=True)
    birthdate = models.DateField(_('Birth date'), blank=True, null=True,
                                 help_text='dd/mm/yyyy')
    address = models.ForeignKey(UserAddress, blank=True, null=True)
    interests = models.ManyToManyField(Interest, blank=True, null=True)

    def get_age(self):

        """
        Get the current user age.
        """

        if self.birthdate:
            diff = datetime.date.today() - self.birthdate
            years = diff.days / 365
            return years
        else:
            return '??'

    class Meta:
        ordering = ('pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)
