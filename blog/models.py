from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)    #auto_now_add=True
	author = models.ForeignKey(User, on_delete=models.CASCADE)



	def __str__(self):
		return self.title




class login(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	user_id = models.IntegerField()


	def __str__(self):
		return self.username



class ODI(models.Model):
	FirstName = models.CharField(max_length=20)
	LastName = models.CharField(max_length=20)
	matches = models.IntegerField()



	def __str__(self):
		return self.FirstName





