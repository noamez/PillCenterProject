from django.contrib import admin
from .models import Inventory, Medicine, Products, Vending_machines, Order_status, Orders

admin.site.register(Inventory)
admin.site.register(Medicine)
admin.site.register(Products)
admin.site.register(Vending_machines)
admin.site.register(Order_status)
admin.site.register(Orders)


# Register your models here.
