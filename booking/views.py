from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from django.db.models import Q
from services.models import OpeningHours, TimeSlot
from dinastia_salon.views import home
from services.models import Service
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_booking_hair(request):
    available_days = TimeSlot.objects.values_list('date', flat=True).distinct()
    timeslots_by_day = {}
    hours = OpeningHours.objects.all()

    for day in available_days:
        timeslots_by_day[day] = TimeSlot.objects.filter(date=day, duration=40)

    # Paginación
    page = request.GET.get('page')
    paginator = Paginator(available_days, 6)  # Muestra 6 días por página
    try:
        current_days = paginator.page(page)
    except PageNotAnInteger:
        current_days = paginator.page(1)
    except EmptyPage:
        current_days = paginator.page(paginator.num_pages)

    form = BookingForm()
    form.fields['service'].queryset = Service.objects.filter(service_type='Corte de cabello')
    title = Service.objects.filter(service_type='Corte de cabello')
    context = {
        'form': form,
        'hours': hours,
        'timeslots_by_day': timeslots_by_day,
        'current_days': current_days, 
        'title': title
    }

    return render(request, 'booking/booking.html', context)


def get_booking_hair_beard(request):
    available_days = TimeSlot.objects.values_list('date', flat=True).distinct()
    timeslots_by_day = {}
    hours = OpeningHours.objects.all()

    for day in available_days:
        timeslots_by_day[day] = TimeSlot.objects.filter(date=day, duration=60)

    # Paginación
    page = request.GET.get('page')
    paginator = Paginator(available_days, 6)  # Muestra 6 días por página
    try:
        current_days = paginator.page(page)
    except PageNotAnInteger:
        current_days = paginator.page(1)
    except EmptyPage:
        current_days = paginator.page(paginator.num_pages)

    form = BookingForm()
    form.fields['service'].queryset = Service.objects.filter(service_type='Corte y barba')
    title = Service.objects.filter(service_type='Corte y barba')

    context = {
        'form': form,
        'hours': hours,
        'timeslots_by_day': timeslots_by_day,
        'current_days': current_days,
        'title': title
    }

    return render(request, 'booking/booking.html', context)


@login_required
def create_booking_authenticated(request):

    user = request.user

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            timeslot_id = request.POST.get('timeslot')
            timeslot = TimeSlot.objects.get(id=timeslot_id)
            booking.timeslot = timeslot
            booking.user = user

            booking.save()
            return redirect('user_bookings')

    # Si el método no es 'POST', redirigir a la vista para el método 'GET'
    return home(request)

@login_required
def user_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)

    context = {
        'bookings': bookings
    }

    return render(request, 'booking/user_bookings.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Almacenar el ID del timeslot antes de cancelar la reserva
        timeslot_id = booking.timeslot.id

        # Cancelar la reserva
        
        booking.delete()

        # Volver a habilitar el timeslot asociado
        timeslot = get_object_or_404(TimeSlot, id=timeslot_id)
        timeslot.is_reservated = False
        timeslot.save()

        # Liberar los timeslots bloqueados debido a la superposición de horarios
        overlapping_slots = TimeSlot.objects.filter(
            Q(opening_hours=timeslot.opening_hours),
            Q(date=timeslot.date),
            (
                Q(start_time__lt=timeslot.end_time, end_time__gt=timeslot.start_time) |
                Q(start_time__gte=timeslot.start_time, end_time__lte=timeslot.end_time) |
                Q(start_time__lte=timeslot.start_time, end_time__gte=timeslot.end_time)
            )
        ).exclude(pk=timeslot.pk)  # Excluye el timeslot que ya se ha marcado como reservado

        for overlapping_slot in overlapping_slots:
            overlapping_slot.is_blocked = False
            overlapping_slot.save()

        # Redirigir a la lista de reservas del usuario o a una página de confirmación
        return redirect('user_bookings')

    # Si el método no es 'POST', podrías renderizar un formulario de confirmación de cancelación
    context = {
        'booking': booking,
    }
    return render(request, 'booking/cancel_booking.html', context)

