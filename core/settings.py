"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-2co-vb@oh09op=o3z$c!r!#b2)q4h6gqie*%0ug#k*kmyupifs'

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ['*', '127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'blog',
    'accounts',
    'ckeditor',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'home'),
            os.path.join(BASE_DIR,'blog'),
            os.path.join(BASE_DIR,'accounts'),
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database SQLite
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Fly Postgres Deployment inside app organization - on cloud prod
# DATABASES = {
#     'default': dj_database_url.parse('postgres://aashutosh:mPZlNBxjMbf64bT@top2.nearest.of.aashu-postgres.internal:5432/aashutosh?sslmode=disable', 
#         conn_max_age=600)
# }

# Fly Postgres Deployment local / outside app organization - on cloud
# DATABASES = {
#     'default': dj_database_url.parse('postgres://aashutosh:mPZlNBxjMbf64bT@149.248.216.128:5432/aashutosh?sslmode=disable', 
#         conn_max_age=600)
# }

# Cockroach lab Postgres DB
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ['DATABASE_URL'], 
#         engine='django_cockroachdb'
#         )
# }

# Cockroach PostgreSQL DB Connection Details
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_cockroachdb',
#         'NAME': 'bronze-civet-1481.defaultdb',
#         'USER': 'aashutosh',
#         'PASSWORD': 'Hn4uz6U1QpVC-snPw4t6Rg',
#         'HOST': 'bronze-civet-1481.7s5.cockroachlabs.cloud',
#         'PORT': '26257',
#         'OPTIONS': {
#             'sslmode': 'verify-full',
#             'sslrootcert': os.path.join(BASE_DIR, "cockroach_db", "root.crt"),
#             # 'sslmode': 'disable',
#             # 'sslcert': os.path.join(BASE_DIR, "cockroach_db", "root.crt"),
#             #'sslrootcert': '/certs/ca.crt',
#             # Either sslcert and sslkey (below) or PASSWORD (above) is
#             # required.
#             #'sslcert': '/certs/client.myprojectuser.crt',
#             #'sslkey': '/certs/client.myprojectuser.key',
#             # If applicable
#             #'options': '--cluster={routing-id}',
#         },
#     }
# }

'''
Flyctl Postgres aashu-postgres attached to aashutosh.fly.dev 
flyctl postgres attach --app aashutosh aashu-postgres
DATABASE_URL=postgres://aashutosh:mPZlNBxjMbf64bT@top2.nearest.of.aashu-postgres.internal:5432/aashutosh?sslmode=disable
aashu-postgres.internal=149.248.216.128
'''
# FLy Postgres DB aashu-postgres attached to aashu.fly.dev app
# DATABASES = {
#     'default': dj_database_url.parse('postgres://postgres:yMuTailSsIzS9RG@149.248.216.128:5432/aashu-postgres', 
#         conn_max_age=600)
#     }


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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Whitenoise to server static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = "/blog/"
LOGOUT_REDIRECT_URL = "/blog/"



CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev','https://*.127.0.0.1']