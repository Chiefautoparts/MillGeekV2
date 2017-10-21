# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def logPage(request):
	return render(request, 'log_reg/login.html')

def regPage(request):
	return render(request, 'log_reg/register.html')

def login(request):
	print '***login***' * 100
	status = User.objects.loginUser(request.POST)

	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
			return redirect('log_reg:logPage')
	else:
		user = User.objects.get(id=results['user'])
		request.session['id'] = user.id
	return redirect('log_reg:userLogged')

def register(request):
	print '***register***' * 1000
	status = User.objects.authUser(request.POST)

	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
			return redirect('log_reg:regPage')
	else:
		user = User.objects.get(id=results['user'])
		request.session['id'] = user.id
	return redirect('log_reg:userLogged')

def userLogged(request):
	return redirect('home:index')