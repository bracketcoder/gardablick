import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-gardablick-dev-key-change-in-production"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "translations",
    "properties",
    "contacts",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_ALL_ORIGINS = DEBUG

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.parent / "cms_templates" / "templates",
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR.parent / "cms_templates" / "static",
]

UNFOLD = {
    "SITE_TITLE": "Gardablick",
    "SITE_HEADER": "Gardablick",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            "href": lambda request: "/static/images/favicon.png",
        },
    ],
    "SITE_LOGO": {
        "light": lambda request: "/static/images/full-logo-black.png",
        "dark": lambda request: "/static/images/full-logo-white.png",
    },
    "STYLES": [
        lambda request: "/static/css/admin-custom.css",
    ],
    "SCRIPTS": [
        lambda request: "/static/js/admin-custom.js",
    ],
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": "Content",
                "items": [
                    {
                        "title": "Properties",
                        "icon": "home",
                        "link": lambda request: "/theadmin/properties/property/",
                        "active": lambda request: request.path.startswith("/theadmin/properties/property"),
                    },
                    {
                        "title": "Contact Messages",
                        "icon": "mail",
                        "link": lambda request: "/theadmin/contacts/contactmessage/",
                        "badge": "contacts.admin.unread_count",
                        "active": lambda request: request.path.startswith("/theadmin/contacts/contactmessage"),
                    },
                ],
            },
            {
                "title": "Pages",
                "items": [
                    {
                        "title": "Home",
                        "icon": "home",
                        "link": lambda request: "/theadmin/pages/homepage/1/change/",
                        "active": lambda request: "/pages/homepage" in request.path,
                    },
                    {
                        "title": "Sell",
                        "icon": "sell",
                        "link": lambda request: "/theadmin/pages/sellpage/1/change/",
                        "active": lambda request: "/pages/sellpage" in request.path,
                    },
                    {
                        "title": "Service",
                        "icon": "build",
                        "link": lambda request: "/theadmin/pages/servicepage/1/change/",
                        "active": lambda request: "/pages/servicepage" in request.path,
                    },
                    {
                        "title": "About",
                        "icon": "info",
                        "link": lambda request: "/theadmin/pages/aboutpage/1/change/",
                        "active": lambda request: "/pages/aboutpage" in request.path,
                    },
                    {
                        "title": "Contact",
                        "icon": "contact_page",
                        "link": lambda request: "/theadmin/pages/contactpage/1/change/",
                        "active": lambda request: "/pages/contactpage" in request.path,
                    },
                    {
                        "title": "Privacy Policy",
                        "icon": "policy",
                        "link": lambda request: "/theadmin/pages/privacypolicy/1/change/",
                        "active": lambda request: "/pages/privacypolicy" in request.path,
                    },
                ],
            },
            {
                "title": "Settings",
                "items": [
                    {
                        "title": "Users",
                        "icon": "person",
                        "link": lambda request: "/theadmin/auth/user/",
                        "active": lambda request: request.path.startswith("/theadmin/auth/user"),
                    },
                ],
            },
        ],
    },
}
