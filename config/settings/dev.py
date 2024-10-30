"""
Development Django settings for config project.
"""

from .common import *
from dotenv import load_dotenv

# Load environment variables from /secrets/.env
SECRETS_DIR = BACKEND_DIR / 'secrets'
SECRETS_PATH = SECRETS_DIR / '.env'
load_dotenv(SECRETS_PATH)

# Secret key
SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-secret-key-for-dev')

# Debug
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST', '').split(',')

# Database configuration for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'portfolio_local'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'econx2024'),
        'HOST': os.getenv('DB_HOST', 'host.docker.internal'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
