from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'moto.views.table', name='table'),
    url(r'^(?P<id>\d+)/$', 'moto.views.detail', name='detail'),

    url(r'^admin/', include(admin.site.urls)),
)

