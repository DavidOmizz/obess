
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
# Register View
# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
        
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"error": "Username already exists"}, status=400)
        
#         user = User.objects.create_user(username=username, email=email, password=password)
#         return JsonResponse({"message": "User registered successfully"})
    
#     return render(request, "register.html")

# # Login View
# def user_login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")
#         else:
#             return JsonResponse({"error": "Invalid credentials"}, status=400)
    
#     return render(request, "login.html")

# # Logout View
# def user_logout(request):
#     logout(request)
#     return redirect("login")

# # Dashboard View
# def dashboard(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
    
#     return render(request, "dashboard.html", {"user": request.user})


# Register View
# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
        
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"error": "Username already exists"}, status=400)
        
#         user = User.objects.create_user(username=username, email=email, password=password)
#         return redirect("login")
    
#     return render(request, "register.html")

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserEditForm
from .models import *
from django.db import transaction # Import for atomic transactions
# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("home")  # Redirect to the dashboard
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "register.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")  # Redirect to the dashboard
        else:
            print(form.errors)  # Debugging line
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def credit_wallet(user, amount):
    user.wallet.balance += amount
    user.wallet.save()

def debit_wallet(user, amount):
    if user.wallet.balance >= amount:
        user.wallet.balance -= amount
        user.wallet.save()
        return True
    return False  # Not enough balance



# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    
    return render(request, "login.html")

# Logout View
def user_logout(request):
    logout(request)
    return redirect("login")

# Dashboard View
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    # Retrieve the user's wallet balance
    try:
        wallet = Wallet.objects.get(user=request.user)
        balance = wallet.balance
    except Wallet.DoesNotExist:
        balance = 0  # Default to 0 if no wallet exists
    
    # products1 = [
    #     {"name": "Product 1", "price": "$10", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 2", "price": "$15", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 3", "price": "$20", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 4", "price": "$25", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 5", "price": "$30", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 6", "price": "$35", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 7", "price": "$40", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 8", "price": "$45", "image": "https://via.placeholder.com/150"},
    #     {"name": "Product 9", "price": "$50", "image": "https://via.placeholder.com/150"},
    # ]
    
    return render(request, "dashboard.html", {"user": request.user, "products": products, "balance": balance})

def certificate(request):
    return render(request, "certificate.html")
def withdraw(request):
    return render(request, "withdraw.html")
def deposit(request):
    return render(request, "deposit.html")
def viplevel(request):
    return render(request, "vip-level.html")

def profile(request):
    # Retrieve the user's wallet balance
    try:
        wallet = Wallet.objects.get(user=request.user)
        balance = wallet.balance
    except Wallet.DoesNotExist:
        balance = 0  # Default to 0 if no wallet exists
    return render(request, "profile.html", {"user": request.user, "balance": balance})

from django.contrib.auth.decorators import login_required
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace with your profile view name
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, 'edit-profile.html', {'form': form})


def products(request):
    products = Product.objects.filter(is_available=True).order_by('name')
    context = {'products': products,"user": request.user}
    return render(request, 'products.html', context)

def contact(request):
    return render(request, 'contact-us.html', {"user": request.user})

def records(request):
    return render(request, 'records.html', {"user": request.user})

def withdrawInformation(request):
    return render(request, 'withdraw-information.html', {"user": request.user})

def notification(request):
    return render(request, 'notifications.html', {"user": request.user})


from django.contrib import messages
# --- Product Views (Unchanged) ---
def product_list(request):
    products = Product.objects.filter(is_available=True).order_by('name')
    context = {'products': products}
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_available=True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

# --- Cart Views (Unchanged) ---
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f'Increased quantity of {product.name} in your cart.')
    else:
        messages.success(request, f'{product.name} added to your cart!')

    return redirect('view_cart')

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        cart = None
        cart_items = []
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity <= 0:
                cart_item.delete()
                messages.info(request, f'Removed {cart_item.product.name} from your cart.')
            else:
                # Optional: Check if quantity exceeds stock
                # if quantity > cart_item.product.stock:
                #     messages.error(request, f"Not enough stock for {cart_item.product.name}. Only {cart_item.product.stock} available.")
                #     return redirect('view_cart')

                cart_item.quantity = quantity
                cart_item.save()
                messages.success(request, f'Updated quantity for {cart_item.product.name}.')
        except ValueError:
            messages.error(request, 'Invalid quantity.')
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.warning(request, f'Removed {product_name} from your cart.')
    return redirect('view_cart')

# --- Modified Checkout View ---
@login_required
# @transaction.atomic # Ensures all database operations succeed or fail together
# def checkout(request):
#     try:
#         cart = Cart.objects.get(user=request.user)
#         cart_items = cart.items.all()
#     except Cart.DoesNotExist:
#         messages.error(request, "Your cart is empty.")
#         return redirect('product_list')

#     if not cart_items:
#         messages.error(request, "Your cart is empty.")
#         return redirect('product_list')

#     total_cart_price = cart.total_price

#     # Check if user has a wallet and sufficient balance
#     try:
#         wallet = request.user.wallet
#     except Wallet.DoesNotExist:
#         messages.error(request, "You do not have a wallet. Please contact support.")
#         return redirect('view_cart')

#     if wallet.balance < total_cart_price:
#         messages.error(request, f"Insufficient balance. Your balance: ${wallet.balance:.2f}, Required: ${total_cart_price:.2f}. Contact customer support to add funds.")
#         # return redirect('view_cart')
#         return redirect('contact')

