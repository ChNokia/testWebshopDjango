# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from webshop import views
from webshop.models import Category, Product

urlpatterns = patterns('',
	url(r'^$', views.index),
	#url(r'^index/', views.index),
	url(r'^products/$', views.products),
	url(r'^products/([0-9]+)?/$', views.product_detail, name = 'product_detail'),
	url(r'^category/([0-9]+)?/$', views.category),
)
