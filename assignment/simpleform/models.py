from django.db import models

# Create your models here.
class form1(models.Model):
	First_Name = models.CharField(max_length=200)
	Last_Name = models.CharField(max_length=200)
	DOB = models.DateTimeField('DOB')
	Course = models.CharField(max_length=200)
	
	def __str__(self):
		return self.First_Name