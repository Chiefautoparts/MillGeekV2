from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
	return render(request, 'events/events.html')

def calendar(request):
	return render(request, 'events/calendar.html')