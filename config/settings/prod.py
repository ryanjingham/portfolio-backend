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

CSRF_TRUSTED_ORIGINS = [
    'https://rji-portfolio-backend-126d5f0ba5b9.herokuapp.com',
    'https://rji.software',
    'https://rji-portfolio-frontend-47ca0c27036c.herokuapp.com',
    'http://localhost:3000',
    'http://localhost:8000',
]

# Database configuration for Heroku
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
