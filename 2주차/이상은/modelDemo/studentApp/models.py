from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=30)
	studentId = models.CharField(max_length=20)
	age = models.IntegerField()
	phone_number = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	grade = models.FloatField()