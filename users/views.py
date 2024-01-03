from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Reemplaza 'nombre_de_la_pagina_de_inicio' con el nombre de tu página de inicio
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
