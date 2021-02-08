from django.urls import path, include
from .views import UserAddressView, OrderView
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'orders', OrderView)
router.register(r'address', UserAddressView)

urlpatterns = [

    path('', include(router.urls)),


]
