from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user', 'name', 'email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'digital', 'image')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'date_ordered', 'complete', 'transaction_id')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'order', 'quantity', 'date_added')


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('customer', 'order', 'address', 'state', 'city', 'zipcode', 'date_added')