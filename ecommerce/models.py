from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255, null=True)
    created_at = models.DateField()

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    stock = models.IntegerField()
    size = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=30, null=True)
    img_url = models.CharField(max_length=255, null=True)
    created_at = models.DateField()
    deleted_at = models.DateField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    rating = models.IntegerField()
    comment = models.CharField(max_length=255, null=True)
    created_at = models.DateField()

    

