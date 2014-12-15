# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	url(r'^register_order/$', views.register_order, name = 'register_order'),
	url(r'^show_orders/$', views.show_orders, name = 'show_orders'),
	url(r'^order_detail/([0-9]+)?/$', views.order_detail, name = 'order_detail'),
	#url(r'^logout/$', views.logout),
	#url(r'^register/$', views.register),
)
