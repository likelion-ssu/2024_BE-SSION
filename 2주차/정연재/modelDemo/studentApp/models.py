from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=150)
  studentId = models.IntegerField()
  age = models.IntegerField()
  phone_number = models.CharField(max_length=15)
  email = models.CharField(max_length=30)