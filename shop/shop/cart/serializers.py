from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cart, CartItem
from product.models import Product


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        user = serializers.SlugRelatedField(
            queryset=User.objects.all(),
            slug_field='username'
        )
        items = serializers.SlugRelatedField(
            queryset=Product.objects.all(),
            slug_field='product_id'
        )

        model = Cart
        categories = serializers.SlugRelatedField(queryset=Cart.objects.all(),
                                                  many=True,
                                                  slug_field='category_id')
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        cart = serializers.SlugRelatedField(
            queryset=Cart.objects.all(),
            slug_field='cart_id'
        )
        items = serializers.SlugRelatedField(
            queryset=Product.objects.all(),
            slug_field='product_id'
        )

        model = CartItem
        categories = serializers.SlugRelatedField(queryset=CartItem.objects.all(),
                                                  many=True,
                                                  slug_field='category_id')
        fields = '__all__'
