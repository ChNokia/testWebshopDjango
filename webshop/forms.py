# -*- coding: utf-8 -*-

from django import forms

from webshop.models import Category, Product

class ProductAddCartForm(forms.Form):
	quantity = forms.IntegerField(
								widget = forms.TextInput(
										attrs = {
											'size': '2',
											'value' : '1',
											'class' : 'quantity'
											}
										),
										error_messages = {
										'invalid' : 'Please enter a valid quantity'},
										min_value = 1
								)
	#product_slug = forms.CharField(widget = forms.HiddenInput())
	#product_id = forms.IntegerField(widget = forms.HiddenInput())

	def __init__(self, request = None, *args, **kwargs):
		self.request = request

		super(ProductAddCartForm, self).__init__(*args, **kwargs)

	def clean(self):
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError('Cookies must be enabled.')

		return self.cleaned_data
