# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from . import models
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'family/index.html')


def visit_hospital(request):
    users = models.User.objects.all()
    return render(request, 'family/visit_user_page.html', {'users': users})


def visit_info_page(request, visitor_id):
    user = models.User.objects.get(pk=visitor_id)
    return render(request, 'family/visit_info_page.html', {'user': user})


def visit_edit_page(request, user_id, visit_id):
    if user_id == '0':
        # return render(request, 'family/visit_edit_page.html')
        return render(request, 'family/visit_edit_page.html', {'user': ''})
    if visit_id == '0':
        user = models.User.objects.get(pk=user_id)
        ctx = {
            'user': user,
            'visit_info': ''
        }
        return render(request, 'family/visit_edit_page.html', ctx)
    user = models.User.objects.get(pk=user_id)
    visit_info = models.VisitHospital.objects.get(pk=visit_id)
    ctx = {
        'user': user,
        'visit_info': visit_info
    }
    return render(request, 'family/visit_edit_page.html', ctx)


def visit_edit_action(request):
    user_name = request.POST.get('name')
    user_age = request.POST.get('age')
    user_gender = request.POST.get('gender')
    hospital = request.POST.get('hospital')
    date = request.POST.get('date')
    pathogenesis = request.POST.get('pathogenesis')
    user_id = request.POST.get('user_id_hidden')
    visit_id = request.POST.get('visit_id_hidden')
    if user_id == u'':
        new_user = models.User.objects.create(name=user_name, age=user_age, gender=user_gender)
        new_user.visithospital_set.create(hospital=hospital, date=date, pathogenesis=pathogenesis)
        new_user.save()
        return render(request, 'family/index.html')

    if user_id != '' and visit_id == '':
        user = models.User.objects.get(pk=user_id)
        user.visithospital_set.create(hospital=hospital, date=date, pathogenesis=pathogenesis)
        user.save()
        return render(request, 'family/index.html')

    user = models.User.objects.get(pk=user_id)
    user.name = user_name
    user.age = user_age
    user.gender = user_gender
    visit_info = models.VisitHospital.objects.get(pk=visit_id)
    visit_info.hospital = hospital
    visit_info.date = date
    visit_info.pathogenesis = pathogenesis
    user.save()
    visit_info.save()
    return render(request, 'family/index.html')


def visit_delete(request, user_id, visit_id):
    visit_info = models.VisitHospital.objects.get(pk=visit_id)
    visit_info.delete()
    return render(request, 'family/index.html')


def user_delete(request, user_id):
    user = models.User.objects.get(pk=user_id)
    user.delete()
    return render(request, 'family/index.html')


def user_search(request):
    content = request.GET['q']
    users = models.User.objects.filter(name__icontains=content)
    context = {
        'content': content,
        'users': users
    }
    return render(request, 'family/test_page.html', context)


def test_page(request):
    objs = models.TestDatabase.objects.all()
    context = {'objs': objs}
    return render(request, 'family/test_page.html', context)


def test_edit(request):
    pass


def car(request):
    pass

