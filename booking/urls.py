from django.urls import path
from .views import success_booking, create_booking_authenticated, get_booking, user_bookings, cancel_booking

urlpatterns = [
    path('booking/', get_booking, name='get_booking'),
    path('create_booking/', create_booking_authenticated, name='create_booking_authenticated'),
    path('booking/success_booking/', success_booking, name='success_booking'),
    path('user/bookings/', user_bookings, name='user_bookings'),
    path('user/bookings/<int:booking_id>/cancel/', cancel_booking, name='cancel_booking'),
]


