from django.shortcuts import render, redirect
from .forms import BookingForm
from services.models import OpeningHours, TimeSlot


def create_booking(request):

    available_days = TimeSlot.objects.values_list('date', flat=True).distinct()
    timeslots_by_day = {}
    hours = OpeningHours.objects.all()

    for day in available_days:
        timeslots_by_day[day] = TimeSlot.objects.filter(date=day)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            timeslot_id = request.POST.get('timeslot')
            timeslot = TimeSlot.objects.get(id=timeslot_id)
            booking.timeslot = timeslot
            booking.save()
            return redirect('success_booking')  # Redirige a alguna página después de una reserva exitosa
    else:
        form = BookingForm()
        

    context = {
        'form': form,
        'hours': hours,
        'timeslots_by_day': timeslots_by_day
    }
    
    return render(request, 'booking/booking.html', context)

def success_booking(request):
    return render(request, 'booking/success_booking.html', {})


