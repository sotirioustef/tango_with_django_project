from django.conf.urls import url
from django.conf.urls import include
from rango import views
from about import urls
urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.about, name='about'),
	url(r'^about/', include('about.urls')),
	#url(r'^about/$', views.about, name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),
]
