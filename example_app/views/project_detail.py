from example_app.models import Project
from django.shortcuts import render

def page(request):
	projects = Project.objects.all().get(id=pk)
	return render(request, 'index.html',{'action':'Display a project in detail','project':project })