#     # Optional: Check product stock before processing
#     for item in cart_items:
#         if item.quantity > item.product.stock:
#             messages.error(request, f"Not enough stock for {item.product.name}. Only {item.product.stock} available.")
#             return redirect('view_cart')

#     if request.method == 'POST':
#         # Assuming simple confirmation, no complex forms for now
#         # You might want to add withdrawal_pin verification here
#         # Example for PIN verification (if you hashed it, you'd use check_password):
#         from django.contrib.auth.hashers import check_password
#         entered_pin = request.POST.get('withdrawal_pin')
#         if not check_password(entered_pin, request.user.withdrawal_pin):
#             messages.error(request, "Incorrect withdrawal PIN.")
#             return render(request, 'checkout.html', {'cart': cart, 'cart_items': cart_items, 'total_cart_price': total_cart_price, 'wallet_balance': wallet.balance})

#         try:
#             # 1. Deduct from wallet balance
#             wallet.balance -= total_cart_price
#             wallet.save()

#             # 2. Optionally, reduce product stock
#             for item in cart_items:
#                 item.product.stock -= item.quantity
#                 item.product.save()

#             # 3. Clear the user's cart
#             cart_items.delete() # Deletes all cart items associated with this cart

#             messages.success(request, "Your purchase has been completed successfully!")
#             return redirect('purchase_successful') # Redirect to new success page

#         except Exception as e:
#             messages.error(request, f"An error occurred during purchase: {e}")
#             return redirect('view_cart')

#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_cart_price': total_cart_price,
#         'wallet_balance': wallet.balance,
#     }
#     return render(request, 'checkout.html', context)

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
    except Cart.DoesNotExist:
        messages.error(request, "Your cart is empty.")
        return redirect('product_list')

    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect('product_list')

    total_cart_price = cart.total_price

    try:
        wallet = request.user.wallet
    except Wallet.DoesNotExist:
        messages.error(request, "You do not have a wallet. Please contact support.")
        return redirect('view_cart')

    if wallet.balance < total_cart_price:
        messages.error(request, f"Insufficient balance. Your balance: ${wallet.balance:.2f}, Required: ${total_cart_price:.2f}. Contact customer support to add funds.")
        return redirect('contact')

    # Re-check product stock before final processing (crucial in case stock changed between cart view and checkout)
    for item in cart_items:
        if item.quantity > item.product.stock:
            messages.error(request, f"Not enough stock for {item.product.name}. Only {item.product.stock} available. Please adjust your cart.")
            return redirect('view_cart')

    if request.method == 'POST':
        # Optional: Add withdrawal_pin verification here if needed
        entered_pin = request.POST.get('withdrawal_pin')
        if not request.user.withdrawal_pin == entered_pin: # Basic comparison, hash for production!
            messages.error(request, "Incorrect withdrawal PIN.")
            context = {
                'cart': cart, 'cart_items': cart_items,
                'total_cart_price': total_cart_price, 'wallet_balance': wallet.balance,
                'show_pin_error': True # You might use this in template to show error near PIN field
            }
            return render(request, 'checkout.html', context)


        try:
            with transaction.atomic(): # Ensures all steps succeed or fail together
                # 1. Create the Order
                order = Order.objects.create(
                    user=request.user,
                    total_amount=total_cart_price, # Use the calculated cart total
                    status='delivered' # Set an initial status
                )

                # 2. Create OrderItems from CartItems and reduce product stock
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        product_name=item.product.name, # Store current product name for history
                        quantity=item.quantity,
                        price_at_purchase=item.product.price # Store price at time of purchase
                    )
                    # Reduce actual product stock
                    item.product.stock -= item.quantity
                    item.product.save()

                # 3. Deduct from wallet balance
                wallet.balance -= total_cart_price
                wallet.save()

                # 4. Clear the user's cart (delete all CartItems associated with this cart)
                cart_items.delete() # Deletes all cart items related to this cart object

                messages.success(request, "Your purchase has been completed successfully!")
                return redirect('purchase_successful')

        except Exception as e:
            messages.error(request, f"An error occurred during purchase: {e}. Please try again or contact support.")
            # Log the exception for debugging
            # import logging
            # logging.exception("Checkout error")
            return redirect('view_cart')

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
        'wallet_balance': wallet.balance,
    }
    return render(request, 'checkout.html', context)

# New simple purchase success view
@login_required
def purchase_successful(request):
    return render(request, 'purchase_successful.html')

# --- NEW: Purchase History View ---
@login_required
def purchase_history(request):
    # Fetch all orders for the currently logged-in user, ordered by most recent
    # prefetch_related('items__product') efficiently fetches related OrderItems and their Products
    orders = Order.objects.filter(user=request.user).order_by('-created_at').prefetch_related('items__product')

    all_purchased_items = OrderItem.objects.filter(
        order__user=request.user
    ).select_related('order', 'product').order_by('-order__created_at', 'id')

    context = {
        'orders': orders, # Changed 'purchases' to 'orders' to match your model name
        'all_purchased_items': all_purchased_items,
    }
    return render(request, 'purchase_history.html', context) # Make sure your template path is correct


# New simple purchase success view
# @login_required
# def purchase_successful(request):
#     return render(request, 'purchase_successful.html')