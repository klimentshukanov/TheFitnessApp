from django.contrib import admin

from .models import *


# Register your models here.

class ProduktAdmin(admin.ModelAdmin):
    list_display = ["productName"]
    exclude = ["user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user == request.user or request.user.is_superuser):
            return True
        return True

    def has_view_permission(self, request, obj=None):
        if obj and (obj.user == request.user or request.user.is_superuser):
            return True
        return True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["categoryName"]

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True

    def has_view_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True


class CartItemAdmin(admin.ModelAdmin):
    exclude = ["price", "user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        produkt=Produkt.objects.filter(id=request.POST.get('product')).first()
        obj.price = obj.quantity * produkt.price
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (obj.user == request.user or request.user.is_superuser):
            return True
        return True

    def has_view_permission(self, request, obj=None):
        if obj and (obj.user == request.user or request.user.is_superuser):
            return True
        return True


class OrderAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True

    def has_view_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True


class OrderItemAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True

    def has_view_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return True
        return True


admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Category, CategoryAdmin)
