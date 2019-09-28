from django.db import models
class users(models.Model):
	EmailId=models.CharField(max_length=50,primary_key=True)
	Password=models.CharField(max_length=50)
	Username=models.CharField(max_length=50)
	Gender=models.CharField(max_length=50)
	Country=models.CharField(max_length=50)

class emails(models.Model):
	EmailDate=models.DateField()
	FromEmailId=models.CharField(max_length=50)
	ToEmailId=models.CharField(max_length=50)
	Subject=models.CharField(max_length=50)
	Message=models.CharField(max_length=250)