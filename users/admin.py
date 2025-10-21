
from django.contrib import admin
from .models import UserProfile # Import your UserProfile model
from django.contrib.auth.models import User # Also import Django's built-in User model

# Register your models here.
admin.site.register(UserProfile)