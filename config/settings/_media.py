from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'media/templates/'],
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

# https://docs.djangoproject.com/en/5.1/ref/settings/#static-files
STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATIC_URL = 'media/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'media/static/'
]

MEDIA_ROOT = BASE_DIR / 'media/uploads/'
MEDIA_URL = 'media/uploads/'