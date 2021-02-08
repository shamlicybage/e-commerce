from django.urls import path, include

from rest_framework import routers
from product import urls
from order import urls as orderUrls
from cart import urls as cartUrls


urlpatterns = [

    path('', include(urls)),
    path('', include(orderUrls)),
    path('', include(cartUrls)),
]
