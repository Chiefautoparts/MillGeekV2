from django.conf.urls import url
from . import views

appname = 'events'

urlpatterns = [
	url(r'^$', views.index, name='event')
]