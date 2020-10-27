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

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)

        # Query for searching
        if name is not None:
            queryset = queryset.filter(name__contains=name) | queryset.filter(code__contains=name) | queryset.filter(description__contains=name)

        return queryset

