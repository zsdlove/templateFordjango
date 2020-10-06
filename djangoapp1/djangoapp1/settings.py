# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# django-rq配置,setting中的配置
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',  # redis地址
        'PORT': 6379, # redis端括号
        'DB': 10, # 使用的是哪个redis db
        #'PASSWORD': '123456', #redis 密码
        'DEFAULT_TIMEOUT': 360, # 此队列中任务的超时时间
    },
    'with-sentinel': {
        'SENTINELS': [('localhost', 26736), ('localhost', 26737)],
        'MASTER_NAME': 'redismaster',
        'DB': 10,
        #'PASSWORD': '123456',
        'SOCKET_TIMEOUT': None,
        'CONNECTION_KWARGS': {
            'socket_connect_timeout': 0.3
        },
    },
    'high': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 10,
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 10,
    }
}
RQ_EXCEPTION_HANDLERS= [] # 定义自定义异常处理函数

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '36a9b0(dk98)f4t^=aan=jv0d4=)uhz@2po9317lda)k*pv6i4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rq',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoapp1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['frontend/dist'],
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

WSGI_APPLICATION = 'djangoapp1.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/static"),
]

STATIC_URL = '/static/'
