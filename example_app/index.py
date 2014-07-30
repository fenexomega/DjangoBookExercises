# - * - Coding: utf -8 - * -
from django.http import HttpResponse

def page(request):
	return  HttpResponse("Hello World!")
