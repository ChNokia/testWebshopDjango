# -*- coding: utf-8 -*-

from django.contrib import auth
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import cart_operations as cart
from myShop import settings
from webshop.forms import ProductAddCartForm
from webshop.models import (
							Category,
							Customer,
							Product
							)

def show_cart(request, template_name = 'cart/cart.html'):
	cart_items = cart.get_cart_items(request)

	for cart_item in cart_items:
		print('quantity = ', cart_item.quantity)
		print('product_id = ', cart_item.product_id)

	cart_subtotal = cart.cart_subtotal(request)
	#form = ProductAddCartForm(request = request)
	#form.quantity.widget['quantity'] = 4

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))
