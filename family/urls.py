from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^visit_hospital/$', views.visit_hospital, name='visitHospital'),
    url('^visit_info_page/(?P<visitor_id>[0-9]+)/$', views.visit_info_page, name='visit_info_page'),
    url('^visit_edit_page/(?P<user_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.visit_edit_page, name='visit_edit_page'),
    url('^visit_edit_action/$', views.visit_edit_action, name='visit_edit_action'),
    url('^visit_delete/(?P<user_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.visit_delete, name='visit_delete'),
    url('^user_delete/(?P<user_id>[0-9]+)/$', views.user_delete, name='user_delete'),
    url('^user_search/$', views.user_search, name='user_search'),
    url('^test_page/$', views.test_page, name='test_page'),
    url('^car/$', views.car, name='car'),
]