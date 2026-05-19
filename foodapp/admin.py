from django.contrib import admin

# Register your models here.
from .models import FoodItem, Order

admin.site.register(FoodItem)
admin.site.register(Order)