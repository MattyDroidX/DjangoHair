from django.urls import path
from .views import services

urlpatterns = [
    # otras rutas...
    path('services/', services, name='services'),
]