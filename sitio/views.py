# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse
import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse

def contacto(request):
    if request.method == "POST":
        messages.success(request, "<i class='fa fa-info-circle' ></i> Su mensaje ha sido enviado correctamente!")
    return render(request, 'contacto.html', {})

def mapa_sitio(request):
    mostrar = True
    return render(request, 'mapa.html', {'mostrar':mostrar})

''' INICIO PORTAL CLIENTE '''
def dashboard(request):
    paciente = request.user
    hoy = datetime.datetime.today()
    fecha_inicio = datetime.date(hoy.year, 1, 1)
    fecha_fin = datetime.date(hoy.year, 12, 31)
    total_citas = Cita.objects.filter(paciente=paciente).count()
    citas_faltantes = Cita.objects.filter(paciente=paciente, dia_agendado__range=(fecha_inicio, fecha_fin)).count()

    return render(request, 'dashboard.html', {'total_citas':total_citas, 'citas_faltantes':citas_faltantes})

def perfilusuario(request):
    usuario = get_object_or_404(User, username=request.user)
    perfil = get_object_or_404(PerfilUsuario, user=usuario)

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=usuario)
        perfil_form = ProfileForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()

            messages.success(request, 'Se actualizo correctamente el perfil <strong>{0}</strong>'.format(usuario.username), extra_tags='safe' )
            return HttpResponseRedirect(reverse('index'))

    else:
        user_form = UserForm(instance=usuario)
        perfil_form = PerfilUsuarioForm(instance=perfil)
    
    return render(request, 'perfilusuario.html', {'user_form':user_form, 'perfil_form':perfil_form})

def lista_citas(request):
    user = get_object_or_404(User, username=request.user)
    lista_citas = Cita.objects.select_related("paciente", "doctor").filter(paciente=user)

    return render(request, 'lista_citas.html', {'lista_citas':lista_citas})

def agregar_cita(request):
    fecha_hoy = datetime.datetime.now().strftime("%d/%m/%Y")
    titulo = "<i class='fas fa-calendar-plus'></i> Agregar Cita"
    if request.method == "POST":
        agregar_cita_form = AgregarCitaForm(request.POST)
        if agregar_cita_form.is_valid():
            doctor = get_object_or_404(User, username="albertoarjona")
            agregar_cita = agregar_cita_form.save(commit=False)
            agregar_cita.paciente = request.user
            agregar_cita.doctor = doctor
            agregar_cita.estado = Cita.pendiente
            agregar_cita.save()

            messages.success(request, "Cita agregada correctamente!")
            return HttpResponseRedirect(reverse('lista_citas'))
    else:
        agregar_cita_form = AgregarCitaForm()

    return render(request, 'agregar_cita.html', {'agregar_cita_form': agregar_cita_form, 'fecha_hoy':fecha_hoy, 'titulo':titulo})

def editar_cita(request, id_cita):
    fecha_hoy = datetime.datetime.now().strftime("%d/%m/%Y")
    titulo = "<i class='fas fa-calendar-alt'></i> Editar Cita"
    cita_existente = Cita.objects.filter(paciente=request.user, id=id_cita)
    if cita_existente.exists():
        cita_existente = cita_existente[0]
        if request.method == "POST":
            agregar_cita_form = AgregarCitaForm(request.POST, instance=cita_existente)
            if agregar_cita_form.is_valid():
                agregar_cita_form.save()
                messages.success(request, "<i class='fas fa-info-circle'></i> Su cita ha sido editada correctamente!")
                return HttpResponseRedirect(reverse('lista_citas'))
        else:
            agregar_cita_form = AgregarCitaForm(instance=cita_existente)
    else:
        messages.warning(request, "<i class='fas fa-info-warning'></i> La cita que desea editar no ha sido encontrada. Contacte al personal")
        return HttpResponseRedirect(reverse('lista_citas'))

    return render(request, 'agregar_cita.html', {'agregar_cita_form':agregar_cita_form, 'fecha_hoy':fecha_hoy, 'titulo':titulo, 'x':cita_existente})

def eliminar_cita(request, id_cita):
    cita = get_object_or_404(Cita, id=id_cita)

    if request.method == "POST":
        cita.delete()
        messages.success(request, "<i class='fas fa-info-circle'></i> La cita ha sido eliminada correctamente.")
        return HttpResponseRedirect(reverse('lista_citas'))

    return render(request, 'eliminar_cita.html', {'cita':cita})

def documentacion(request):
        
    return render(request, 'documentacion.html', {})

#Handling Errors:
def _404(request):
    return render(request, '404.html', {})