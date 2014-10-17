from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'moto.views.table', name='table'),

    url(r'^admin/', include(admin.site.urls)),
)

