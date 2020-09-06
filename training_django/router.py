from ecommerce.User.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ecommerce/user', UserViewset)