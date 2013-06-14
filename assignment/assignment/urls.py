from django.conf.urls import patterns, include, url
from simpleform import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^assignment/', include('assignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^form/', include('simpleform.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^dataentryform/$', views.entryform),
	url(r'^thanks/$', views.thanks),
)
