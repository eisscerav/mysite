# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, VisitHospital


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'gender')
#
#
# class VisitHospitalAdmin(admin.ModelAdmin):
#     module = VisitHospital
#     list_display = ('user_name', 'date')
#
#     def user_name(self, obj):
#         return obj.user.name
#     user_name.admin_order_field = 'user' #Allows column order sorting
#     user_name.short_description = 'name' #Renames column head
#
# admin.site.register(User, UserAdmin)
# admin.site.register(VisitHospital, VisitHospitalAdmin)


class VisitHospitalInline(admin.StackedInline):
    model = VisitHospital
    extra = 1

    # def user_name(self, obj):
    #     return obj.user.name
    # user_name.admin_order_field = 'user' #Allows column order sorting
    # user_name.short_description = 'name' #Renames column head


class UserAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    list_display = ('name', 'age', 'gender')
    inlines = [VisitHospitalInline]


admin.site.register(User, UserAdmin)
