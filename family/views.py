# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'family/index.html')


def visit_hospital(request):
    users = models.User.objects.all()
    return render(request, 'family/visit_page.html',{'users': users})


def visit_info_page(request, id):
    user = models.User.objects.get(pk=id)
    return render(request, 'family/visit_info_page.html', {'user': user})


def car(request):
    pass

