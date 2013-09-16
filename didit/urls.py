from django.conf.urls import patterns, url, include
from app import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'didit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(urls))
)
