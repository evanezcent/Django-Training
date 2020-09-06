from rest_framework import serializers
from ecommerce.models import User
from django.contrib.auth.hashers import make_password

# convert to json

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__' # all field

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class LoginResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', )