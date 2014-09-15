#  encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
	user_auth 		= models.OneToOneField(User,primary_key=True)
	phone 			= models.CharField(max_length=20,verbose_name="Phone")
	born_date 		= models.DateField(verbose_name="Born date", null=True,blank=True)
	last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True,blank=True,default=None)
	years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
	date_created 	= models.DateField(verbose_name="Date of Birthday",default=datetime.now())
	def __unicode__(self):
		return self.user_auth.last_name
	
class Project(models.Model):
	title 			= models.CharField(max_length=100, verbose_name="Title")
	description 	= models.CharField(max_length=1000, verbose_name="Description")
	client_name 	= models.CharField(max_length=1000, verbose_name="Client name")
	def __unicode__(self):
		return self.title

class Supervisor(UserProfile):
	specialisation  = models.CharField(max_length=50,verbose_name="Specialisation")
	

class Developer(UserProfile):
	supervisor 		= models.ForeignKey(Supervisor,verbose_name="Supervisor")

class Task(models.Model):
	title 			= models.CharField(max_length=100,verbose_name="Title")
	description 	= models.CharField(max_length=1000,verbose_name="Description")
	time_lapsed 	= models.IntegerField(verbose_name="Elapsed time",null=True,default=None,blank=True)
	importance  	= models.ForeignKey(Project,verbose_name="Project",null=True,default=None,blank=True)
	developers		= models.ManyToManyField(Developer, through="DeveloperWorkTask")
	def __unicode__(self):
		return self.title

class DeveloperWorkTask(models.Model):
	developer = models.ForeignKey(Developer)
	task = models.ForeignKey(Task)
	time_lapsed_dev = models.IntegerField(verbose_name="Time Elapsed",null=True,default=None,blank=True)

