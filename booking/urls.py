from django.urls import path
from .views import create_booking, success_booking

urlpatterns = [
    path('booking/', create_booking, name='create_booking'),
    path('booking/success_booking/', success_booking, name='success_booking'),
]


