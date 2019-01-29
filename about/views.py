from django.shortcuts import render

from django.http import HttpResponse

def about(request):
	#return HttpResponse("<a href='/rango/'> Rango says here is the About Page!</a>")
	#<a href="/rango/">Index</a>
	context_dict = {'bold': "This tutorial has been put together by Stefanos Sotiriou!"}
	return render(request, 'rango/about.html', context=context_dict)
