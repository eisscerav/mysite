from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^article/edit/(?P<article_id>[0-9]+)$', views.article_edit, name='article_edit'),
    url(r'^article/edit/action/$', views.article_edit_action, name='article_edit_action')
]
