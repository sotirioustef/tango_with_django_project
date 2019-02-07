from django.conf.urls import url
from django.conf.urls import include
from rango import views
from about import urls

#app_name = 'rango'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	#url(r'^about/', include('about.urls')),
	url(r'^add_category/$', views.add_category, name='add_category'),
	#url(r'^about/$', views.about, name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
		views.show_category, name='show_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),

]
