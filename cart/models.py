# -*- coding: utf-8 -*-

from django.db import models

import datetime

from django.db import models
from django.conf import settings

from webshop.models import Product

# Create your models here.
class CartItem(models.Model):
	cart_id = models.CharField(max_length = 50)
	date_added = models.DateTimeField(auto_now_add = True)
	quantity = models.IntegerField(default = 1)
	product = models.ForeignKey('webshop.Product', unique = False)

	class Meta:
		db_table = 'cart_items'
		ordering = ['date_added']

	def total(self):
		return self.quantity * self.product.price_in_ua

	def name(self):
		return self.product.name

	def price(self):
		return self.product.price_in_ua

	def get_absolute_url(self):
		return self.product.get_absolute_url()

	def augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)

		self.save()

