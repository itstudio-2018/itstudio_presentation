
"""
Django settings for it_presentation project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-c=27(ki&y2m=b4(-*^tr5@)_a!t8ez=kynv1op*0%he8q=wbr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'show',
    'join',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'it_presentation.middleware.MobileDetectionMiddleware',
]

ROOT_URLCONF = 'it_presentation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
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

WSGI_APPLICATION = 'it_presentation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pre',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [
#    'static',
#    ]
STATIC_ROOT=os.path.join(BASE_DIR,"static1/").replace('\\', '/')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static/').replace('\\', '/'),
 )

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')







EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '15563709699@163.com'
EMAIL_HOST_PASSWORD = 'it2018'
EMAIL_USE_SSL = True
EMAIL_FROM = '15563709699@163.com'

#CACHES = {
#    "default": {
#    	"BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": "redis://127.0.0.1:6379",
#        "OPTIONS": {
#        "CLIENT_CLASS": "django_redis.client.DefaultClient",
#        "CONNECTION_POOL_KWARGS": {"max_connections": 100}}}}　　

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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



BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切换文件当达到最大大小
            'filename': os.path.join(BASE_LOG_DIR, 'debug.log').replace('\\', '/'),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'encoding': 'UTF-8',
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切换文件当达到最大大小
            'filename': os.path.join(BASE_LOG_DIR, 'warning.log').replace('\\', '/'),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'encoding': 'UTF-8',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'info.log').replace('\\', '/'),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'encoding': 'UTF-8',
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d]'+
                      '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'warning': {
            'handlers': ['warning_file',],
            'level': 'WARNING',
            'propagate': True,
        },
        'info': {
            'handlers': ['info_file', ],
            'level': 'INFO',
            'propagate': False,
        }
    }
}


ALLOWED_OSTS = ["*"]
