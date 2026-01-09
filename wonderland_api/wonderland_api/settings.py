from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'portfolio-ywk1.onrender.com',  
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'corsheaders', 
    'wonderland', 
    'chatbot',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'wonderland_api.urls'

TEMPLATES = []

WSGI_APPLICATION = 'wonderland_api.wsgi.application'

DATABASES = {}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

CORS_ALLOWED_ORIGINS = [
  "https://kellytan-portfolio.vercel.app",
  "http://localhost:8080"
]