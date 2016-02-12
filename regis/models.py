from django.db import models

# Create your models here.
class R_User(models.Model):
	zeal = models.CharField(max_length=10)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	course = models.CharField(max_length=10)
	branch = models.CharField(max_length=10)
	contact = models.CharField(max_length=10)
	college = models.CharField(max_length=200)
	year = models.CharField(max_length=200)
