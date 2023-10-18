from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


# Register your models here.

class StockProductInline(admin.TabularInline):
    model = StockProduct
    list_display = ['stock', 'product', 'quantity', 'price']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
    inlines = [StockProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

