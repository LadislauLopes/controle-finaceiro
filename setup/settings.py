from pathlib import Path
import os

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança e configurações do Django
SECRET_KEY = 'django-insecure-=+#0dw+ktuflxxqs3p&=8bshu#ca4*b966j215l9z!4!e9nxu@'

# Modo de desenvolvimento (em produção, deve ser False)
DEBUG = True

# Definir os hosts permitidos (ajuste conforme necessário)
ALLOWED_HOSTS = []

# Definir os apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'central',  # Seu app
]

# Middleware da aplicação
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL de raiz e configurações de URLs
ROOT_URLCONF = 'setup.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório de templates
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

# WSGI e outros arquivos de configuração
WSGI_APPLICATION = 'setup.wsgi.application'

# Banco de dados (SQLite por padrão)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de Senha
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

# Internacionalização
LANGUAGE_CODE = 'en-us'  # Pode ser 'pt-br' ou outro idioma
TIME_ZONE = 'UTC'  # Altere conforme necessário, por exemplo, 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos (CSS, JavaScript, Imagens)
STATIC_URL = '/static/'  # URL onde os arquivos estáticos serão acessados no navegador
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Diretório de arquivos estáticos no nível do projeto
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Onde os arquivos estáticos serão coletados em produção

# Configurações de arquivos de mídia (uploads de usuários)
MEDIA_URL = '/media/'  # URL onde os arquivos de mídia serão acessados
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório onde os arquivos de mídia serão armazenados

# Modelo de chave primária para tabelas (caso queira mudar o comportamento padrão)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de segurança (adicionais)
SECURE_SSL_REDIRECT = False  # Defina como True em produção, se usando HTTPS
CSRF_COOKIE_SECURE = False  # Defina como True em produção
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email (configuração mínima para desenvolvimento)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Definir as rotas de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definir o idioma padrão do site
LANGUAGE_CODE = 'en-us'  # Pode mudar para 'pt-br' ou outro idioma

# Definir o fuso horário
TIME_ZONE = 'UTC'  # Alterar para o fuso horário desejado, ex: 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True
USE_TZ = True
