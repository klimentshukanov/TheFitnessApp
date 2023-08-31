from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Produkt(models.Model):
    productName = models.CharField(max_length=50)
    productDesc = models.TextField(max_length=500, default="")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.productName
