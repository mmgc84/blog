from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Examples:
url(r'^$', 'mysite.views.home', name='home'),
url(r'^blog/', include('blog.urls')), """

urlpatterns = patterns('',
                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
