from django.db import models
# Create your models here.
class Reg(models.Model):
    Firstname=models.CharField(max_length=10)
    Lastname=models.CharField(max_length=10)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
    username=models.CharField(max_length=10 ,primary_key=True)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)

