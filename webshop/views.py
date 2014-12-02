# -*- coding: utf-8 -*-

from django.http import Http404
from django.http import (
						HttpResponseRedirect,
						HttpResponse
						)

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from myShop import settings
from webshop.forms import ProductAddCartForm
from webshop.models import (
							Category,
							Product
							)

def index(request, template_name="product/product_list.html"):
	object_list = Product.objects.all()

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))#render(request, template_name, context)

def products(request):
	index(request)

def product_detail(request, product_id, template_name="product/product_list.html"):
	try:
		product = Product.objects.get(pk = product_id)
	except Product.DoesNotExist:
		raise Http404

	if request.POST:
		post_data = request.POST.copy()

		#cart.add_to_cart(request)

		url = urlresolvers.reverse('show_cart')

		return HttpResponseRedirect(url)
	
	form = ProductAddCartForm(request = request, label_suffix = ':')
	form.product_id = product_id

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))


def category(request, category_id, template_name="product/product_list.html"):
	try:
		category = Category.objects.get(pk = category_id)
	except Category.DoesNotExist:
		raise Http404

	object_list = Product.objects.filter(category_id = category_id)

	return render_to_response(template_name, locals(),
		context_instance = RequestContext(request))
