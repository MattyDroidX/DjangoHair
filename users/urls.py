from django.urls import path
from .views import register

urlpatterns = [
    # Otras URL de la aplicación
    path('register/', register, name='register'),
]