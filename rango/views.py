from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from django import forms
from django.contrib.auth.models import User
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	#return HttpResponse("<br/> <a href='/rango/about/'> Rango says hey there partner! </a>")
	#return ("<br/> <a href='/rango/about/'>About</a>")
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	#context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	category_list = Category.objects.order_by('-likes')[:5]

	context_dict = {'categories': category_list}

	page_list = Page.objects.order_by('-views')[:5]
	context_dict['pages'] = page_list

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context_dict)

def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)

	return render(request, 'rango/add_category.html',{'form':form})

def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if category:
				page = form.save(commit=False)
				page.category = category
				page.views = 0
				page.save()
				return show_category(request, category_name_slug)
			else:
				print(form.errors)

	context_dict = {'form':form, 'category':category}

	return render(request, 'rango/add_page.html', context_dict)

def about(request):
	#return HttpResponse("<a href='/rango/'> Rango says here is the About Page!</a>")
	#<a href="/rango/">Index</a>
	context_dict = {'bold': "This tutorial has been put together by Stefanos Sotiriou!"}
	return render(request, 'rango/about.html', context=context_dict)

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				profile.save()
				registered = True

			else:
				print(user_form.errors, profile_form.errors)

	else:
		user_form=UserForm()
		profile_form = UserProfileForm()

	return render(request,
					'rango/register.html',
					{'user_form':user_form,
					'profile_form':profile_form,
					'registerd': registered})

def user_login(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'rango/login.html', {})
