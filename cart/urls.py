# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from cart import views

urlpatterns = patterns('',
	url(r'^$', views.show_cart, name = 'show_cart'),
	#url(r'^logout/$', views.logout),
	#url(r'^register/$', views.register),
)
