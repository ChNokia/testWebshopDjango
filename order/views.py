# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.db import models
from django.http import Http404
from django.http import (
						HttpResponseRedirect,
						HttpResponse
						)
from django.shortcuts import (
							  get_object_or_404,
							  render,
							  redirect,
							  render_to_response
							  )
from django.template import RequestContext

from myShop import settings
import order_operations
from order.models import Order, OrderItem
from webshop.models import (
							Category,
							Customer,
							Product
							)

class CheckOrderForm(ModelForm):
	class Meta:
		model = Order
		exclude = ('status', 'ip_address', 'user', 'transaction_id')

def register_order(request, template_name="order/order.html"):
	context = { 'shop_name': settings.WEB_SITE_NAME,
				'categorylist': Category.objects.all()}

	context.update(csrf(request))

	context['form'] = CheckOrderForm()

	if request.POST:
		post_data = request.POST.copy()
		form = CheckOrderForm(request.POST)

		if form.is_valid():
			print('CheckOrderForm')
			order = order_operations.create_order(request)

			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()

			url = urlresolvers.reverse('order_detail', args=[order.id])

			return HttpResponseRedirect(url)
	return render(request, template_name, context)

def show_orders(request, template_name = 'order/show_order.html'):
	

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))

def order_detail(request, order_id, template_name = 'order/order_detail.html'):
	order = get_object_or_404(Order, pk = order_id)
	order_items = OrderItem.objects.filter(order = order)

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))
