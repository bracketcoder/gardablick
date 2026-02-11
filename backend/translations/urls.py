from django.urls import path
from . import views

urlpatterns = [
    path("translations/<str:locale>/", views.get_translations, name="get_translations"),
]
