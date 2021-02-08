from rest_framework import serializers

from product.models import Product
from product.models import Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        categories = serializers.SlugRelatedField(queryset=Product.objects.all(),
                                                  many=True,
                                                  slug_field='category_id')
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'
