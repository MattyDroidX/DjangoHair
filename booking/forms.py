from django import forms
from .models import Booking
from services.models import TimeSlot
from datetime import date

class BookingForm(forms.ModelForm):

    timeslot = forms.ModelChoiceField(queryset=TimeSlot.objects.all(), empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Booking
        fields = ['salon', 'service', 'timeslot']

        






