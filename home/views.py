# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

#def post_list(request):
#	posts = Post.published.all()
#	return render(request, 'blog/post/list.html', {'posts': post})

def post_list(request):
	posts = Post.published.all()
	return render(request, 'home/index.html', {'posts': posts})
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