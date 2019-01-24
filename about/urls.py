from django.conf.urls import url
from django.conf.urls import include
from about import views
#from rango import urls
urlpatterns = [
	url(r'^$', views.about, name='about'),
	#url(r'^index/', include('rango.urls')),
]
