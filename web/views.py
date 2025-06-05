"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: views.py
Fecha de inserción: 2025-05-17

Este archivo es parte del repositorio oficial de Developments Berlad y está
protegido por derechos de autor. No está permitida su copia, modificación
ni redistribución sin autorización expresa.

This file is part of the official Developments Berlad repository.
It is protected by copyright and may not be copied, modified, or distributed
without express permission.

ℹ️ Para más información, consulte el archivo README (disponible en varios idiomas).
ℹ️ For more information, see the README file (available in multiple languages).
------------------------------------------------------------------------------

"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactoForm
from .models import Proyecto, Certificados


def index(request):
    return render(request, 'Web/index.html')

def proyectos(request):
    estado_filtro= request.GET.get('estado', 'todos')
    tipo_filtro= request.GET.get('tipo', 'todos')
    tecnologias_filtro = request.GET.get('tecnologias', 'todos')
    orden_por_progreso = request.GET.get('orden', 'descendente')
    
    proyectos = Proyecto.objects.all()
    
    if estado_filtro != 'todos':
        proyectos = proyectos.filter(estado=estado_filtro)
        
    if tipo_filtro != 'todos':
        proyectos = proyectos.filter(tipo=tipo_filtro)
        
    if tecnologias_filtro != 'todos':
        proyectos = proyectos.filter(tecnologias__icontains=tecnologias_filtro)
        
    if orden_por_progreso == 'ascendente':
        proyectos = proyectos.order_by('progreso')
    else:
        proyectos = proyectos.order_by('-progreso')
        
    return render(request, 'Web/projects/list.html', {
        'proyectos': proyectos,
        'estado_filtro': estado_filtro,
        'tipo_filtro':tipo_filtro,
        'tecnologias_filtro':tecnologias_filtro,
        'ordenar_por_progreso' : orden_por_progreso
        })

def sobre_mi(request):
    certificados = Certificados.objects.all()
    return render(request, 'Web/sobre_mi.html', {
        'certificados' : certificados
    })

def certificados(request):
    estado_filtro = request.GET.get('estado', 'todos')
    orden_por_progreso = request.GET.get('progreso', 'descendente')
    
    certificados = Certificados.objects.all()
    if estado_filtro != 'todos':
        certificados = certificados.filter(estado=estado_filtro)
    
    if orden_por_progreso == 'ascendente':
        certificados = certificados.order_by('progreso')
    else:
        certificados = certificados.order_by('-progreso')
    
    return render(request, "Web/certificados.html", {
        'estado_filtro' : estado_filtro,
        'ordenar_por_progreso' : orden_por_progreso,
        'certificados' : certificados
    })

def contacto(request):
    form = ContactoForm()
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            try:
                contacto = form.save(commit=False)  # Aún no se guarda en la base de datos
                
                # Enviar correo
                send_mail(
                    subject=f"Nuevo mensaje de {contacto.nombre} - Asunto: {contacto.asunto}",
                    message=f"Correo del remitente: {contacto.correo}\n\nMensaje:\n{contacto.mensaje}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],  
                    fail_silently=False,
                )
                
                contacto.save()  # Se guarda después del envío exitoso
                messages.success(request, '✅ ¡Tu mensaje ha sido enviado con éxito!')
                return redirect('contacto')

            except BadHeaderError:
                messages.error(request, '❌ Encabezado inválido encontrado.')

            except Exception as e:
                messages.warning(request, f'❌ Error al enviar el correo: {e}')
    
    return render(request, 'Web/contacto.html', {'form': form})
