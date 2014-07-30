# - * - Coding: utf -8 - * -
from django.shortcuts import render
"""
	View for index page
"""
def page(request):
	userip = get_client_ip(request)
	my_var = "Hello World"
	years_old = 1
	array_city_capitale = ["Paris", "London", "New York"]
	texto = "Ola, esse eh o meu texto.\n Consegui converter os lines breaks para <br /> usando django! \n Viva! :D"
	return render(request,'example_app/index.html',
		{"my_var":my_var,"years_old":years_old,"array_city":array_city_capitale,"userip":userip, "texto":texto})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip