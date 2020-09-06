from ecommerce.User.viewsets import UserViewset
# from ecommerce.User.views import registration_view, TokenAuthenticationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ecommerce/user', UserViewset)
# router.register('ecommerce/user/register/', registration_view, basename='registerUser')
# router.register('ecommerce/user/login/', TokenAuthenticationView.as_view(), basename='loginUser')