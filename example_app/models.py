from django.db import models

class UserProfile(models.Model):
	name 			= models.CharField(max_length=50, verbose_name="Name")
	login 			= models.CharField(max_length=30,verbose_name="Login")
	password 		= models.CharField(max_length=30,verbose_name="Password")
	phone 			= models.CharField(max_length=20,verbose_name="Login")
	born_date 		= models.DateField(verbose_name="Born date", null=True,blank=True)
	last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True,blank=True,default=None)
	email 			= models.EmailField(verbose_name="Email")
	years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
	date_created 	= models.DateField(verbose_name="Date of Birthday")

	
class Project(models.Model):
	title 			= models.CharField(max_length=100, verbose_name="Title")
	description 	= models.CharField(max_length=1000, verbose_name="Description")
	client_name 	= models.CharField(max_length=1000, verbose_name="Client name")

class Task(models.Model):
	title 			= models.CharField(max_length=100,verbose_name="Title")
	description 	= models.CharField(max_length=1000,verbose_name="Description")
	time_lapsed 	= models.IntegerField(verbose_name="Elapsed time",null=True,default=None,blank=True)
	importance  	= models.ForeignKey(Project,verbose_name="Project",null=True,default=None,blank=True)
	app_user		= models.ForeignKey(UserProfile,verbose_name="User")

class Supervisor(UserProfile):
	specialisation  = models.CharField(max_length=50,verbose_name="Specialisation")

class Developer(UserProfile):
	supervisor 		= models.ForeignKey(Supervisor,verbose_name="Supervisor")
