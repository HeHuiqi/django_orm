
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'myapp.apps.MyAppConfig'
]
TEMPLATES = []
LANGUAGES_BIDI = []

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True
LANGUAGES = [
    ("en", 'English'),
    ('zh-hans', 'Simplified Chinese'),
]
LOCALE_PATHS = []
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DEFAULT_AUTO_FIELD =  'django.db.models.BigAutoField'

DATABASE_ROUTERS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_INDEX_TABLESPACE = ''

LOGGING_CONFIG = ''
LOGGING = []
FORCE_SCRIPT_NAME = ''

DEFAULT_TABLESPACE = 4
ABSOLUTE_URL_OVERRIDES = {}

CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
CSRF_TRUSTED_ORIGINS = []
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
SILENCED_SYSTEM_CHECKS = []

MIGRATION_MODULES = {}
AUTH_USER_MODEL = 'auth.User'