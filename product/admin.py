from django.contrib import admin
from .models import ProductModel,Category, OrderStatus, ProductOrder, UserOrder

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(Category)
admin.site.register(OrderStatus)
admin.site.register(ProductOrder)
admin.site.register(UserOrder)

