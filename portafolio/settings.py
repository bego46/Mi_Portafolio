"""
------------------------------------------------------------------------------
Autor: Berlad Gonzalez Valenzuela para Developments Berlad (<DB/>)
Proyecto: Portafolio personal de desarrollo web.
Archivo: settings.py
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



from pathlib import Path
#from dotenv import load_dotenv
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')
# SECRET_KEY = '=xy5v(vi0$3xv)1bm1r5g0)r!3g1bgz&kybm%*8^v*xbfx-@n6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portafolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portafolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_TZ = True

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'web/static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Seguridad de Cookies

SESSION_COOKIE_SECURE = True        # Solo por HTTPS
CSRF_COOKIE_SECURE = True           # Solo por HTTPS
SESSION_COOKIE_HTTPONLY = True      # No accesible desde JS

# Seguridad del navegador

SECURE_BROWSER_XSS_FILTER = True         # Protección XSS
SECURE_CONTENT_TYPE_NOSNIFF = True       # Evita que el navegador adivine el tipo de contenido
X_FRAME_OPTIONS = 'DENY'                 # Evita que tu web se cargue en un iframe



# INSTALLED_APPS += ['csp']

# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", 'cdn.jsdelivr.net', 'cdnjs.cloudflare.com')
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'fonts.googleapis.com')
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')

