from rest_framework import serializers
from ecommerce.models import Category
from django.contrib.auth.hashers import make_password

# convert to json

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__' # all field