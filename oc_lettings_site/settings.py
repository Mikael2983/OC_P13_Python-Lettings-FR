"""
Django settings for oc_lettings_site project.

This module contains all the configuration for the Django project, including:
- Paths
- Security settings
- Installed applications
- Middleware
- Templates
- Database
- Authentication
- Internationalization
- Static files

For more information, see:
https://docs.djangoproject.com/en/3.0/topics/settings/
"""

import os
from pathlib import Path

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Hosts/domain names that are valid for this site
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# -------------------------------------------------------------------
# Application definition
# -------------------------------------------------------------------

INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',  # Main project app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings',
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Project-level templates
        ],
        'APP_DIRS': True,  # Look for templates inside app directories
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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# -------------------------------------------------------------------
# Database
# -------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite backend
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}

# -------------------------------------------------------------------
# Password validation
# -------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True   # Enable Django’s translation system
USE_L10N = True   # Enable locale-specific formatting of data
USE_TZ = True     # Enable timezone-aware datetimes

# -------------------------------------------------------------------
# Static files
# -------------------------------------------------------------------

STATIC_URL = '/static/'  # URL to serve static files
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directories with static files for development
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles'),
