from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, UserAddress
from cart.models import Cart


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        user = serializers.SlugRelatedField(
            queryset=User.objects.all(),
            slug_field='username'
        )
        cart = serializers.SlugRelatedField(
            queryset=Cart.objects.all(),
            slug_field='cart_id'
        )
        billing_address = serializers.SlugRelatedField(
            queryset=UserAddress.objects.all(),
            slug_field='address_id'
        )
        shipping_address = serializers.SlugRelatedField(
            queryset=UserAddress.objects.all(),
            slug_field='address_id'
        )
        model = Order
        categories = serializers.SlugRelatedField(queryset=Order.objects.all(),
                                                  many=True,
                                                  slug_field='category_id')
        fields = '__all__'


class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        user = serializers.SlugRelatedField(
            queryset=User.objects.all(),
            slug_field='username'
        )
        model = UserAddress
        categories = serializers.SlugRelatedField(queryset=UserAddress.objects.all(),
                                                  many=True,
                                                  slug_field='category_id')
        fields = '__all__'
