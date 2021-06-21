from .base import *
import environ

environ.Env.read_env()
env = environ.Env(
    DEBUG=(bool, False)
)

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

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

DATABASES = {
    'default': env.db(),
}

# cookies secure
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE')
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE')

# redirects all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT')

# HTTP(Strict Transport Security) - HSTS - set in STS header:
SECURE_HSTS_SECONDS = env.bool('SECURE_HSTS_SECONDS')
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS')
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD')

# The file storage engine to use when collecting static files with the collectstatic management command.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'





