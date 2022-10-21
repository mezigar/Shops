from django.contrib import admin

from .models import City, Street, Shop

@admin.register(City, Street, Shop)
class ShopAdmin(admin.ModelAdmin):
    pass
