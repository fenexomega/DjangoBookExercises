from django.shortcuts import render
from django.contrib.auth import logout

def page(request):
	logout(request)
	return render(request,'example_app/logout.html')