# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect

from myShop import settings
from webshop.models import (
							Category,
							Customer,
							Product
							)

class ProfileForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].help_text = None
		self.fields['password2'].help_text = None

	class Meta:
		model = User
		#exclude = ('discount')
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		if not commit:
			raise NotImplementedError("Can't create User and UserProfile without database save")

		user = super(UserCreationForm, self).save(commit=False)

		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()

		user_customer = Customer(user=user)
		user_customer.save()

		return user, user_customer

def login(request, template_name="login.html"):
	context = { 'shop_name': settings.WEB_SITE_NAME,
				'categorylist': Category.objects.all()}

	context.update(csrf(request))

	if request.POST and ('username' not in request.session):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username,
								password = password)

		if user is not None:
			if user.is_active:
				auth.login(request, user)
				request.session['username'] = username

				return redirect('/')
			
			context['login_error'] = 'The password is valid, but the account has been disabled!'
		else:
			context['login_error'] = 'The user and password were incorrect.'

	return render(request, template_name, context)

def logout(request):
	#try:
	del request.session['username']
	auth.logout(request)
    #except KeyError:
      #  pass

	return redirect('/')

def register(request, template_name="register.html"):
	context = { 'shop_name': settings.WEB_SITE_NAME,
				'categorylist': Category.objects.all()}

	context.update(csrf(request))

	context['form'] = ProfileForm()

	if request.POST:
		new_user_form = ProfileForm(request.POST)

		if new_user_form.is_valid():
			new_user_form.save()

			username = new_user_form.cleaned_data['username']
			password2 = new_user_form.cleaned_data['password2']
			new_user = auth.authenticate(username = username,
										password = password2)

			auth.login(request, new_user)

			request.session['username'] = new_user_form.cleaned_data['username']

			return redirect('/')
		
		context['form'] = new_user_form

	return render(request, template_name, context)
