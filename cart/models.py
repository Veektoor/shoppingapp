from django.db import models
from django.contrib.auth.models import User
from shop.models import Product



class OrderItem(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()

    def get_cart_items(self):
        return self.items.all()
# Create your models here.



# Cart
# |-- CartItem
# |----- product
# |----- price
# |----- quantity