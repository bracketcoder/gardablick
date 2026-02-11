from django.shortcuts import render
from .models import PrivacyPolicy


def get_lang(request):
    """Get language from query param or cookie, default to 'it'."""
    lang = request.GET.get("lang") or request.COOKIES.get("django_language", "it")
    return lang if lang in ("it", "en", "de") else "it"


def home_view(request):
    return render(request, "index.html")


def chi_siamo_view(request):
    return render(request, "chi-siamo.html")


def servizi_view(request):
    return render(request, "servizi.html")


def vendi_view(request):
    return render(request, "vendi.html")


def contatti_view(request):
    return render(request, "contatti.html")


def immobili_view(request):
    return render(request, "immobili.html")


def property_detail_view(request, pk):
    return render(request, "property-detail.html", {"property_id": pk})


def privacy_policy_view(request):
    lang = get_lang(request)
    policy = PrivacyPolicy.load()

    data_purposes = policy.get_field_translation("data_purposes", lang)
    cookie_types = policy.get_field_translation("cookie_types", lang)

    context = {
        "privacy_title": policy.get_field_translation("privacy_title", lang),
        "data_controller": policy.get_field_translation("data_controller", lang),
        "legal_basis": policy.get_field_translation("legal_basis", lang),
        "data_purposes_list": [
            line.strip() for line in data_purposes.split("\n") if line.strip()
        ],
        "data_sharing": policy.get_field_translation("data_sharing", lang),
        "data_storage": policy.get_field_translation("data_storage", lang),
        "retention_period": policy.get_field_translation("retention_period", lang),
        "user_rights": policy.get_field_translation("user_rights", lang),
        "cookie_title": policy.get_field_translation("cookie_title", lang),
        "cookie_types_list": [
            line.strip() for line in cookie_types.split("\n") if line.strip()
        ],
        "consent_requirements": policy.get_field_translation("consent_requirements", lang),
        "cookies_listed": policy.get_field_translation("cookies_listed", lang),
    }
    return render(request, "privacy-policy.html", context)
