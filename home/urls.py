from django.conf.urls import url 
from . import views

app_name='home'
urlpatterns = [
	url(r'^$', views.post_list, name='index'),
]