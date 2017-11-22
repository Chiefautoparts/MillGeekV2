from django.conf.urls import url
from . import views

app_name="log_reg"
urlpatterns = [
	url(r'^login/$', views.login, name="login"),
	url(r'^register/$', views.register, name="register"),
	url(r'^logPage$', views.logPage, name="logPage"),
	url(r'^regPage$', views.regPage, name="regPage"),
	url(r'^UserHome$', views.UserHome, name="UserHome"),
]