from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^visit_hospital/$', views.visit_hospital, name='visitHospital'),
    url('^car/$', views.car, name='car')
]