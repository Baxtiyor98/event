from django.contrib import admin
from .models import (DevicesService, SnacksService, Order, Quantity, Place)
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(DevicesService)
admin.site.register(SnacksService)
admin.site.register(Place)


class QuantityReview(admin.TabularInline):
    model = Quantity
    extra = 0


@admin.register(Order)
class EventAdmin(admin.ModelAdmin):
    inlines = [QuantityReview]
    model = Order
    list_display = [
        "fullname",
        "company",
        "is_active",
        "start_time",
        "finish_time",
    ]
    list_filter = ["is_active", "is_deleted", "start_time"]
    search_fields = ["fullname","company"]
