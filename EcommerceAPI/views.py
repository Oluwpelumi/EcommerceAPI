from operator import ge
from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.


class ListCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DetailCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name']
        return Product.objects.filter(name=name)
    



class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class ListOrderItem(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class DetailOrderItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class ListShippingAddress(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class DetailShippingAddress(generics.RetrieveUpdateDestroyAPIView):
    # queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    lookup_field = 'address'

    def get_queryset(self):
        address = self.kwargs['address']
        return ShippingAddress.objects.filter(address=address)