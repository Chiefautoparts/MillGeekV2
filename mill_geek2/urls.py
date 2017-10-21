"""mill_geek2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
 	url(r'^', include('home.urls', namespace='home')),
 	url(r'^log_reg/', include('log_reg.urls', namespace='log_reg')),
 	url(r'^cart/', include('myshop.cart.urls', namespace='cart')),  
    url(r'^orders/', include('myshop.orders.urls', namespace='orders')),
    url(r'^shop/', include('myshop.shop.urls', namespace='shop')),  
]
