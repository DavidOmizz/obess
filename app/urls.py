# urls.py
from django.urls import path
# from .views import register, user_login, user_logout, dashboard, certificate, withdraw, deposit, viplevel, profile, products, contact,records,withdrawInformation,edit_profile,notification
from . import views
urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('certificate/' , views.certificate, name='certificate'),
    path('withdraw/' , views.withdraw, name='withdraw'),
    path('deposit/' , views.deposit, name='deposit'),
    path('viplevel/' , views.viplevel, name='viplevel'),
    path('profile/' , views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('records/', views.records, name='records' ),
    path('notifications/', views.notification, name='notifications' ),
    path('withdrawInformation/', views.withdrawInformation, name='withdrawInformation' ),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    # Removed: path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('purchase-successful/', views.purchase_successful, name='purchase_successful'), # New success page
    path('order-history/', views.purchase_history, name='order_history'),
]