from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_list, name='create_list'),
    url(r'^(?P<list_id>.+?)/$', views.detail, name='detail'),
    url(r'^(?P<list_id>.+?)/create/$', views.create_item, name='create_item'),
    url(r'^(?P<list_id>.+?)/close/$', views.close_item, name='close_item'),
)