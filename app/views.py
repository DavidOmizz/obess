
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse

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
from .forms import CustomUserCreationForm
from .models import *
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
    
    products = [
        {"name": "Product 1", "price": "$10", "image": "https://via.placeholder.com/150"},
        {"name": "Product 2", "price": "$15", "image": "https://via.placeholder.com/150"},
        {"name": "Product 3", "price": "$20", "image": "https://via.placeholder.com/150"},
        {"name": "Product 4", "price": "$25", "image": "https://via.placeholder.com/150"},
        {"name": "Product 5", "price": "$30", "image": "https://via.placeholder.com/150"},
        {"name": "Product 6", "price": "$35", "image": "https://via.placeholder.com/150"},
        {"name": "Product 7", "price": "$40", "image": "https://via.placeholder.com/150"},
        {"name": "Product 8", "price": "$45", "image": "https://via.placeholder.com/150"},
        {"name": "Product 9", "price": "$50", "image": "https://via.placeholder.com/150"},
    ]
    
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