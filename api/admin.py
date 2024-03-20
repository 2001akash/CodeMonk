# api/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    search_fields = ('username', 'email')

admin.site.register(User, CustomUserAdmin)