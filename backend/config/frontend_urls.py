from django.urls import path
from pages.frontend_views import (
    home_view,
    chi_siamo_view,
    servizi_view,
    vendi_view,
    contatti_view,
    immobili_view,
    privacy_policy_view,
    property_detail_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("chi-siamo/", chi_siamo_view, name="chi-siamo"),
    path("servizi/", servizi_view, name="servizi"),
    path("vendi/", vendi_view, name="vendi"),
    path("contatti/", contatti_view, name="contatti"),
    path("immobili/", immobili_view, name="immobili"),
    path("details/<int:pk>/", property_detail_view, name="property-detail"),
    path("privacy-policy/", privacy_policy_view, name="privacy-policy"),
]
