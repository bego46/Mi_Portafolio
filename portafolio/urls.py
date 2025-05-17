"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: urls.py
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
URL configuration for portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
   
]

""" 
# Páginas principales
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('projects/', views.projects, name='projects'),
path('contact/', views.contact, name='contact'), """
""" 
# Blog (con CRUD completo + comentarios)
path('blog/', include([
    path('', views.blog, name='blog'),
    path('new/', views.new_blog_post, name='new_blog_post'),
    path('<int:post_id>/', views.blog_post, name='blog_post'),
    path('<int:post_id>/edit/', views.edit_blog_post, name='edit_blog_post'),
    path('<int:post_id>/delete/', views.delete_blog_post, name='delete_blog_post'),
    path('<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:post_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('<int:post_id>/comment/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
])), """