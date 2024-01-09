from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta, date, time
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class HairSalon(models.Model):
    name = models.CharField(max_length=50, unique=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return f'{self.name}, {self.street}, {self.city}'   
    
    class Meta:
        verbose_name_plural = "Salon"


class OpeningHours(models.Model):

    salon = models.ForeignKey(HairSalon, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField()

    class Meta:
        verbose_name_plural = "Horarios"

    def get_opening_hours(self):
            if self.is_closed:
                return _("Cerrado todo el día")
            nombre_dia_semana = self.date.strftime('%A')
            return f"El {nombre_dia_semana} {self.date.strftime('%d de %B de %Y')} desde {self.opening_time} hasta {self.closing_time}"
    
    def get_time_slots_by_date(self, date):
        return self.timeslot_set.filter(opening_hours=self, opening_hours__date=date)
    
    def __str__(self):
        return f"{self.get_opening_hours()}"
    
    

# CREA TIME SLOTS DE CORTE 
    def create_time_slots(self):
        # Elimina los TimeSlot existentes para este OpeningHours antes de recrearlos
        self.timeslot_set.all().delete()

        # Convierte opening_time y closing_time a objetos datetime
        opening_datetime = datetime.combine(self.date, self.opening_time)
        closing_datetime = datetime.combine(self.date, self.closing_time)

        # Divide ese tiempo en intervalos más pequeños (puedes ajustar el intervalo según tus necesidades)
        intervals = [timedelta(minutes=40), timedelta(minutes=60)]
        current_datetime = opening_datetime

        for interval in intervals:
            current_datetime = opening_datetime
            duration = interval.total_seconds() // 60

            while current_datetime < closing_datetime:
                end_datetime = current_datetime + interval

                # Crea el TimeSlot
                TimeSlot.objects.create(
                    opening_hours=self,
                    date = self.date,
                    start_time=current_datetime.time(),
                    end_time=end_datetime.time(),
                    is_blocked=False,  # Puedes ajustar esto según tus necesidades
                    duration = duration
                )

                current_datetime = end_datetime

    # Este método se llamará después de guardar una instancia de OpeningHours
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_time_slots()

@receiver(post_save, sender=OpeningHours)
def create_timeslots_on_openinghours_save(sender, instance, **kwargs):
    instance.create_time_slots()


class TimeSlot(models.Model):

    opening_hours = models.ForeignKey(OpeningHours, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_blocked = models.BooleanField()
    is_reservated = models.BooleanField(default=False)
    duration = models.IntegerField(default=40)

    class Meta:
        verbose_name_plural = "Turnos"

    def __str__(self):
        return f'El turno es el {self.opening_hours.date} desde {self.start_time} hasta {self.end_time}'
    
    
class Service(models.Model):
    SERVICE_TYPE = [
        ("Corte de cabello", "Corte de cabello"),
        ("Corte y barba", "Corte y barba"),
    ]

    description = models.TextField(blank=True, null=True)
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.service_type}'
    
    class Meta:
        verbose_name_plural = 'Servicios'
        ordering = ['id']










    
    


