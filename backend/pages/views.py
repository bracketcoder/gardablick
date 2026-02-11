from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PrivacyPolicy, HomePage, SellPage, ServicePage, AboutPage, ContactPage


def get_image_url(request, image_field):
    """Get absolute URL for an image field."""
    if image_field and hasattr(image_field, 'url'):
        return request.build_absolute_uri(image_field.url)
    return ""


class PrivacyPolicyView(APIView):
    """Get privacy policy content with language support."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        policy = PrivacyPolicy.load()

        return Response({
            "privacy_title": policy.get_field_translation("privacy_title", lang),
            "data_controller": policy.get_field_translation("data_controller", lang),
            "legal_basis": policy.get_field_translation("legal_basis", lang),
            "data_purposes": policy.get_field_translation("data_purposes", lang),
            "data_sharing": policy.get_field_translation("data_sharing", lang),
            "data_storage": policy.get_field_translation("data_storage", lang),
            "retention_period": policy.get_field_translation("retention_period", lang),
            "user_rights": policy.get_field_translation("user_rights", lang),
            "cookie_title": policy.get_field_translation("cookie_title", lang),
            "cookie_types": policy.get_field_translation("cookie_types", lang),
            "consent_requirements": policy.get_field_translation("consent_requirements", lang),
            "cookies_listed": policy.get_field_translation("cookies_listed", lang),
            "updated_at": policy.updated_at,
        })


class HomePageView(APIView):
    """Get home page content with language support."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        page = HomePage.load()

        return Response({
            "about_section": {
                "subtitle": page.get_field_translation("about_subtitle", lang),
                "heading": page.get_field_translation("about_heading", lang),
                "paragraph1": page.get_field_translation("about_paragraph1", lang),
                "paragraph2": page.get_field_translation("about_paragraph2", lang),
                "image": get_image_url(request, page.about_image),
            },
            "services_section": {
                "subtitle": page.get_field_translation("services_subtitle", lang),
                "heading": page.get_field_translation("services_heading", lang),
                "paragraph1": page.get_field_translation("services_paragraph1", lang),
                "paragraph2": page.get_field_translation("services_paragraph2", lang),
                "image": get_image_url(request, page.services_image),
            },
            "service_icons": [
                {
                    "title": page.get_field_translation("service_icon_1_title", lang),
                    "icon": get_image_url(request, page.service_icon_1_image),
                },
                {
                    "title": page.get_field_translation("service_icon_2_title", lang),
                    "icon": get_image_url(request, page.service_icon_2_image),
                },
                {
                    "title": page.get_field_translation("service_icon_3_title", lang),
                    "icon": get_image_url(request, page.service_icon_3_image),
                },
                {
                    "title": page.get_field_translation("service_icon_4_title", lang),
                    "icon": get_image_url(request, page.service_icon_4_image),
                },
                {
                    "title": page.get_field_translation("service_icon_5_title", lang),
                    "icon": get_image_url(request, page.service_icon_5_image),
                },
            ],
            "updated_at": page.updated_at,
        })


class SellPageView(APIView):
    """Get sell page content with language support."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        page = SellPage.load()

        return Response({
            "intro_section": {
                "subtitle": page.get_field_translation("intro_subtitle", lang),
                "heading": page.get_field_translation("intro_heading", lang),
                "description": page.get_field_translation("intro_description", lang),
                "image": get_image_url(request, page.intro_image),
            },
            "services": [
                {
                    "title": page.get_field_translation("service_1_title", lang),
                    "description": page.get_field_translation("service_1_description", lang),
                    "icon": get_image_url(request, page.service_1_icon),
                },
                {
                    "title": page.get_field_translation("service_2_title", lang),
                    "description": page.get_field_translation("service_2_description", lang),
                    "icon": get_image_url(request, page.service_2_icon),
                },
                {
                    "title": page.get_field_translation("service_3_title", lang),
                    "description": page.get_field_translation("service_3_description", lang),
                    "icon": get_image_url(request, page.service_3_icon),
                },
                {
                    "title": page.get_field_translation("service_4_title", lang),
                    "description": page.get_field_translation("service_4_description", lang),
                    "icon": get_image_url(request, page.service_4_icon),
                },
                {
                    "title": page.get_field_translation("service_5_title", lang),
                    "description": page.get_field_translation("service_5_description", lang),
                    "icon": get_image_url(request, page.service_5_icon),
                },
            ],
            "updated_at": page.updated_at,
        })


class ServicePageView(APIView):
    """Get services page content with language support."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        page = ServicePage.load()

        return Response({
            "services": [
                {
                    "title": page.get_field_translation("service_1_title", lang),
                    "description": page.get_field_translation("service_1_description", lang),
                    "icon": get_image_url(request, page.service_1_icon),
                    "image": get_image_url(request, page.service_1_image),
                },
                {
                    "title": page.get_field_translation("service_2_title", lang),
                    "description": page.get_field_translation("service_2_description", lang),
                    "icon": get_image_url(request, page.service_2_icon),
                    "image": get_image_url(request, page.service_2_image),
                },
                {
                    "title": page.get_field_translation("service_3_title", lang),
                    "description": page.get_field_translation("service_3_description", lang),
                    "icon": get_image_url(request, page.service_3_icon),
                    "image": get_image_url(request, page.service_3_image),
                },
                {
                    "title": page.get_field_translation("service_4_title", lang),
                    "description": page.get_field_translation("service_4_description", lang),
                    "icon": get_image_url(request, page.service_4_icon),
                    "image": get_image_url(request, page.service_4_image),
                },
                {
                    "title": page.get_field_translation("service_5_title", lang),
                    "description": page.get_field_translation("service_5_description", lang),
                    "icon": get_image_url(request, page.service_5_icon),
                    "image": get_image_url(request, page.service_5_image),
                },
            ],
            "updated_at": page.updated_at,
        })


class AboutPageView(APIView):
    """Get about page content with language support."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        page = AboutPage.load()

        return Response({
            "agency_section": {
                "subtitle": page.get_field_translation("agency_subtitle", lang),
                "heading": page.get_field_translation("agency_heading", lang),
                "paragraph1": page.get_field_translation("agency_paragraph1", lang),
                "paragraph2": page.get_field_translation("agency_paragraph2", lang),
                "image": get_image_url(request, page.agency_image),
            },
            "team_members": [
                {
                    "name": page.team_member_1_name,
                    "title": page.get_field_translation("team_member_1_title", lang),
                    "image": get_image_url(request, page.team_member_1_image),
                },
                {
                    "name": page.team_member_2_name,
                    "title": page.get_field_translation("team_member_2_title", lang),
                    "image": get_image_url(request, page.team_member_2_image),
                },
            ],
            "updated_at": page.updated_at,
        })


class ContactPageView(APIView):
    """Get contact page content with language support. Also used by Footer."""

    def get(self, request):
        lang = request.query_params.get("lang", "it")
        if lang not in ("it", "en", "de"):
            lang = "it"

        page = ContactPage.load()

        return Response({
            "company_name": page.company_name,
            "description": page.get_field_translation("description", lang),
            "address": {
                "building": page.address_building,
                "street": page.address_street,
                "city": page.address_city,
            },
            "contact": {
                "phone_1": page.phone_1,
                "phone_2": page.phone_2,
                "email": page.email,
                "whatsapp_number": page.whatsapp_number,
            },
            "map_embed_url": page.map_embed_url,
            "social_links": {
                "whatsapp": page.social_whatsapp,
                "instagram": page.social_instagram,
                "facebook": page.social_facebook,
                "linkedin": page.social_linkedin,
            },
            "updated_at": page.updated_at,
        })
