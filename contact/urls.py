from django.conf.urls import url 
from . import views

appname = 'castUs'
urlpatterns = [
	url(r'^$', views.index, name='contact'),
]