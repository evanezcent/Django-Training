from rest_framework import serializers
from ecommerce.models import User
from django.contrib.auth.hashers import make_password

# convert to json

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__' # all field