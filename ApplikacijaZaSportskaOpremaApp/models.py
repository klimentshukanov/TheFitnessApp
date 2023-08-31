import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName


class Produkt(models.Model):
    productName = models.CharField(max_length=50)
    productDesc = models.TextField(max_length=500, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.productName


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalPrice = models.IntegerField(default=0)
    date_created = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.user.username + ",  total price: " + self.totalPrice.__str__() + ", date created: " \
               + self.date_created.__str__()


class OrderItem(models.Model):
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.productName




