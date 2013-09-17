from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_list, name='create_list'),
    url(r'^(?P<list_id>.+?)/$', views.detail, name='detail'),
    url(r'^(?P<list_id>.+?)/(?P<item_id>.+?)/update/$', views.update_item, name='update_item'),
)