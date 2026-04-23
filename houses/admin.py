from django.contrib import admin
from houses.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "active", "bedrooms"]
    list_filter = ["active"]
