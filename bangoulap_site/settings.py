"""
Django settings for bangoulap_site project.
Adapté pour DEBUG=False sur Render et DEBUG=True en local.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# DEBUG & SECRET
# ========================
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-u6&p#o!x@z@3xk=3)j#s6g!%qz$7)vbk=+f)6$#gp99+0fn4k="
)

# ========================
# ALLOWED HOSTS
# ========================
if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
else:
    ALLOWED_HOSTS = ["bangoulap-site.onrender.com"]  # 🔄 Ton domaine Render

# ========================
# APPS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'core',
    'culture',
    'histoire',
    'personnalites',
    'projets',
    'actualites',
    'galerie',
    'CODEBA',
    'dons',
    'associations',
    'contact',
    'widget_tweaks',
    'admin_custom',
    'django.contrib.humanize',
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

# ========================
# LANGUES
# ========================
LANGUAGES = [
    ('fr', 'Français'),
    ('med', 'Medumba'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # sert les statics en prod
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bangoulap_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'bangoulap_site.wsgi.application'

# ========================
# DATABASES
# ========================
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("POSTGRES_DB", "postgres"),
            'USER': os.getenv("POSTGRES_USER", "postgres"),
            'PASSWORD': os.getenv("POSTGRES_PASSWORD", ""),
            'HOST': os.getenv("POSTGRES_HOST", "localhost"),
            'PORT': os.getenv("POSTGRES_PORT", "5432"),
        }
    }

# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# EMAIL
# ========================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "ketchadjiguymartial@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "yrvc qolj uoqx bqvu")
DEFAULT_FROM_EMAIL = 'Bangoulap <ketchadjiguymartial@gmail.com>'
ADMINS = [("Martial", "ketchadjiguymartial@gmail.com")]

# ========================
# INTERNATIONALISATION
# ========================
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Africa/Douala'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ========================
# STATIC & MEDIA
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # fichiers en dev
STATIC_ROOT = BASE_DIR / 'staticfiles'    # pour prod collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# AUTHENTIFICATION
# ========================
LOGIN_URL = '/admin-custom/login/'
LOGIN_REDIRECT_URL = '/admin-custom/dashboard/'
LOGOUT_REDIRECT_URL = '/'
CSRF_FAILURE_VIEW = 'admin_custom.views.custom_permission_denied_view'

# ========================
# AUTRES OPTIONS
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========================
# SÉCURITÉ EN PROD
# ========================
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
