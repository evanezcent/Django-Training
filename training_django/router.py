from rest_framework import routers

# Our Viewset
from ecommerce.User.viewsets import UserViewset
from ecommerce.Product.viewsets import ProductViewset
from ecommerce.Review.viewsets import ReviewViewset
from ecommerce.Category.viewsets import CategoryViewset
from ecommerce.ProductCategory.viewsets import ProductCategoryViewset


router = routers.DefaultRouter()
router.register('ecommerce/user', UserViewset)
router.register('ecommerce/product', ProductViewset)
router.register('ecommerce/review', ReviewViewset)
router.register('ecommerce/category', CategoryViewset)
router.register('ecommerce/product-category', ProductCategoryViewset)