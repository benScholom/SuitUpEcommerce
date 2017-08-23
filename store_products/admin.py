from django.contrib import admin

# Register your models here.
from .models import Product, Order

admin.site.register(Product)
#admin.site.register(Customer)
admin.site.register(Order)
