
from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "model",
        "year",
        "price",
        "available",
    )

    list_filter = ("brand", "year", "fuel", "transmission", "available")

    search_fields = ("name", "brand", "model")

    list_editable = ("available",)
