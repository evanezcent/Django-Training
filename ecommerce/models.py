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
    img_url = models.FileField(upload_to='user', null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    stock = models.IntegerField()
    size = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=30, null=True)
    img_url = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    rating = models.FloatField()
    comment = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    total = models.IntegerField(default=None)

class Category(models.Model):
    name = models.CharField(max_length=50)

class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, related_name='category_related')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='product_related')

