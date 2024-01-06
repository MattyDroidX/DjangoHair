from django import forms
from .models import Booking
from services.models import TimeSlot, HairSalon, Service
from datetime import date

class BookingForm(forms.ModelForm):

    timeslot = forms.ModelChoiceField(queryset=TimeSlot.objects.all(), empty_label=None, widget=forms.RadioSelect)
    salon = forms.ModelChoiceField(queryset=HairSalon.objects.all(), widget=forms.Select(attrs={'class': 'custom-select'}))
    service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.Select(attrs={'class': 'custom-select'}))


    class Meta:
        model = Booking
        fields = ['salon', 'service', 'timeslot']

        






