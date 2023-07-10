from django.db import models
from cart.models import Cart
from customer.models import Customer
from delivery.models import Delivery

# Create your models here.
class Order(models.Model):
    # name = models.CharField(max_length=32)
    # customer_id = models.IntegerField()
    quantity= models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    cart = models.ForeignKey(Cart,null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    delivery = models.ManyToManyField(Delivery)