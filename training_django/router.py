from rest_framework import routers

# Our Viewset
from ecommerce.User.viewsets import UserViewset
from ecommerce.Product.viewsets import ProductViewset
from ecommerce.Review.viewsets import ReviewViewset


router = routers.DefaultRouter()
router.register('ecommerce/user', UserViewset)
router.register('ecommerce/product', ProductViewset)
router.register('ecommerce/review', ReviewViewset)