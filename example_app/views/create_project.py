from django.shortcuts import render
from example_app.models import Project
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import forms,ModelForm
from django.core.urlresolvers import reverse

class Form_project_create(ModelForm):
	# title = forms.CharField(label='Title',max_length=30)
	# description = forms.CharField(widget= forms.Textarea(attrs={'rows':5,'cols':100,}))
	# client_name = forms.CharField(label='Client',max_length=50)
	class Meta:
		model = Project
		fields = ['title','description','client_name']
		widgets = {
			'description': forms.Textarea(attrs={'rows':5,'cols':100,})
		}


def page(request):
	form = Form_project_create(initial={'title':'Nome do Projeto'})
	if request.POST:
		form = Form_project_create(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			client_name = form.cleaned_data['client_name']
			new_project = Project(title=title,description=description,client_name=client_name)
			new_project.save()
			return HttpResponseRedirect(reverse('index'))
			return HttpResponse("Projeto adicionado")
		else:
			return render(request, 'create_project.html',{'form':form})
	else:
		return render(request, 'create_project.html',{'form':form})