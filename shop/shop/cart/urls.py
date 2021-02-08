from django.urls import path, include
from .views import CartView, CartItemView
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'cart', CartView)
router.register(r'cart-items', CartItemView)

urlpatterns = [

    path('', include(router.urls)),


]
