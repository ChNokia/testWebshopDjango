# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from loginsys import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name = 'login'),
	url(r'^logout/$', views.logout),
	url(r'^register/$', views.register),
)
