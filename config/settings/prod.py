"""
Production Django settings for config project.
"""

from .common import *
import dj_database_url

# Secret key
SECRET_KEY = os.getenv('SECRET_KEY')

# Debug
DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

# Allowed hosts
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# CORS
CORS_ORIGIN_ALLOW_ALL = os.getenv('CORS_ORIGIN_ALLOW_ALL', 'False').lower() in ['true', '1', 't']
if not CORS_ORIGIN_ALLOW_ALL:
    CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST', '').split(',')

# Database configuration for Heroku
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
