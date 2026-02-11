import json
from pathlib import Path
from django.http import JsonResponse


LOCALES_DIR = Path(__file__).resolve().parent / "locales"
SUPPORTED_LOCALES = {"en", "it", "de"}


def get_translations(request, locale):
    if locale not in SUPPORTED_LOCALES:
        return JsonResponse({"error": f"Unsupported locale: {locale}"}, status=400)

    locale_file = LOCALES_DIR / f"{locale}.json"
    if not locale_file.exists():
        return JsonResponse({"error": f"Locale file not found: {locale}"}, status=404)

    with open(locale_file, "r", encoding="utf-8") as f:
        translations = json.load(f)

    return JsonResponse(translations)
