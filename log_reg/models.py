# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
from datetime import datetime


class UserManager(models.Manager):
	def authUser(self, postData):
		status = {'valid':True, 'errors':[], 'user':None}
		if not postData['first_name'] or len(postData['first_name']) < 3:
			status['valid'] = False
			status['errors'].append('Must be more than 3 characters long')
		if not postData['last_name'] or len(postData['last_name']) < 3:
			status['valid'] = False
			status['errors'].append('Must be more than 3 characters in length')
		if not postData['username'] or len(postData['username']) < 3:
			status['valid'] = False
			status['errors'].append('Please pick a more Awesomer usernam than that. I know you can do better')
		if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			status['valid'] = False
			status['errors'].append('Fake Email. Please use valid email format')
		if not postData['dob'] or postData['dob'] < 13:
			status['valid'] = False
			status['errors'].append('You are not old enough for this. go back to playing with disney toys')
		if not postData['password'] or len(postData['password']) < 8:
			status['valid'] = False
			status['errors'].append('Password cannot be less than 8 characters')
		if postData['confPassword'] != postData['password']:
			status['valid'] = False
			status['errors'].append('Passwords Do Not Match. Dumbass')
		if status['valid'] is False:
			return status

		user = User.objects.filter(username=postData['username'])

		if user:
			status['valid'] = False
			status['errors'].append('All systems Failure. Could not register User')

		if results['status']:
			passWord = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
				first_name=postData['first_name'],
				last_name=postData['last_name'],
				username=postData['username'],
				email=postData['email'],
				dob=postData['dob'],
				password=passWord)

	def loginUser(self, postData):
		status = {'valid':True, 'errors':[], 'user':None}
		user = User.objects.filter(username=postData['username'])

		try:
			user
		except IndexError as e:
			status['valid'] = False
			status['errors'].append('Username or password is not corrent')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				status['valid'] = False
				status['errors'].append('Something has gone horrifically wrong.')
			else:
				status['user'] = user[0].id
		else:
			status['valid'] = False
		return status

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=150)
	email = models.CharField(max_length=100)
	dob = models.DateTimeField()
	password = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self):
		return self.username + self.id

