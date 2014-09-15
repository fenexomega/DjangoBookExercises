from django.shortcuts import render
from example_app.models import Task
from django.http import HttpResponseRedirect

def page(request):
	tasks = Task.objects.all()
	last_task = 0
	if 'last_task' in request.session:
		last_task = Task.objects.get(id= request.session['last_task'])
		tasks = tasks.exclude(id=request.session['last_task'])
	return render(request,'list_task.html',{'object_list':tasks,'last_task':last_task})