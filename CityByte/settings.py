"""
Django settings for CityByte project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cm&ek+rlsg%=@47_^f7@^_d0o6^#azfb%oel1h8x65c06*b2u8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search'
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

ROOT_URLCONF = 'CityByte.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'CityByte.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GEODB_CONFIG = {
    "protocol": "https",
    "host": "wft-geo-db.p.rapidapi.com",
    "port": 443,
    "headers": {
        'x-rapidapi-key': os.environ.get("GEODB_X_RAPID_API_KEY"),
        'x-rapidapi-host': os.environ.get("GEODB_X_RAPID_API_HOST")
    }
}

AMADEUS_CONFIG = {
    "protocol": "https",
    "host": "test.api.amadeus.com",
    "port": 443,
    "headers": {
        "API_KEY": os.environ.get("AMADEUS_API_KEY"),
        "API_SECRET_KEY": os.environ.get("AMADEUS_API_SECRET_KEY"),
    }
}

UNSPLASH_CONFIG = {
    "protocol": "https",
    "host": "api.unsplash.com",
    "port": 443,
    "headers": {
        'Authorization': f"Client-ID {os.environ.get('UNSPLASH_API_KEY')}",
    }
}

FOURSQUARE_CONFIG = {
    "protocol": "https",
    "host": "api.foursquare.com",
    "port": 443,
    "headers": {
        'Authorization': os.environ.get("FOURSQUARE_API_KEY"),
    }
}

WEATHER_BIT_CONFIG = {
    "protocol": "https",
    "host": "weatherbit-v1-mashape.p.rapidapi.com",
    "port": 443,
    "headers": {
        'X-RapidAPI-Key': os.environ.get("WEATHER_BIT_X_RAPID_API_KEY"),
        'X-RapidAPI-Host': os.environ.get("WEATHER_BIT_X_RAPID_API_HOST"),
    }
}
