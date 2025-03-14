
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
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")
    
    return render(request, "register.html")

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
    
    return render(request, "dashboard.html", {"user": request.user, "products": products})

def certificate(request):
    return render(request, "certificate.html")
def withdraw(request):
    return render(request, "withdraw.html")
def deposit(request):
    return render(request, "deposit.html")