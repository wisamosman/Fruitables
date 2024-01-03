from django.db import models
from django.utils import timezone
from accounts.models import Address
from fruit.models import Fruit
from django.contrib.auth.models import User
from utils.generate_code import generate_code



class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,blank=True,null=True)
    code = models.CharField(max_length=30,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code




class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, related_name='order_fruit',on_delete=models.SET_NULL,null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,blank=True,null=True)
    completed = models.BooleanField(default=False)

     # instance method
    def cart_total(self):
        total = 0
        for fruit in self.cart_detail.all():
            total += fruit.total
        return round(total,2)



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail',on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit , related_name='cart_fruit',on_delete=models.SET_NULL,null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)



