from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from services.models import HairSalon, Service, TimeSlot
from django.db.models import Q

# Create your models here.

class Booking(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_bookings')
    salon = models.ForeignKey(HairSalon, on_delete=models.CASCADE, related_name='salon_booking')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_booking')
    timeslot= models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='time_slot_booking')
    booking_date = models.DateField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Bookings"
        unique_together = ('salon', 'timeslot')
        ordering = ['timeslot']

    def __str__(self):
        return f'Turno para {self.user.email} - {self.service.service_type} - {self.timeslot}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Marcar el campo is_reservated como True directamente desde el modelo Booking
        TimeSlot.objects.filter(pk=self.timeslot.pk).update(is_reservated=True)
    
        overlapping_slots = TimeSlot.objects.filter(
            Q(opening_hours=self.timeslot.opening_hours),
            Q(date=self.timeslot.date),
            (
                Q(start_time__lt=self.timeslot.end_time, end_time__gt=self.timeslot.start_time) |
                Q(start_time__gte=self.timeslot.start_time, end_time__lte=self.timeslot.end_time) |
                Q(start_time__lte=self.timeslot.start_time, end_time__gte=self.timeslot.end_time)
            )
        ).exclude(pk=self.timeslot.pk)  # Excluye el turno que ya se ha marcado como reservado

        for overlapping_slot in overlapping_slots:
            overlapping_slot.is_blocked = True
            overlapping_slot.save()
    



    