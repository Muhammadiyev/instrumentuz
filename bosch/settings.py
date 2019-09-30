import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'comments.apps.CommentsConfig',
    'dictionary.apps.DictionaryConfig',
    'instruments.apps.InstrumentsConfig',
    'company.apps.CompanyConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bosch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'bosch.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

CRISTY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = '/mediafiles/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [
#     "http://starinstrument.uz",
#     "http://194.67.78.26",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000"
# ]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
