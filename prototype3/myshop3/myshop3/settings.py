"""
Django settings for myshop3 project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django_heroku
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR_R = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../../')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9ubiuy)y7vq+ir4*7a#ov)!db*p#9ts2l6dwvz!9so5m#rmznj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost','188.68.221.224', '188.68.221.224.xip.io']
ALLOWED_HOSTS = ['*']

#'.herokuapp.com'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    'cart',
    'orders',

    'login',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'allauth')],
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

WSGI_APPLICATION = 'myshop3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''
'''DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': "maison_dev",
        'USER': "vladglebovv",
        'PASSWORD': "password",
        'HOST': "db",
        'PORT': "5432",
    }
}'''
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': "de9l00vf0f9rki",
        'USER': "eqnogrnwgiyqjt",
        'PASSWORD': "16bacff6670bff89dfdea9ea1bae6a47350e7e3f4dadd193c71c27b4388a0499",
        'HOST': "ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",
        'PORT': "5432",
    }
}

'''DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='DATABASE_URL')'''

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'

CART_SESSION_ID = 'cart'

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 3

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True
django_heroku.settings(locals())