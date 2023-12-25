from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
# Create your models here.

FRUIT_TYPES = (
    ('Vegetables','Vegetables'),
    ('Fruits','Fruits'),
    ('Bread','Bread'),
    ('Meat','Meat'),
)


class Fruit(models.Model):
    name = models.CharField(max_length=10)
    subtitle = models.TextField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='fruit')
    type = models.CharField(max_length=20,choices=FRUIT_TYPES)
    description = models.TextField(max_length=300, default='very good production')
    user = models.ForeignKey(User,related_name='user_fruit',on_delete=models.SET_NULL,null=True,blank=True)

    
    def __str__(self):
        return self.name
    


class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    fruit = models.ForeignKey(Fruit,related_name='fruit_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=30)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_data = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='review')
    

    def __str__(self):
        return f"{self.user}"
