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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import UserProfile


class AccountInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = _('User profiles')


class UserAdmin(UserAdmin):

    """
    Administration of the users and user profiles
    """
    inlines = (AccountInline, )

    def has_delete_permission(self, request, obj=None):

        """
        Allow the superusers to delete users, but don't allow any other type
        of administrator
        """
        if request.user.is_superuser:
            return True
        else:
            return False

    def get_actions(self, request):

        """
        There are some situations where the has_delete_permission function
        won't remove the delete action from the menu. This function will do.
        """
        actions = super(UserAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

admin.site.unregister(User)  # Remove standard user admin
admin.site.register(User, UserAdmin)
