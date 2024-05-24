from django.db import models

# Create your models here.
class student(models.Model):
  name=models.CharField(max_length=20)
  studentId=models.CharField(max_length=10)
  age=models.IntegerField()
  major=models.CharField(max_length=20)
  date_of_birth=models.DateField()
  