"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: models.py
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

from django.db import models

class Proyecto(models.Model):
    ESTADOS = [
        ('produccion', '🟢 En Producción'),
        ('beta', '🟣 En Beta'),
        ('desarrollo', '🟡En Desarrollo'),
        ('finalizado', '🔴 Finalizado')
    ]
    
    TIPOS_PROYECTOS = [
        ('web', '🌐 Aplicación Web'),
        ('escritorio', '🖥️ Sotfware de Escritorio'),
        ('movil', '📱 Aplicación Móvil'),
        ('ai', '🤖 Asistente Virtual')
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='desarrollo')
    tipo = models.CharField(max_length=20, choices=TIPOS_PROYECTOS, default='web')
    progreso = models.IntegerField(default=0)
    tecnologias = models.CharField(max_length=255, default='Sin especificar')
    version = models.CharField(max_length=10, default=1.0)
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    enlace = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto}"