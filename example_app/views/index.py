# -*- coding: utf-8 -*-
from django.shortcuts import render
from example_app.models import Project

"""
	View for index page
"""

def page(request):
	all_projects = Project.objects.all()
	return render(request, 'index.html',{'action':'Display all projects','all_projects':all_projects })


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip