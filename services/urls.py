from django.urls import path
from .views import services, delete_past_opening_hours, confirm_delete_past_opening_hours

urlpatterns = [
    # otras rutas...
    path('services/', services, name='services'),
    path('delete_past_opening_hours/', delete_past_opening_hours, name='delete_past_opening_hours'),
    path('confirm_delete_past_opening_hours/', confirm_delete_past_opening_hours, name='confirm_delete_past_opening_hours'),
]