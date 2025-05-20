from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "phone_number", "withdrawal_pin", "gender", "invitation_code", "password1", "password2"]



class CustomUserEditForm(UserChangeForm):
    password = None  # Exclude the password field

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'withdrawal_pin', 'gender', 'invitation_code']
