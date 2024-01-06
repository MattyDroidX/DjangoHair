from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'service_type', 'timeslot_info')

    def user_email(self, obj):
        return obj.user.email

    def service_type(self, obj):
        return obj.service.service_type

    def timeslot_info(self, obj):
        return f'{obj.timeslot.date} desde {obj.timeslot.start_time} hasta {obj.timeslot.end_time}'

    user_email.short_description = 'Cliente'
    service_type.short_description = 'Tipo de Servicio'
    timeslot_info.short_description = 'Información del Turno'

admin.site.register(Booking, BookingAdmin)