from django.db import models
from django.contrib.auth.models import User
import uuid
from cart.models import Cart
# Create your models here.
ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)


class UserAddress(models.Model):
    address_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr_type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=120)

    def __str__(self):
        return str(self.city)


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        UserAddress, related_name='billing_address', null=True, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(
        UserAddress, related_name='shipping_address', null=True, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=50, decimal_places=2, )

    def __str__(self):
        return str(self.status)
