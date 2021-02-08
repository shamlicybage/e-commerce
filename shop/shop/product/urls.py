from django.urls import path, include
from .views import ProductView, CategoryView
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'products', ProductView)
router.register(r'categories', CategoryView)

urlpatterns = [

    path('', include(router.urls)),


]
