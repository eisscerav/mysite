# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, VisitHospital


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')


class VisitHospitalAdmin(admin.ModelAdmin):
    list_display = ('date', )


admin.site.register(User, UserAdmin)
admin.site.register(VisitHospital, VisitHospitalAdmin)