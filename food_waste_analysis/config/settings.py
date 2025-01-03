from pathlib import Path

# Ana proje dizinini belirle
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY ayarı (geliştirme için sabit bir anahtar, üretim için değiştirilmeli)
SECRET_KEY = 'django-insecure-please-change-this-key'  # Geliştirme için uygun

# DEBUG ayarı
DEBUG = True  # Geliştirme için açık, üretimde False yapılmalı

# ALLOWED_HOSTS
ALLOWED_HOSTS = []  # Üretimde izin verilen alan adlarını ekleyin

# Uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Projeye özel uygulamalar
    'analysis',
    'users',
]

# Orta katman yazılımları (middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL yönlendirmesi
ROOT_URLCONF = 'config.urls'

# Şablonlar
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI uygulaması
WSGI_APPLICATION = 'config.wsgi.application'

# Veritabanı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Statik dosyalar
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Medya dosyaları
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



# E-posta ayarları
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Üretim için SMTP yapılandırması gereklidir
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Güvenlik ayarları
SESSION_COOKIE_SECURE = False  # Geliştirme için False, üretimde True olmalı
CSRF_COOKIE_SECURE = False  # Geliştirme için False, üretimde True olmalı
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = False
LOGIN_REDIRECT_URL = '/panel/'  # Başarılı giriş sonrası yönlendirme
LOGIN_REDIRECT_URL = '/panel/'  # Başarılı giriş sonrası yönlendirme
