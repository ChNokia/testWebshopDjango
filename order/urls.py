# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	url(r'^$', views.regisrer_order, name = 'regisrer_order'),
	#url(r'^logout/$', views.logout),
	#url(r'^register/$', views.register),
)
