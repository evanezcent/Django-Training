from rest_framework import viewsets
from ecommerce.models import Review
from .serializers import ReviewSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

