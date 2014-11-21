# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from webshop.models import Category, Product

shop_name = 'My WebSHop'

def login(request, template_name="login.html"):
	context = {}

	context.update(csrf(request))

	if request.POST and ('username' not in request.session):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				auth.login(request, user)
				request.session['username'] = username
				return redirect('/')
			else:
				context['login_error'] = 'The password is valid, but the account has been disabled!'
		else:
			context['login_error'] = 'The user and password were incorrect.'

		return render(request, template_name, context)
	else:
	#object_list = Product.objects.all()
	#context = { 'shop_name': shop_name,
	#			'categorylist': Category.objects.all(),
	#			'object_list': object_list}

		return render(request, template_name, context)

def logout(request):
	#try:
	del request.session['username']
	auth.logout(request)
    #except KeyError:
      #  pass

	return redirect('/')

def register(request, template_name="register.html"):
	context = {}

	context.update(csrf(request))

	context['forms'] = UserCreationForm()

	if request.POST:
		new_user_form = UserCreationForm(request.POST)

		if new_user_form.is_valid():
			new_user_form.save()
			new_user = auth.authenticate(username = new_user_form.cleaned_data['username'],
										password = new_user_form.cleaned_data['password2'])
			auth.login(request, new_user)
			request.session['username'] = new_user_form.cleaned_data['username']

			return redirect('/')
		else:
			context['form'] = new_user_form

	return render(request, template_name, context)