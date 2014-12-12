# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.db import models
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from myShop import settings
from order.models import Order
from webshop.models import (
							Category,
							Customer,
							Product
							)

class CheckOrderForm(ModelForm):
	class Meta:
		model = Order
		exclude = ('status', 'ip_address', 'user', 'transaction_id')

def regisrer_order(request, template_name="order/order.html"):
	context = { 'shop_name': settings.WEB_SITE_NAME,
				'categorylist': Category.objects.all()}

	context.update(csrf(request))

	context['form'] = CheckOrderForm()

	return render(request, template_name, context)

