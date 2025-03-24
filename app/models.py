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