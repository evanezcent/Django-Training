from rest_framework import serializers
from ecommerce.models import ProductCategory
from django.contrib.auth.hashers import make_password

# convert to json

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__' # all field