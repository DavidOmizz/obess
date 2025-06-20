from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    withdrawal_pin = models.CharField(max_length=6)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    invitation_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallet")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet - Balance: {self.balance}"




# --- New Models for Products and Cart/Orders ---

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True) # Requires Pillow library
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name'] # Order products by name by default

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"

    @property
    def total_price(self):
        # Calculates the total price of all items in the cart
        return sum(item.total_item_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product') # A user can only have one of each product in their cart

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart.user.username}'s Cart"

    @property
    def total_item_price(self):
        return self.quantity * self.product.price

# --- Optional: Order and OrderItem models for after checkout ---
# You might want these to store historical orders and manage order statuses.

# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status_choices = [
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     ]
#     status = models.CharField(max_length=20, choices=status_choices, default='pending')
#     # You might add fields like shipping address, payment method, etc.

#     def __str__(self):
#         return f"Order #{self.id} by {self.user.username}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
#     product = models.ForeignKey(Product, on_delete=models.PROTECT) # Don't delete product if it's part of an order
#     quantity = models.PositiveIntegerField()
#     price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2) # Store price at the time of purchase

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"

#     @property
#     def total_item_price(self):
#         return self.quantity * self.price_at_purchase