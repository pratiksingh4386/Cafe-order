from django.contrib import admin
from.models import cuisine,Food,Order
# Register your models here.

class cuisineadmin(admin.ModelAdmin):
    list_display = ("category", "created_at")
    search_fields = ('category',)
    ordering = ('category',)


class Foodadmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available")
    search_fields = ('name',)
    list_editable = ("is_available",)
    list_filter = ("is_available",)
    ordering = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','order_details','is_ready','is_delivered')
    list_editable = ('is_ready','is_delivered')
    ordering = ('-id',)

admin.site.register(cuisine, cuisineadmin)
admin.site.register(Food, Foodadmin)
admin.site.register(Order, OrderAdmin)