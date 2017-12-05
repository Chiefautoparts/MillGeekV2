from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Article, MTGFeed 


class MTGFeedAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url_', 'scraper')
	list_display_links = ('name',)

	def url_(self, instance):
		return '<a href="{url"}" target="_blank">{title}</a>'.format(url=instance.url, title=instance.url)
		url_.allow_tags = True

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'mtgfeed', 'url_',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(url=instance.url, title=instance.url)
		url_.allow_tags = True

admin.site.register(MTGFeed, MTGFeedAdmin)
admin.site.register(Article, ArticleAdmin)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'image', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)