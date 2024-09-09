from rest_framework import serializers
from .models import ProductCategory, ProductModel


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_category = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all()
    )

    class Meta:
        model = ProductModel
        exclude = ['status']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['status']
        depth = 1