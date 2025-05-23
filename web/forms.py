"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: forms.py
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

from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["nombre", "correo", "asunto", "mensaje"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Tu Nombre'}),
            'correo': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Tu Correo Electronico'}),
            'asunto': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Escribe tu mensaje aqui...'}),
        }
        