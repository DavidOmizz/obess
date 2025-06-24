from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


admin.site.register(CustomUser)

admin.site.register(Wallet)

# ... (Your CustomUserAdmin and WalletAdmin as before) ...

# list_display = ('name', 'price', 'stock', 'is_available', 'created_at')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at', 'is_available')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

class CartItemInline(admin.TabularInline): # For displaying CartItems within the Cart admin
    model = CartItem
    extra = 0 # Don't show empty extra forms

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'total_price')
    search_fields = ('user__username',)
    inlines = [CartItemInline] # Show items directly in the cart admin page

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name','product', 'quantity', 'price_at_purchase') # Make them read-only in admin

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]
    readonly_fields = ('user', 'total_amount', 'created_at', 'updated_at') # Or specific fields you want immutable