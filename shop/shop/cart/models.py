from django.db import models
import uuid
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    cart_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.total)


class CartItem(models.Model):
    cartItem_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.quantity)
