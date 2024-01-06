from django.urls import path
from .views import create_booking_authenticated, get_booking_hair, get_booking_hair_beard, user_bookings, cancel_booking

urlpatterns = [
    path('booking_hair/', get_booking_hair, name='get_booking_hair'),
    path('booking_hair_beard/', get_booking_hair_beard, name='get_booking_hair_beard'),
    path('create_booking/', create_booking_authenticated, name='create_booking_authenticated'),
    path('user/bookings/', user_bookings, name='user_bookings'),
    path('user/bookings/<int:booking_id>/cancel/', cancel_booking, name='cancel_booking'),
]


