"""
Django settings for datsegit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'photologue',
    'datsegit',
    'twhst'
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'datsegit.urls'

WSGI_APPLICATION = 'datsegit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'eu'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.env.get('DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.env.get('DATABASE_USER', ''),
        'PASSWORD': os.env.get('DATABASE_PASSWORD', ''),
        'HOST': os.env.get('DATABASE_HOST', ''),
        'PORT': os.env.get('DATABASE_PORT', ''),
    }
}

TWITTER_CONSUMER_KEY = os.env.get('TWITTER_CONSUMER_KEY', '') 
TWITTER_CONSUMER_SECRET = os.env.get('TWITTER_CONSUMER_SECRET', '')

SECRET_KEY = os.env.get('SECRET_KEY', '')
