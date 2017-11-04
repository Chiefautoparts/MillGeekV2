# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewsFeedManager(models.Manager):
	def validPost(self, postData):
		results = {'status': True, 'errors':[]}
		if not postData['title'] or len(postData['title']) < 2:
			results['status'] = False
			results['errors'].append('Please have a title that is more than 2 characters')
		if not postData['body'] or len(postData['body']) < 2:
			results['status'] = False
			results['errors'].append('Post to the News Feed must have a description')
		if results['status'] is False:
			return results

		post = NewsFeed.objects.filter(title=postData['title'])

		if results['status']:
			post = NewsFeed.objects.create(title=postData['title'], body=postData['body'], image=postData['image'])
			post.save()
			print post.title
		return results


class NewsFeed(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	image = models.ImageField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = NewsFeedManager()