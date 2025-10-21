# tourist_management_system_project/users/admin.py

from django.contrib import admin
from .models import UserProfile # Import your UserProfile model
from django.contrib.auth.models import User # Also import Django's built-in User model

# Register your models here.
admin.site.register(UserProfile)

# Optional: You can also customize how the UserProfile is displayed in relation to the User
# For now, just registering UserProfile is enough.