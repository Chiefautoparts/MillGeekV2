# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

def post_list(request):
	
	return render(request, 'home/index.html')



												
def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
