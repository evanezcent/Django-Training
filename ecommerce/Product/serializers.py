from rest_framework import serializers
from ecommerce.models import Product
from django.contrib.auth.hashers import make_password

# convert to json

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__' # all field