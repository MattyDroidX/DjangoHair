from django.contrib import admin
from .models import *

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'is_active', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
