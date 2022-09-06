from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(max_length=200, null= True)

    class Meta:
        ordering = ['-user']

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200, null= True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank= True)
    image = models.ImageField(default= 'placeholder.png' )

    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, blank=True)
    date_ordered = models.DateTimeField(default=datetime.now)
    complete =  models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.customer)

    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-date_added']

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = _("ShippingAddresses")
        ordering = ['-date_added']

    def __str__(self):
        return self.address


