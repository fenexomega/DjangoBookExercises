from django.shortcuts import render
from example_app.models import Task
from django.http import HttpResponseRedirect

def page(request,pk):
	checked_task = Task.objects.filter(id=pk)
	try:
		task = checked_task.get()
	except(Task.DoesNotExist,Task.MultipleObjectsReturned):
		return HttpResponseRedirect(reverse('index'))
	else:
		request.session['last_task'] = task.id
	return render(request,"detail_task.html",{'object':task})