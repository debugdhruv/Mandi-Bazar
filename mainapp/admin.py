from django.contrib import admin
from . import models

@admin.register(models.Farmers_detail)
class Farmers_detailAdmin(admin.ModelAdmin):
    list_display = ['id','full_name', 'contact_no']

@admin.register(models.Businessman_details)
class Businessman_detailAdmin(admin.ModelAdmin):
    list_display = ['id','full_name']


@admin.register(models.Product_details)
class Product_detailAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_type','subtype','farmer']


