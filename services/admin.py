from django.contrib import admin
from .models import *

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('opening_hours_day', 'start_time', 'end_time', 'is_blocked', 'is_reservated')
    list_per_page = 12

    def opening_hours_day(self, obj):
        return obj.opening_hours.date.strftime('%A %d de %b. %Y')

    opening_hours_day.short_description = 'Día de la semana'

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(HairSalon)
admin.site.register(OpeningHours)
admin.site.register(Service)

