# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
#from scrapy_djangoitem import DjangoItem 
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class MTGFeed(models.Model):
	name =models.CharField(max_length=200)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=200)
	mtgfeed = models.ForeignKey(MTGFeed)
	description = models.TextField(blank=True)
	url = models.URLField()
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.title

class ArticleItem(DjangoItem):
	django_model = Article

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, MTGFeed):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()

	if isinstance(instance, Article):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_post')
	body = models.TextField()
	image = models.ImageField(upload_to='static/img/', blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home:post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])