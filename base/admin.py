from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress, Category
# Register your models here

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)
