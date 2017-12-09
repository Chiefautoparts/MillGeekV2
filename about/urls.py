from django.conf.urls import url 
from . import views

appname = 'about'
urlpatterns = [
	url(r'^$', views.index, name='usGeeks'),
	url(r'^$', views.basic, name='simpleGeeks')
]