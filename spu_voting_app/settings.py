from pathlib import Path

import mimetypes

mimetypes.add_type("text/css", ".css", True)

LOGIN_URL = '/login/'

BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = 'base.User'

SECRET_KEY = 'django-insecure-juxr&@^v-iw^#n6o*kpol2b(0v_%$)n5uc6ne!$27wz)tlw=ux'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['spu-voting-app.onrender.com']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'administration_app',
]

JAZZMIN_SETTINGS = {
    "site_title": "SPU VOTING",
    "site_header": "SPU VOTING",
    "site_logo": "images/admin-interface/favicon/spu_logo_1.png",
    "login_logo": 'images/admin-interface/favicon/spu_logo_1.png',
}

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

ROOT_URLCONF = 'spu_voting_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'spu_voting_app.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    '/https://spu-voting-app.onrender.com',
]

MEDIA_ROOT = BASE_DIR / 'static/images'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = "/static/"
