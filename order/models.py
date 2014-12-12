from django.db import models

import datetime
import decimal

from django.db import models
from django.conf import settings

from webshop.models import Customer, Product

class Order(models.Model):
	SUBMITTED = 1
	PROCESSED = 2
	SHIPPED = 3
	CANCELLED = 4

	ORDER_STATUSES = ((SUBMITTED, 'Submitted'),
					  (PROCESSED, 'Processed'),
					  (SHIPPED, 'Shipped'),
					  (CANCELLED, 'Cancelled'),)
	date = models.DateTimeField(auto_now_add = True)
	last_updated = models.DateTimeField(auto_now = True)
	status = models.IntegerField(choices = ORDER_STATUSES,
								 default = SUBMITTED)
	ip_address = models.IPAddressField()
	user = models.ForeignKey('webshop.Customer')
	email = models.EmailField(max_length = 50)
	phone = models.CharField(max_length = 20)
	transaction_id = models.CharField(max_length = 20)

	def __unicode__(self):
		return u'Order #' + str(self.id)

	@property
	def total(self):
		total = decimal.Decimal('0.00')
		order_items = OrderItem.objects.filter(order = self)

		for item in order_items:
			total = total + item.total

		return total

class OrderItem(models.Model):
	product = models.ForeignKey('webshop.Product')
	quantity = models.IntegerField(default = 1)
	price = models.DecimalField(max_digits = 9,
								decimal_places = 2)
	order = models.ForeignKey(Order)

	def __unicode__(self):
		return self.product.name

	@property
	def name(self):
	    return self.product.name

	@property
	def total(self):
	    self.quantity * self.price

	def get_absolute_url(self):
		return self.product.get_absolute_url()
