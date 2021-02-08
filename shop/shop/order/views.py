from django.shortcuts import render
from .serializers import OrderSerializer, UserAddressSerializer
# Create your views here.
from rest_framework import viewsets, permissions, status

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import UserAddress, Order


class UserAddressView(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
