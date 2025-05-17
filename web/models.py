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
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
#    imagen = models.ImageField(upload_to='proyectos/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
