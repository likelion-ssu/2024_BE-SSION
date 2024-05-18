from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=150) # CharField => db에 문자열로 넣겠다는 의미
    phone_number = models.CharField(max_length=15)
    salary = models.IntegerField()
    email = models.CharField(max_length=30)