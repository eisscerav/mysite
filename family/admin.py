# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, VisitHospital


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')


class VisitHospitalAdmin(admin.ModelAdmin):
    module = VisitHospital
    list_display = ('user_name', 'date')

    def user_name(self, obj):
        return obj.user.name
    user_name.admin_order_field = 'user'
    user_name.short_description = 'name'

admin.site.register(User, UserAdmin)
admin.site.register(VisitHospital, VisitHospitalAdmin)