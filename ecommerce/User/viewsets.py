from rest_framework import viewsets
from ecommerce.models import User
from .serializers import UserSerializer
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('name', None)

        if username is not None:
            queryset = queryset.filter(username=username).values()

        return queryset

