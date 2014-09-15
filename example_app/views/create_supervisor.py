from example_app.models import Supervisor
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Form_Supervisor(forms.Form):
	name = forms.CharField(label="Name")
	login = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput, label = 'Password')
	pass_confirm = forms.CharField(max_length=30,widget=forms.PasswordInput,label = 'Password Confirm')
	email = forms.EmailField(label = 'E-mail')
	specialisation = forms.CharField(label = 'Specialisation')
	def clean(self):
		cleaned_data = super(Form_Supervisor,self).clean()
		password = self.cleaned_data.get('password',None)
		pass_confirm = self.cleaned_data.get('pass_confirm',None)
		if password and pass_confirm and password != pass_confirm:
			raise forms.ValidationError("Passwords aren't indentical")
		return self.cleaned_data

@login_required
def page(request):
	if request.POST:
		form = Form_Supervisor(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			login = form.cleaned_data['login']
			password = form.cleaned_data['password']
			specialisation = form.cleaned_data['specialisation']
			email = form.cleaned_data['email']
			new_user = User.objects.create_user(username=login,password=password,email=email)
			new_user.is_active = True
			new_user.last_name = name
			new_user.save()
			new_supervisor = Supervisor(user_auth = new_user,specialisation = specialisation)
			new_supervisor.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request,'example_app/create_supervisor.html',{'form':form})
	else:
		form = Form_Supervisor()
	return render(request,'example_app/create_supervisor.html',{'form':form})



# V1

# class Form_Supervisor(forms.Form):
# 	name = forms.CharField(label="Name",max_length=200)
# 	password = forms.CharField(label="Password",widget=forms.PasswordInput)
# 	password_confirmation = forms.CharField(label="Confirm",widget=forms.PasswordInput)


# def page(request):
# 	form = Form_Supervisor()
# 	if request.POST:
# 		form = Form_Supervisor(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
# 			password = form.cleaned_data['password']
# 			password_confirmation = form.cleaned_data['password_confirmation']
# 			if password != password_confirmation:
# 				HttpResponse('Incorrect password confirmation!')
# 			new_supervisor = Supervisor(name=name,password=password,date_created=datetime.now())
# 			new_supervisor.save()
# 			return HttpResponse("Supervisor Added")
# 		else:
# 			return render(request,'example_app/create_supervisor.html',{'form':form})
# 	else:
# 		return render(request,'example_app/create_supervisor.html',{'form':form})



################## V2

# def page(request):
# 	if len(request.POST) > 0 :
# 		form = Form_Supervisor(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			HttpResponseRedirect(reverse('index'))
# 		else:
# 			return render(request,'example_app/create_supervisor',{'form':form})
# 	else:
# 		form = Form_Supervisor()
# 		return render(request,'example_app/create_supervisor.html',{'form':form})



# class Form_Supervisor(forms.ModelForm):
# 	class Meta:
# 		model = Supervisor
# 		exclude = ('date_created','last_connection')
# 		widgets = {
# 			'password':forms.PasswordInput(),
# 		}

