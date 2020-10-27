from rest_framework import viewsets
from ecommerce.models import ProductCategory
from .serializers import ProductCategorySerializer


class ProductCategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
