from django.shortcuts import render
from django.forms import ModelForm
from example_app.models import Task, Developer


class Task_Form_Create(ModelForm):
	class Meta:
		model = Task
		exclude = []


# def page(request):
# 	form = Task_Form
# 	if request.POST:
