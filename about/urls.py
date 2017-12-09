from django.conf.urls import url 
from . import views

appname = 'about'
urlpatterns = [
	url(r'^$', views.index, name='basic'),
	url(r'^geekwars$', views.usGeeks, name='usGeeks')
]