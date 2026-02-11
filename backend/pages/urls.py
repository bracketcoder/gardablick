from django.urls import path
from .views import (
    PrivacyPolicyView,
    HomePageView,
    SellPageView,
    ServicePageView,
    AboutPageView,
    ContactPageView,
)


urlpatterns = [
    path("privacy-policy/", PrivacyPolicyView.as_view(), name="api-privacy-policy"),
    path("page/home/", HomePageView.as_view(), name="home-page"),
    path("page/sell/", SellPageView.as_view(), name="sell-page"),
    path("page/services/", ServicePageView.as_view(), name="services-page"),
    path("page/about/", AboutPageView.as_view(), name="about-page"),
    path("page/contact/", ContactPageView.as_view(), name="contact-page"),
]
