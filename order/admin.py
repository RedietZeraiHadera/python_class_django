from django.contrib import admin

# Register your models here.
from .models import Order

class Order_admin(admin.ModelAdmin):
    list_display = ("quantity", "price")

admin.site.register(Order,Order_admin)

#  name = models.CharField(max_length=32)
#     # customer_id = models.IntegerField()
#     quantity= models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
    
#     basket = models.OneToOneField(Cart, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     shipments = models.ManyToManyField(Delivery)