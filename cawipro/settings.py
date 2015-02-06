"""
Django settings for cawipro project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def contains(str, substr):
    if str.find(substr) != -1:
        return True
    else:
        return False

if contains(socket.gethostname(), 'webfaction'):
    LIVEHOST = True
else:
    LIVEHOST = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z-z5ku3k87j!ygt)$4@5+q2*p#yktnx)3@kno8i-c2m(y-#5vq'

# SECURITY WARNING: don't run with debug turned on in production!
ADMINS = (
    ('Vincenzo Petrungaro', 'vincenzo.petrungaro@tiesi.it'),
)
MANAGERS = ADMINS

DEBUG = True

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
    'cawi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cawipro.urls'

WSGI_APPLICATION = 'cawipro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'it-IT'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

# Absolute path to the media directory

#LOGIN_REDIRECT_URL = '/'
#LOGIN_URL = '/login/'
#LOGOUT_URL = '/logout/'

"""
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
"""

if LIVEHOST:
    """
    Configurazione di Produzione
    """
    import secrets

    DEBUG = False
    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = [
        'tiesiweb.webfactional.com',
        'ex.tiesiweb.webfactional.com',
        ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': secrets.DATABASE_NAME,
            'USER': secrets.DATABASE_USER,
            'PASSWORD': secrets.DATABASE_PASSWORD,
            'HOST': '',
            'PORT': '',
            'ATOMIC_REQUESTS': True,
            }
    }

    """
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'unix:/home/username/memcached_proiezioni.sock',
            }
    }
    """
    STATIC_URL = '/static/'
    STATIC_ROOT = '/home/tiesiweb/webapps/cawi_static/'
    #MEDIA_URL = '/media/'
    #MEDIA_ROOT = '/home/tiesi/webapps/proiezioni_media/'
    #MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
else:
    """
    Configurazione di Sviluppo
    """
    DEBUG = True
    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ATOMIC_REQUESTS': True,
            }
    }
    STATIC_URL = '/static/'
    #MEDIA_URL = '/media/'
    #MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
    #INSTALLED_APPS += ('debug_toolbar.apps.DebugToolbarConfig',)
    #MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
