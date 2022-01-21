from django.db import models

# Create your models here.
class adminlogin(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
class userlogin(models.Model):
    email = models.CharField(max_length=30,null = True)
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)    
class items(models.Model):
    image = models.ImageField(upload_to='images')
    pname = models.CharField(max_length = 30)
    price = models.CharField(max_length = 30)
    
class cart(models.Model):
    username=models.CharField(max_length = 30)
    pname = models.CharField(max_length = 30)
    price = models.IntegerField()
