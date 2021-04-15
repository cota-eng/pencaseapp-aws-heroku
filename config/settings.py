import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import environ
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'pencaseapp.apps.PencaseappConfig',
    'blog.apps.BlogConfig',
    'django_cleanup.apps.CleanupConfig',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'rest_auth',
    # 'rest_auth.registration',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'storages',
    'imagekit',
    'markdownx',
    # 'debug_toolbar',

]
AUTHENTICATION_BACKENDS = [
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
]
# django-contrib.sites
SITE_ID = 1

# set for users
LOGIN_URL = "accounts:account_login"
LOGIN_REDIRECT_URL = "pencaseapp:home"
LOGOUT_REDIRECT_URL = "accounts:account_login"

# ckeditor settings
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold','Underline'],
#             ['NumberedList', 'BulletedList'],
#         ],
#         'width':'auto'
#     }
# }



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware', 

]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db(),
}

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

# for email backend
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = DEFAULT_FROM_EMAIL  = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
"""Use Custom User"""
ACCOUNT_FORMS = {'signup': 'accounts.forms.SignupCustomForm'}
AUTH_USER_MODEL = "accounts.CustomUser"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

DEBUG = False
ALLOWED_HOSTS = ['localhost','127.0.0.1','pencaseapp.herokuapp.com']

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
#                        'pathname=%(pathname)s lineno=%(lineno)s '
#                        'funcname=%(funcName)s %(message)s'),
#             'datefmt': '%Y-%m-%d %H:%M:%S'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         }
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': 'host',
        'PORT': '',
    }
}
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.toc',
    'markdown.extensions.sane_lists',
]

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)
# not need for using aws 
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TOOLBAR_CALLBACK': True,
#     'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
#     'HIDE_DJANGO_SQL': False,
#     'TAG': 'div',
#     'ENABLE_STACKTRACES' : True,
# }

try:
    from .local_settings import *
except ImportError:
    pass


if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_LOCATION = 'static'
    AWS_DEFAULT_ACL = None
    AWS_DEFAULT_ACL = None

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    # STATICFILES_DIRS = (
    #     [
    #         os.path.join(BASE_DIR, "static"),
    #     ]
    # )
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # AWS_S3_FILE_OVERWRITE = True
    AWS_S3_SECURE_URLS = True
    # AWS_QUERYSTRING_AUTH = False
    # AWS_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
