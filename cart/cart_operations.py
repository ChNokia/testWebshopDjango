# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Max

from datetime import datetime, timedelta
import decimal
import random

from models import CartItem
from myShop import settings
from webshop.forms import ProductAddCartForm
from webshop.models import (
                            Category,
                            Product
                            )

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    """ get the current user's cart id, sets new one if blank;
    Note: the syntax below matches the text, but an alternative,
    clearer way of checking for a cart ID would be the following:
    
    if not CART_ID_SESSION_KEY in request.session:
    """
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate(characters):
    return characters[random.randint(0, len(characters)-1)]

def _generate_cart_id():
    """ function for generating random cart ID values """
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    cart_id = ''.join([ _generate(characters) for y in range(cart_id_length)])

    return cart_id

def get_cart_items(request):
    """ return all items from the current user's cart """
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    """ function that takes a POST request and adds a product instance to the current customer's shopping cart """
    post_data = request.POST.copy()
    # get product slug from post data, return blank if empty
    #product_slug = post_data.get('product_slug','')
    # get quantity added, return 1 if empty
    quantity = post_data.get('quantity',1)
    product_id = post_data.get('product_id', 0)
    product = get_object_or_404(Product, pk = product_id)
    # fetch the product or return a missing page error
    cart_products = get_cart_items(request)
    product_in_cart = False
    # check to see if item is already in cart
    for cart_item in cart_products:
        if cart_item.product.id == product.id:
            # update the quantity if found
            cart_item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        # create and save a new cart item
        ci = CartItem()
        ci.product = product
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.save()

def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)

    for cart_item in cart_products:
        cart_total = cart_total + cart_item.product.price_in_ua * cart_item.quantity

    return cart_total

def empty_cart(request):
    user_cart = get_cart_items(request)

    user_cart.delete()
