from django.conf.urls import url 
from . import views

appname = 'contact'
urlpatterns = [
	url(r'^$', views.index, name='contact'),
]