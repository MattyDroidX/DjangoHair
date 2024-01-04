from django.shortcuts import render
from .models import Service

def services(request):
    services = Service.objects.all()
    print(services)
    context = {'services': services}
    return render(request, 'services.html', context)


 

