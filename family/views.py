# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'family/index.html')


def visit_hospital(request):
    return render(request, 'family/visit_page.html')


def car(request):
    pass

