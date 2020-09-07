from rest_framework import viewsets
from ecommerce.models import User
from .serializers import UserSerializer
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

