from example_app.models import Supervisor
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.core.urlresolvers import reverse

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

def page(request):
	if len(request.POST) > 0 :
		form = Form_Supervisor(request.POST)
		if form.is_valid():
			form.save()
			HttpResponseRedirect(reverse('public_index'))
		else:
			return render(request,'example_app/create_supervisor',{'form':form})
	else:
		form = Form_Supervisor()
		return render(request,'example_app/create_supervisor.html',{'form':form})


class Form_Supervisor(forms.ModelForm):
	class Meta:
		model = Supervisor
		exclude = ('date_created','last_connection')
		widgets = {
			'password':forms.PasswordInput(),
		}