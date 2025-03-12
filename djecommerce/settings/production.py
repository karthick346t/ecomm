from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['ecomm-production-8ee1.up.railway.app']
LOGGING_CONFIG = None

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_in_env")]

 # Override to prevent conflicts

WHITENOISE_MANIFEST_STRICT = False  # Avoids errors if files are missing

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY', default='your-default-public-key')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY', default='your-default-secret-key')

CSRF_TRUSTED_ORIGINS = ["https://ecomm-production-8ee1.up.railway.app"]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
WHITENOISE_ALLOW_ALL_ORIGINS = True
import mimetypes
mimetypes.add_type("image/jpeg", ".jpg", True)
mimetypes.add_type("image/png", ".png", True)
