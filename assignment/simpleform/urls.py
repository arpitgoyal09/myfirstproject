from django.conf.urls import patterns, url

from simpleform import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	#url(r'^dataentryform/$', views.entryform),
)