from django.shortcuts import render

def page(request):
	return render(request, 'example_app/connection.html')