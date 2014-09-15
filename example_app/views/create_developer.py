# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from example_app.models import Supervisor, Developer
from django import forms
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



class Form_Developer(forms.Form):
	name = forms.CharField(label="Name",max_length=30)
	login = forms.CharField(label="Login",max_length=30)
	password = forms.CharField(label="Password",widget=forms.PasswordInput)
	password_confirmation = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)
	supervisor = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())
	email = forms.EmailField(label='E-mail')
	def clean(self):
		cleaned_data = super(Form_Developer, self).clean()
		#Checar se os passwords são iguais
		password = self.cleaned_data.get('password',None)
		password_confirmation = self.cleaned_data.get('password_confirmation',None)
		if password and password_confirmation and password != password_confirmation:
			#mostre aviso de erro no formulário
			raise forms.ValidationError("Passwords are not identical!")
		return self.cleaned_data

@login_required
def page(request):
	all_supervisors = Supervisor.objects.all()
	form = Form_Developer()
	if request.POST:
		form = Form_Developer(request.POST)
		# Se o formulário foi postado, iremos pegar as informações dele
		if form.is_valid():
			name = form.cleaned_data['name']
			login = form.cleaned_data['login']
			supervisor = form.cleaned_data['supervisor']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user = User.objects.create_user(username=login,password=password,email=email)
			user.last_name = name
			user.is_active = True
			user.save()
			new_developer = Developer(user_auth=user,supervisor=supervisor,date_created=datetime.now())
			new_developer.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request,'example_app/create_developer.html', {'form':form})
	else:
		return render(request,'example_app/create_developer.html', {'form':form,'all_supervisors':all_supervisors})



# class Form_Developer(forms.Form):
# 	name = forms.CharField(label="Name",max_length=30)
# 	login = forms.CharField(label="Login",max_length=30)
# 	password = forms.CharField(label="Password",widget=forms.PasswordInput)
# 	password_confirmation = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)
# 	supervisor = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())
# 	def clean(self):
# 		cleaned_data = super(Form_Developer, self).clean()
# 		#Checar se os passwords são iguais
# 		password = self.cleaned_data.get('password',None)
# 		password_confirmation = self.cleaned_data.get('password_confirmation',None)
# 		if password and password_confirmation and password != password_confirmation:
# 			#mostre aviso de erro no formulário
# 			raise forms.ValidationError("Passwords are not identical!")
# 		return self.cleaned_data
# 	# class Meta:
# 	# 	model = Developer
# 	# 	fields = ('name','login','password','supervisor')
# 	# 	widgets = {
# 	# 		'password':forms.PasswordInput(),
# 	# 	}


# def page(request):
# 	all_supervisors = Supervisor.objects.all()
# 	form = Form_Developer()
# 	if request.POST:
# 		form = Form_Developer(request.POST)
# 		# Se o formulário foi postado, iremos pegar as informações dele
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
# 			login = form.cleaned_data['login']
# 			supervisor = form.cleaned_data['supervisor']
# 			password = form.cleaned_data['password']
# 			new_developer = Developer(name=name,login=login,password=password,email='daoraavida@email.com',supervisor=supervisor,date_created=datetime.now())
# 			new_developer.save()
# 			return HttpResponseRedirect(reverse('index'))
# 		else:
# 			return render(request,'example_app/create_developer.html', {'form':form})
# 	else:
# 		return render(request,'example_app/create_developer.html', {'form':form,'all_supervisors':all_supervisors})
