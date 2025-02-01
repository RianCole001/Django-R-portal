# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):  # Ensure this is capitalized as 'Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
