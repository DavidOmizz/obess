# urls.py
from django.urls import path
from .views import register, user_login, user_logout, dashboard, certificate, withdraw, deposit, viplevel, profile, products, contact,records,withdrawInformation

urlpatterns = [
    path("", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard", dashboard, name="dashboard"),
    path('certificate/' , certificate, name='certificate'),
    path('withdraw/' , withdraw, name='withdraw'),
    path('deposit/' , deposit, name='deposit'),
    path('viplevel/' , viplevel, name='viplevel'),
    path('profile/' , profile, name='profile'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('records/', records, name='records' ),
    path('withdrawInformation/', withdrawInformation, name='withdrawInformation' ),
]