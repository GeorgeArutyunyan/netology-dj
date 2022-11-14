from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']



class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['stock', 'product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['adress', 'products']

    def create(self, validated_data):

        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for item in positions:
            item['stock'] = stock
            StockProduct.objects.create(**item)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for item in positions:
            item['stock'] = stock
            StockProduct.ojbects.update_or_create(**item)
        return stock
