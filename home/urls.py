from django.conf.urls import url 
from . import views

app_name='home'
urlpatterns = [
	#url(r'^$', views.PostListView.as_view(), name='home'),
	url(r'^$', views.index, name='index'),
	url(r'^postNews/$', views.post_news, name='post_news'),
	#url(r'^displayNews$', views.display_news, name='display_news'),
	url(r'^add_news$', views.add_news, name='add_news')
]