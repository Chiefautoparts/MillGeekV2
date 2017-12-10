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
	
	results = User.objects.loginUser(request.POST)
	if results['status'] is False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('log_reg:logPage')
	else:
		user = User.objects.get(id=results['user'])
		request.session['id'] = user.id
	return redirect('log_reg:UserHome')

def register(request):
	
	results = User.objects.registerUser(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
			return redirect('log_reg:regPage')
	request.session['id'] = results['user'].id
	return redirect('log_reg:logPage')
	


def UserHome(request):
	user = User.objects.get(id=request.session.get('id'))
	context = {
		'user': user
	}
	return render(request, 'log_reg/userPage.html')