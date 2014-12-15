# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.contrib.auth.models import User, UserManager

from datetime import datetime, timedelta
import decimal
import random

import cart.cart_operations as cart
from cart.models import CartItem
from models import Order, OrderItem
from myShop import settings
from webshop.forms import ProductAddCartForm
from webshop.models import (
                            Category,
                            Customer,
                            Product
                            )

#CART_ID_SESSION_KEY = 'cart_id'

def create_order(request):
    """ function that takes a POST request and adds a product instance to the current customer's shopping cart """
    print('create_order!!!!')
    post_data = request.POST.copy()

    cart_items = cart.get_cart_items(request)
    order = Order()
    username = request.session['username']
    custom_user = Customer.objects.get(
                    user = User.objects.get(
                            username = request.session['username']))
    order.user = custom_user
    order.email = post_data.get('email',1)
    order.phone = post_data.get('phone',1)
    order.ip_address = request.META.get('REMOTE_ADDR')

    order.save()

    for cart_item in cart_items:
        product = OrderItem()
        product.order = order
        product.product = cart_item.product
        product.quantity = cart_item.quantity

        product.save()

    cart.empty_cart(request)

    print_order(order.id)
    
    return order

def print_order(id):
    order = Order.objects.get(id = id)
    order_items = OrderItem.objects.filter(order = order)

    for order_item in order_items:
        print('order_id = ', order_item.order.id)
        print('quantity = ', order_item.quantity)
        print('product = ', order_item.product)
#def cart_subtotal(request):
 #   cart_total = decimal.Decimal('0.00')
  #  cart_products = get_cart_items(request)

   # for cart_item in cart_products:
    #    cart_total = cart_total + cart_item.product.price_in_ua * cart_item.quantity

    #return cart_total
