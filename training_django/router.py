from rest_framework import routers

# Our Viewset
from ecommerce.User.viewsets import UserViewset
from ecommerce.Product.viewsets import ProductViewset


router = routers.DefaultRouter()
router.register('ecommerce/user', UserViewset)
router.register('ecommerce/product', ProductViewset)