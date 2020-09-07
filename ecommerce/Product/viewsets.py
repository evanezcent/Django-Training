from rest_framework import viewsets
from ecommerce.models import Product
from .serializers import ProductSerializer
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

