from django.shortcuts import render
from .models import Service, OpeningHours
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.db import transaction
from django.utils import timezone
from .forms import ConfirmDeleteForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

def services(request):

    services = Service.objects.all()
    context = {'services': services}
    
    return render(request, 'services.html', context)

@user_passes_test(is_admin)
@require_GET
def confirm_delete_past_opening_hours(request):
    current_date = timezone.now().date()
    past_opening_hours = OpeningHours.objects.filter(date__lt=current_date)

    form = ConfirmDeleteForm()

    return render(
        request,
        'confirm_delete_past_opening_hours.html',
        {'past_opening_hours': past_opening_hours, 'form': form}
    )

@user_passes_test(is_admin)
@require_POST
def delete_past_opening_hours(request):
    form = ConfirmDeleteForm(request.POST)

    if form.is_valid() and form.cleaned_data['confirmation']:
        try:
            current_date = timezone.now().date()
            past_opening_hours = OpeningHours.objects.filter(date__lt=current_date)

            with transaction.atomic():
                past_opening_hours.delete()

            response_data = {'success': True, 'message': 'OpeningHours pasadas eliminadas correctamente.'}
        except Exception as e:
            response_data = {'success': False, 'message': f'Error: {str(e)}'}
    else:
        response_data = {'success': False, 'message': 'Confirmación no válida.'}

    return render(request, 'delete_past_opening_hours_result.html', response_data)




 

