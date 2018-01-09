from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^visit_hospital/$', views.visit_hospital, name='visitHospital'),
    url('^visit_info_page/(?P<visitor_id>[0-9]+)/$', views.visit_info_page, name='visit_info_page'),
    url('visit_edit_page/(?P<visitor_id>[0-9]+)/$', views.visit_edit_page, name='visit_edit_page'),
    url('^car/$', views.car, name='car')
]