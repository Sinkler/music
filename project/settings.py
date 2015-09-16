import os

ADMINS = ()
MANAGERS = ADMINS
ALLOWED_HOSTS = ['localhost']

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
STORAGE_ROOT = os.path.join(PROJECT_ROOT, '..', '..', 'storage')

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'common',
)

MEDIA_ROOT = os.path.join(STORAGE_ROOT, 'project', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(STORAGE_ROOT, 'project', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'project', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'yw+5r#gx*r4f3523+gpwy@g94j5l6kb5v2e5=dh_!@#^!ru2x'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SESSION_COOKIE_AGE = 473040000
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'project', 'templates'),
)
if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

###########################
# APPLICATION SETTINGS
###########################

LASTFM_API_KEY = 'c6a5004e0c7371b8d8e1cf7d83d916bb'
LASTFM_API_SECRET = 'db53ba293c9998f954c9ce040dd65a66'
LASTFM_USER = 'sinkler91'
LASTFM_MIN_PLAY_COUNT = 10
MB_RELEASE_TYPES = ['album', 'ep', 'live', 'compilation']
MB_RELEASE_STATUSES = ['official']
MB_APP = 'sinkler'
MB_VERSION = '0.1'
MB_CONTACT = 'sinkler@sinkler.ru'

###########################
# LOCAL SETTINGS
###########################
try:
    import types
    import local_settings
    for key in dir(local_settings):
        value = getattr(local_settings, key)
        if not key.startswith('__') and not isinstance(value, types.ModuleType):
            globals()[key] = value
except ImportError:
    pass
