from django.contrib import admin
from .models import *

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_full_name', 'phone_number', 'is_active', 'is_staff')

    def user_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    user_full_name.short_description = 'Nombre completo'

admin.site.register(CustomUser, CustomUserAdmin)
