# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

#from cart import views
#from order import views
from webshop import views
from webshop.models import Category, Product

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	#url(r'^$', cache_page(views.index, 60 * 60 * 3), name = 'index'),
	url(r'^products/$', views.products, name = 'products'),
	url(r'^cart/$', include('cart.urls')),
	url(r'^order/', include('order.urls')),
	url(r'^products/([0-9]+)?/$', views.product_detail, name = 'product_detail'),
	url(r'^category/([0-9]+)?/$', views.category, name = 'category'),
)
