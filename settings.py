import os
from pathlib import Path
import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ================= INSTALLED APPS =================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APP
    'home',

    # API
    'rest_framework',

    # CORS
    'corsheaders',
]


# ================= MIDDLEWARE =================
# ================= MIDDLEWARE =================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware', # یہ لازمی ہے
    
    'django.middleware.common.CommonMiddleware',
    
    # 'django.middleware.csrf.CsrfViewMiddleware',  # آپ کا CSRF مسئلہ حل کرنے کے لیے اسے ہم نے بند ہی رکھا ہے
    
    'django.contrib.auth.middleware.AuthenticationMiddleware', # یہ لازمی ہے
    
    'django.contrib.messages.middleware.MessageMiddleware', # یہ لازمی ہے
    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myproject.urls'


# ================= TEMPLATES =================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'myproject.wsgi.application'


# ================= DATABASE =================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# ================= PASSWORD =================

AUTH_PASSWORD_VALIDATORS = []


# ================= LANGUAGE =================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ================= STATIC =================

STATIC_URL = 'static/'


# ================= DEFAULT AUTO FIELD =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ================= CORS & CSRF TRUSTED ORIGINS =================

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


# ================= DRF CONFIGURATION =================

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [], # سیشن اتھنٹیکیشن کو گلوبل لیول پر خالی رکھا ہے تاکہ کوکی کا رولا نہ ہو
}


# ================= COOKIE SETTINGS =================

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'