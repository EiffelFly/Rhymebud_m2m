"""
Django settings for rhymebus_mission project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'll_6@mme89*o#z##q7s_hh7g+wvs0f%8^_or_z*$c@nbi(#1!7'

#When debug is False, you need to provide allowed host
DEBUG = True
ALLOWED_HOSTS = ['enigmatic-spire-36457.herokuapp.com', '127.1.1.0', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    # This make it easier to integrate django templates with bootstrap things.
    'widget_tweaks',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # For dynamic languages
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rhymebusmission.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

import dj_database_url

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    DATABASE_URL = 'postgres://ekeebibvgwckgz:ccbd989e7718709aa9cd1e80af73f4f499c0718f8733ac4b4de97716b1433eea@ec2-34-239-241-25.compute-1.amazonaws.com:5432/d3idmeo4f63tbs'
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

#DATABASES = {
#    'default':{
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME' : 'heroku_7ff375b328a4a5d',
#        'HOST' : 'us-cdbr-east-02.cleardb.com',
#        'PORT' : '3306',
#        'USER' : 'ba362fb71ff9c4',
#        'PASSWORD' : 'bed2cb4f',
#        #'OPTIONS': {'ssl': {'ca':'secret/cleardb-ca.pem', 'cert':'/secret/ba362fb71ff9c4-cert.pem', 'key':'/secret/ba362fb71ff9c4-key.pem'},}
#    }
#}

WSGI_APPLICATION = 'rhymebusmission.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# We disable the most part of AUTH_PASSWORD_VALIDATORS for convinience of users.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# For i18n
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# This limits the set_language view option
LANGUAGES = {
    ('en', ''),
    ('zh-hant', ''),
}

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

MEDIA_URL = '/uploads/'

# build-in auth system

#LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

