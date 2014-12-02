# -*- coding: utf-8 -*-

from django.contrib import auth
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from myShop import settings
from webshop.forms import ProductAddCartForm
from webshop.models import (
							Category,
							Customer,
							Product
							)

def show_cart(request, template_name = 'cart/cart.html'):
	#form = ProductAddCartForm(request = request)
	#form.product_id = 1

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))
