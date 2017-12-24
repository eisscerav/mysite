# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.
from .models import Article, models


def index(request):
    articles = Article.objects.all()
    # return render(request, 'blog/index.html')
    return render(request, 'blog/index.html', {'articles':articles})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})


def article_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/article_edit.html')
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_edit.html', {'article':article})


def article_edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    #defalut value is '0'
    article_id = request.POST.get('article_id_hidden', '0')
    #Create new blog
    if article_id == '0':
        Article.objects.create(title=title, content=content)
        articles = Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    #Edit blog
    article = Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article':article})
