# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.core.context_processors import csrf
from django.contrib import auth

from webshop.models import Category, Product

shop_name = 'My WebSHop'

def login(request, template_name="login.html"):
	context = {}

	context.update(csrf(request))

	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)

			return redirect('/')
		else:
			context['login_error'] = 'User don find'

			return render(request, template_name, context)
	else:
	#object_list = Product.objects.all()
	#context = { 'shop_name': shop_name,
	#			'categorylist': Category.objects.all(),
	#			'object_list': object_list}

		return render(request, template_name, context)

def logout(request, template_name="product/product_list.html"):
	object_list = Product.objects.all()
	context = { 'shop_name': shop_name,
				'categorylist': Category.objects.all(),
				'object_list': object_list}

	return render(request, template_name, context)
