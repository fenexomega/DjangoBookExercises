from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50, verbose_name="Name")
	login = models.CharField(max_length=30,verbose_name="Login")
	password = models.CharField(max_length=30,verbose_name="Password")
	phone = models.CharField(max_length=20,verbose_name="Login")
	born_date = models.DateField(verbose_name="Born date", null=True,blank=True)
	last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True,blank=True,default=None)
	email = models.EmailField(verbose_name="Email")
	years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
	date_created = models.DateField(verbose_name="Date of Birthday")

	