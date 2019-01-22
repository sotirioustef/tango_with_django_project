from django.shortcuts import render

from django.http import HttpResponse

def about(request):
	return HttpResponse("<a href='/rango/'> Rango says here is the About Page!</a>")
	#<a href="/rango/">Index</a>
