from django.contrib import admin
from store.models.category import Category
from store.models.customer import Customer
from store.models.products import Products
from store.models.Orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
