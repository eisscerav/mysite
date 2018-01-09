# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'family/index.html')


def visit_hospital(request):
    users = models.User.objects.all()
    return render(request, 'family/visit_user_page.html', {'users': users})


def visit_info_page(request, visitor_id):
    user = models.User.objects.get(pk=visitor_id)
    return render(request, 'family/visit_info_page.html', {'user': user})


def visit_edit_page(request, visitor_id):
    if visitor_id == '0':
        return render(request, 'family/visit_edit_page.html')
    user = models.User.objects.get(pk=visitor_id)
    return render(request, 'family/visit_edit_page.html', {'user': user})


def visit_edit_action(request):
    pass


def car(request):
    pass

