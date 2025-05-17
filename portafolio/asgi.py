"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: asgi.py
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

"""
ASGI config for portafolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')

application = get_asgi_application()
