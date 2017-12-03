# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
#import feedparser
#import requests
import urllib2
from bs4 import BeautifulSoup

def post_list(request):
	quote_page = 'https://magic.wizards.com/en/rss/rss.xml?tags=Daily%20MTG&lang=en'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html5lib')
	return render(request, 'home/index.html')



# def post_list(request):
# 	docs = requests.get("https://magic.wizards.com/en/rss/rss.xml?tags=Daily%20MTG&lang=en")
# 	soup = BeautifulSoup(docs)
# 	posts = Post.published.all()
# 	mtg = feedparser.parse("https://magic.wizards.com/en/rss/rss.xml")
# 	return render(request, 'home/index.html', {'posts': posts,
# 												'mtg': mtg,
# 												'soup': soup})
def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
# def index(request):
# 	post = NewsFeed.objects.all()
# 	context = {
# 		'post': post
# 	}
# 	return render(request, 'home/index.html', context)
# #class PostListView(ListView):
#	queryset = Post.published.all()
#	conext_object_name = 'posts'
#	template_name = 'blog/post/list.html'
# def add_news(request):
# 	return render(request, 'home/news.htm

# def rss_feed(request):
# 	mtg = feedparser.parse("https://magic.wizards.com/en/rss/rss.xml")


# def magic_news(request):
# 	docs = requests.get("https://magic.wizards.com/en/rss/rss.xml?tags=Daily%20MTG&lang=en").html
# 	soup = BeautifulSoup(docs)
# 	return re