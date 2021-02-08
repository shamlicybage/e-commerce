from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework.generics import ListAPIView

from django.http import HttpResponse
from django.http import Http404

from product.models import Product, Category


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
