from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=15,null=True,blank=True)
    phones = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(max_length=15,null=True,blank=True)
    about_us = models.TextField(max_length=500)
    street = models.TextField(max_length=20)
    post_code = models.IntegerField(default=1)
    city = models.TextField(max_length=20)


    def __str__(self):
        return self.name