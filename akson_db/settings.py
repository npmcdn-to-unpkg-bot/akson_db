"""
Django settings for akson_db project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
AKSON_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(AKSON_DIR)

DEBUG = False

ADMINS = (
    ('Grzegorz Terlikowski', 'terlikowski.grzegorz@gmail.com'),
)

MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c$2m5q@le+42ifs2=+)nv7xs_)5jm0m!3)mckva9n5=a1yo%x&'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en//ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']  # TODO should be changed to proper thing

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = "".join([BASE_DIR, '/media'])
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = "".join([BASE_DIR, '/static'])
STATIC_URL = '/static/'

# Application definition

SUPERVISED_APPS = [
    'neurorehabilitation_card',
    'gait_reeducation_card',
    'massage_reflexology_card',
    'physiotherapy_card',
    'track_gait_training',
    'upper_limb_study',
    'upper_limb_therapy',
    'metric_card',
    'neurophysiological_study',
    'dynamometry_card',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'easy_select2',
    'patient',
    'neurorehabilitation_card',
    'gait_reeducation_card',
    'massage_reflexology_card',
    'physiotherapy_card',
    'time_spread',
    'track_gait_training',
    'upper_limb_study',
    'upper_limb_therapy',
    'metric_card',
    'treatment_record',
    'neurophysiological_study',
    'dynamometry_card',
    'therapy_program',
    'supervision',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOCALE_PATHS = [AKSON_DIR + '/locale', ]

ROOT_URLCONF = 'akson_db.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'akson_db.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.getenv('DB_NAME') or 'akson_prod',  # Or path to database file if using sqlite3.
        'USER': os.getenv('DB_USER'),  # Not used with sqlite3.
        'PASSWORD': os.getenv('DB_PASS'),  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

if 'RDS_HOSTNAME' in os.environ: # AWS environment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

U_LOGFILE_NAME = '/var/log/akson_db.log'
U_LOGFILE_SIZE = 10 * 1024 * 1024
U_LOGFILE_COUNT = 10
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': U_LOGFILE_NAME,
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
