from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from example_app.models import UserProfile

def page(request):
	if request.POST:
		form = Form_connection(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user:
				login(request,user)
			else:
				return render(request, 'example_app/connection.html',{'form':form})
	form = Form_connection()
	return render(request, 'example_app/connection.html',{'form':form})

class Form_connection(forms.Form):
	username = forms.CharField(label="Login",max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)
	def clean(self):
		cleaned_data = super(Form_connection,self).clean()
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username,password=password):
			raise forms.ValidationError("Wrong Login or password")
		return self.cleaned_data