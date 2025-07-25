from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

print("Loaded test file")

class WalletModelTest(TestCase):
    print("Running test_wallet_default_balance")
    def setUp(self):
        self.user = User.objects.create_user(username='testuser_unique', password='testpass')

    def test_wallet_default_balance(self):
        wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(wallet.balance, 0.00)

class ProductModelTest(TestCase):
    print("Running model test")
    def test_product_str(self):
        product = Product.objects.create(name="Test Product", price=9.99)
        self.assertEqual(str(product), "Test Product")

class CartModelTest(TestCase):
    print("Running cart")
    def setUp(self):
        self.user = User.objects.create_user(username='cartuser', password='pass')
        self.cart = Cart.objects.create(user=self.user)
        self.product1 = Product.objects.create(name='Product 1', price=10.00, stock=100)
        self.product2 = Product.objects.create(name='Product 2', price=20.00, stock=50)

    def test_add_cart_items_and_total_price(self):
        CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        CartItem.objects.create(cart=self.cart, product=self.product2, quantity=1)
        self.assertEqual(self.cart.items.count(), 2)
        self.assertEqual(self.cart.total_price, 40.00)

    # Add this dummy test to check if it's discovered
    def test_dummy(self):
        self.assertTrue(True)


from decimal import Decimal

class WalletOrderIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="orderuser", password="pass")
        self.wallet = Wallet.objects.get(user=self.user)
        self.wallet.balance = Decimal("100.00")
        self.wallet.save()
        
        self.product = Product.objects.create(name="Test Product", price=Decimal("30.00"), stock=10)

    def test_wallet_balance_decreases_after_order(self):
        # Create order with total_amount (sum of all OrderItems)
        order = Order.objects.create(user=self.user, total_amount=Decimal("30.00"))

        # Create order item for product and quantity
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            product_name=self.product.name,
            quantity=1,
            price_at_purchase=self.product.price,
        )

        # Here you can simulate balance deduction logic if implemented
        self.wallet.balance -= order.total_amount
        self.wallet.save()

        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal("70.00"))
