# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50, db_index=True)
	slug = models.SlugField(max_length=50, db_index=True)
	image =models.ImageField()
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Post {}'.format(self.id)