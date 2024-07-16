from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import *
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout , login , authenticate ,update_session_auth_hash 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views import View

# Create your views here.

def cerrar(request):
    logout(request)
    return redirect("index") 

def index(request):
    queryset = Hotel.objects.all()
    datos = {
        'productos': queryset,
    }
    return render(request,'index.html',datos)

def login_xd(request):
    if request.method=="POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            user = form.user_cache  
            if user.es_baneado:
                messages.warning(request, "su usuario esta baneado") 
                messages.warning(request, "si desea asistencia utilize los contactos") 
                return redirect("login")
            login(request ,user)
            if user.is_staff:
                return redirect("trabajador")
            return redirect("index")
        else :
            messages.warning(request, "usuario o contraseña incorrectos") 
            return redirect("login")
    else :
        form = loginForm()
    datos ={
        "form":form
    }
    return render(request,'login.html',datos)

def registro(request):
    form = createUser()
    
    if request.method=="POST":
        form=createUser(data=request.POST)
        
        if form.is_valid():
            form.save()
    
            return redirect("login")
            #Redirigir  
        
    datos= {
        "form":form,
    }
    return render(request , 'registro.html' , datos)

def trabajador(request):
    promociones = Promocion.objects.all()  # Obtiene todas las promociones
    
    context = {
        'promociones': promociones
    }
    
    if request.user.is_authenticated and request.user.is_gerente:
        return render(request,'trabajador.html',context)
    return render(request,'login.html') 
  
def ver_habitaciones(request,id_h):
    habitaciones = Habitacion.objects.filter(hotel=id_h)
    filter_form = HabitacionFilterForm(request.GET)
    
    if filter_form.is_valid():
        habitaciones = filter_form.filter_queryset(habitaciones)
    
    context = {
        'filter_form': filter_form,
        'habitaciones': habitaciones,
    }
    
    return render(request, 'ver_habitaciones.html', context)

def ver_habitacion(request,id_h):
    habitacion = get_object_or_404(Habitacion, pk=id_h)
    
    context = {
        'habitacion': habitacion,
    }
    return render(request, 'ver_habitacion.html', context)

def reservar(request,id):
    habitacion = get_object_or_404(Habitacion, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, user=request.user)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.habitacion = habitacion  # Asigna la habitación seleccionada al campo 'habitacion' de la reserva
            reserva.save()
            return redirect('index')  # Redirige a una página de confirmación o a otra vista
    else:
        form = ReservaForm(user=request.user)

    return render(request, 'Reservar.html', {'form': form, 'habitacion': habitacion})

def ver_promos(request):
    promociones = Promocion.objects.filter(validada=True)
    context = {
        'promociones': promociones,
    }
    return render(request, 'ver_promos.html', context)


def editar_promocion(request, id):
    promocion = get_object_or_404(Promocion, pk=id)
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('trabajador')  # Redirige a la vista de todas las promociones
    else:
        form = PromocionForm(instance=promocion)

    return render(request, 'editar_promocion.html', {'form': form, 'promocion': promocion})

def agregar_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción agregada exitosamente.')
            return redirect('trabajador')  # Reemplaza con el nombre de tu URL de éxito
    else:
        form = PromocionForm()
    
    return render(request, 'agregar_promocion.html', {'form': form})