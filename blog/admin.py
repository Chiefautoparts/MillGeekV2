# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']
	objects = models.Manager()
	published = PublishedManager()
admin.site.register(Post, PostAdmin)