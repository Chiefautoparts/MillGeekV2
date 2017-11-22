from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

class UserManager(models.Manager):
	def registerUser(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if not postData['first_name']:
			results['status'] = False
			results['errors'].append('You must enter your first name.')
		if not postData['last_name']:
			results['status'] = False
			results['errors'].append('Enter your last name too')
		if not postData['username']:
			results['status'] = False
			results['errors'].append('Make a username to keep your identity secret from the evil powers at large')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			results['status'] = False
			results['errors'].append('Enter a valid email')
		if not postData['age'] > 10:
			results['status'] = False
			results['errors'].append('Go back to the disney channel you child')
		if not postData['password'] or len(postData['password']) < 8:
			results['status'] = False
			results['errors'].append('Password must be greater than 8 characters')
		if postData['confirm_password'] != postData['password']:
			results['status'] = False
			results['errors'].append('passwords do not match..... idiot')
		if results['status'] is False:
			return results

		user = User.objects.filter(username=postData['username'])

		if user:
			results['status'] = False
			results['errors'].append('You done didn\'t do something correctly')

		if results['status']:
			passwerd = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
										first_name = postData['first_name'],
										last_name = postData['last_name'],
										username = postData['username'],
										email = postData['email'],
										age = postData['age'],
										password = passwerd
										)
			user.save()
			results['user'] = user
		return results

	def loginUser(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		user = User.objects.filter(username = postData['username'])

		try:
			user

		except IndexError:
			results['status'] = False
			results['errors'].append('unable to log in user')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				results['status'] = False
				results['errors'].append('Username or password is inncorrect. The FBI has been notified')
			else:
				results['user'] = uiser[0].id
		else:
			resutls['status'] = False
		return results

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100, unique=True)
	email = models.CharField(max_length=200)
	age = models.IntegerField(default=25)
	password = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = UserManager()