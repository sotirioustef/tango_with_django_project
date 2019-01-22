from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("<br/> <a href='/rango/about/'> Rango says hey there partner! </a>")
	#return ("<br/> <a href='/rango/about/'>About</a>")
