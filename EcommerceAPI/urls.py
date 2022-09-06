from django.urls import path
from .views import *



urlpatterns = [
    path('', ListCustomer.as_view(), name='listcustomer'),
    path('editcustomer/<int:pk>/', DetailCustomer.as_view(), name='detailcustomer'),

    path('products/', ListProduct.as_view(), name='listproduct'),
    path('editproduct/<str:name>/', DetailProduct.as_view(), name='detailproduct'),

    path('orders/', ListOrder.as_view(), name='listorder'),
    path('editorder/<int:pk>', DetailOrder.as_view(), name='detailorder'),

    path('orderitems/', ListOrderItem.as_view(), name='listorderitem'),

    path('shippingaddress/', ListShippingAddress.as_view(), name='listshippingaddress'),
    path('editshippingaddress/<str:address>', DetailShippingAddress.as_view(), name='detailshippindaddress'),
]
