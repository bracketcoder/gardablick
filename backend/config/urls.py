from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("theadmin/", admin.site.urls),
    path("api/", include("translations.urls")),
    path("api/", include("properties.urls")),
    path("api/", include("contacts.urls")),
    path("api/", include("pages.urls")),
    # Frontend page routes
    path("", include("config.frontend_urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
