from django.shortcuts import render
from services.models import Service

# Create your views here.

def home(request):    
    services = Service.objects.all()
    print(services)
    context = {'services': services}
    return render(request, 'home.html', context)
