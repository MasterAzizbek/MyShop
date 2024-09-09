from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet, get_inactive_products
from django.urls import path


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', ProductCategoryViewSet)

urlpatterns = [
    path('inactive_products/', get_inactive_products)    
] + router.urls
