# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from webshop.models import Category, Product

shop_name = 'My WebSHop'

def index(request, template_name="product/product_list.html"):
	object_list = Product.objects.all()
	username = request.session.get('username', None)
	context = { 'shop_name': shop_name,
				'username': username,
				'categorylist': Category.objects.all(),
				'object_list': object_list}

	return render(request, template_name, context)

def products(request, template_name="product/product_list.html"):
	object_list = Product.objects.all()
	username = request.session.get('username', None)
	context = { 'shop_name': shop_name,
				'username': username,
				'categorylist': Category.objects.all(),
				'object_list': object_list}

	return render(request, template_name, context)

def product_detail(request, product_id):
	try:
		product = Product.objects.get(pk = product_id)
		username = request.session.get('username', None)
		context = { 'shop_name': shop_name,
					'username': username,
					'categorylist': Category.objects.all(),
					'product': product}
	except Product.DoesNotExist:
		raise Http404

	return render(request, 'product/product_detail.html', context)


def category(request, category_id):
	try:
		category = Category.objects.get(pk = category_id)
	except Category.DoesNotExist:
		raise Http404

	object_list = Product.objects.filter(category_id = category_id)
	username = request.session.get('username', None)
	context = { 'shop_name': shop_name,
				'username': username,
				'categorylist': Category.objects.all(),
				'object_list': object_list}

	return render(request, 'product/product_list.html', context)
