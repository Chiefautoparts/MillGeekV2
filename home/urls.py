from django.conf.urls import url 
from . import views

app_name='home'
urlpatterns = [
	url(r'^$', views.PostListView.as_view(), name='home'),
	url(r'^$', views.index, name='index'),
]