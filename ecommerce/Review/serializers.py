from rest_framework import serializers
from ecommerce.models import Review
from django.contrib.auth.hashers import make_password

# convert to json

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__' # all field