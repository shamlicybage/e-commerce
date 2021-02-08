from django.contrib import admin
from .models import Order, UserAddress
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["status", "order_total"]


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["street", "city", "state", "zipcode"]
