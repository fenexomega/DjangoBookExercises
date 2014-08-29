# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from example_app.models import Supervisor, Developer
from django import forms

class Form_inscription(forms.Form):
	name = forms.CharField(label="Name",max_length=30)
	login = forms.CharField(label="Login",max_length=30)
	password = forms.CharField(label="Password",widget=forms.PasswordInput)
	supervisor = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())


def page(request):
	if request.POST:
		form = Form_inscription(request.POST)
		# Se o formulário foi postado, iremos pegar as informações dele
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			password_confirmation = form.cleaned_data['password_confirmation']
			if password != password_confirmation :
				return render(request,'example_app/register_developer.html', {'form':form})
			supervisor = form.cleaned_data['supervisor']
			new_developer = Developer(name=name,password=password,email='',supervisor=supervisor)
			new_developer.save()
			return HttpResponse("Developer Added")
		else:
			return render(request,'example_app/register_developer.html', {'form':form})
	else:
		form = Form_inscription()
		return render(request,'example_app/register_developer.html', {'form':form})
