from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150) 
    studentId = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)