from django.contrib import admin
from django import forms
from django.db import models
from unfold.admin import ModelAdmin
from .models import PrivacyPolicy, HomePage, SellPage, ServicePage, AboutPage, ContactPage


class JSONTextareaWidget(forms.Textarea):
    """Custom textarea widget for JSON fields with better display."""
    def __init__(self, attrs=None):
        default_attrs = {
            'rows': 6,
            'style': 'font-family: monospace; width: 100%;',
            'placeholder': '{"it": "Italian text", "en": "English text", "de": "German text"}'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class SingletonAdmin(ModelAdmin):
    """Base admin class for singleton models."""

    formfield_overrides = {
        models.JSONField: {'widget': JSONTextareaWidget},
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("About Section - Subtitle (IT / EN / DE)", {
            "fields": ("about_subtitle",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("About Section - Heading (IT / EN / DE)", {
            "fields": ("about_heading",),
            "classes": ("wide",),
        }),
        ("About Section - Paragraph 1 (IT / EN / DE)", {
            "fields": ("about_paragraph1",),
            "classes": ("wide",),
        }),
        ("About Section - Paragraph 2 (IT / EN / DE)", {
            "fields": ("about_paragraph2",),
            "classes": ("wide",),
        }),
        ("About Section - Image", {
            "fields": ("about_image",),
            "classes": ("wide",),
        }),
        ("Services Section - Subtitle (IT / EN / DE)", {
            "fields": ("services_subtitle",),
            "classes": ("wide",),
        }),
        ("Services Section - Heading (IT / EN / DE)", {
            "fields": ("services_heading",),
            "classes": ("wide",),
        }),
        ("Services Section - Paragraph 1 (IT / EN / DE)", {
            "fields": ("services_paragraph1",),
            "classes": ("wide",),
        }),
        ("Services Section - Paragraph 2 (IT / EN / DE)", {
            "fields": ("services_paragraph2",),
            "classes": ("wide",),
        }),
        ("Services Section - Image", {
            "fields": ("services_image",),
            "classes": ("wide",),
        }),
        ("Service Icon 1", {
            "fields": ("service_icon_1_title", "service_icon_1_image"),
            "classes": ("wide",),
        }),
        ("Service Icon 2", {
            "fields": ("service_icon_2_title", "service_icon_2_image"),
            "classes": ("wide",),
        }),
        ("Service Icon 3", {
            "fields": ("service_icon_3_title", "service_icon_3_image"),
            "classes": ("wide",),
        }),
        ("Service Icon 4", {
            "fields": ("service_icon_4_title", "service_icon_4_image"),
            "classes": ("wide",),
        }),
        ("Service Icon 5", {
            "fields": ("service_icon_5_title", "service_icon_5_image"),
            "classes": ("wide",),
        }),
    )


@admin.register(SellPage)
class SellPageAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("Intro Section - Subtitle (IT / EN / DE)", {
            "fields": ("intro_subtitle",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("Intro Section - Heading (IT / EN / DE)", {
            "fields": ("intro_heading",),
            "classes": ("wide",),
        }),
        ("Intro Section - Description (IT / EN / DE)", {
            "fields": ("intro_description",),
            "classes": ("wide",),
        }),
        ("Intro Section - Image", {
            "fields": ("intro_image",),
            "classes": ("wide",),
        }),
        ("Service 1 - Title (IT / EN / DE)", {
            "fields": ("service_1_title",),
            "classes": ("wide",),
        }),
        ("Service 1 - Description (IT / EN / DE)", {
            "fields": ("service_1_description",),
            "classes": ("wide",),
        }),
        ("Service 1 - Icon", {
            "fields": ("service_1_icon",),
            "classes": ("wide",),
        }),
        ("Service 2 - Title (IT / EN / DE)", {
            "fields": ("service_2_title",),
            "classes": ("wide",),
        }),
        ("Service 2 - Description (IT / EN / DE)", {
            "fields": ("service_2_description",),
            "classes": ("wide",),
        }),
        ("Service 2 - Icon", {
            "fields": ("service_2_icon",),
            "classes": ("wide",),
        }),
        ("Service 3 - Title (IT / EN / DE)", {
            "fields": ("service_3_title",),
            "classes": ("wide",),
        }),
        ("Service 3 - Description (IT / EN / DE)", {
            "fields": ("service_3_description",),
            "classes": ("wide",),
        }),
        ("Service 3 - Icon", {
            "fields": ("service_3_icon",),
            "classes": ("wide",),
        }),
        ("Service 4 - Title (IT / EN / DE)", {
            "fields": ("service_4_title",),
            "classes": ("wide",),
        }),
        ("Service 4 - Description (IT / EN / DE)", {
            "fields": ("service_4_description",),
            "classes": ("wide",),
        }),
        ("Service 4 - Icon", {
            "fields": ("service_4_icon",),
            "classes": ("wide",),
        }),
        ("Service 5 - Title (IT / EN / DE)", {
            "fields": ("service_5_title",),
            "classes": ("wide",),
        }),
        ("Service 5 - Description (IT / EN / DE)", {
            "fields": ("service_5_description",),
            "classes": ("wide",),
        }),
        ("Service 5 - Icon", {
            "fields": ("service_5_icon",),
            "classes": ("wide",),
        }),
    )


@admin.register(ServicePage)
class ServicePageAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("Service 1 - Title (IT / EN / DE)", {
            "fields": ("service_1_title",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("Service 1 - Description (IT / EN / DE)", {
            "fields": ("service_1_description",),
            "classes": ("wide",),
        }),
        ("Service 1 - Icon & Image", {
            "fields": ("service_1_icon", "service_1_image"),
            "classes": ("wide",),
        }),
        ("Service 2 - Title (IT / EN / DE)", {
            "fields": ("service_2_title",),
            "classes": ("wide",),
        }),
        ("Service 2 - Description (IT / EN / DE)", {
            "fields": ("service_2_description",),
            "classes": ("wide",),
        }),
        ("Service 2 - Icon & Image", {
            "fields": ("service_2_icon", "service_2_image"),
            "classes": ("wide",),
        }),
        ("Service 3 - Title (IT / EN / DE)", {
            "fields": ("service_3_title",),
            "classes": ("wide",),
        }),
        ("Service 3 - Description (IT / EN / DE)", {
            "fields": ("service_3_description",),
            "classes": ("wide",),
        }),
        ("Service 3 - Icon & Image", {
            "fields": ("service_3_icon", "service_3_image"),
            "classes": ("wide",),
        }),
        ("Service 4 - Title (IT / EN / DE)", {
            "fields": ("service_4_title",),
            "classes": ("wide",),
        }),
        ("Service 4 - Description (IT / EN / DE)", {
            "fields": ("service_4_description",),
            "classes": ("wide",),
        }),
        ("Service 4 - Icon & Image", {
            "fields": ("service_4_icon", "service_4_image"),
            "classes": ("wide",),
        }),
        ("Service 5 - Title (IT / EN / DE)", {
            "fields": ("service_5_title",),
            "classes": ("wide",),
        }),
        ("Service 5 - Description (IT / EN / DE)", {
            "fields": ("service_5_description",),
            "classes": ("wide",),
        }),
        ("Service 5 - Icon & Image", {
            "fields": ("service_5_icon", "service_5_image"),
            "classes": ("wide",),
        }),
    )


@admin.register(AboutPage)
class AboutPageAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("Agency Section - Subtitle (IT / EN / DE)", {
            "fields": ("agency_subtitle",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("Agency Section - Heading (IT / EN / DE)", {
            "fields": ("agency_heading",),
            "classes": ("wide",),
        }),
        ("Agency Section - Paragraph 1 (IT / EN / DE)", {
            "fields": ("agency_paragraph1",),
            "classes": ("wide",),
        }),
        ("Agency Section - Paragraph 2 (IT / EN / DE)", {
            "fields": ("agency_paragraph2",),
            "classes": ("wide",),
        }),
        ("Agency Section - Image", {
            "fields": ("agency_image",),
            "classes": ("wide",),
        }),
        ("Team Member 1 - Name", {
            "fields": ("team_member_1_name",),
            "classes": ("wide",),
        }),
        ("Team Member 1 - Title (IT / EN / DE)", {
            "fields": ("team_member_1_title",),
            "classes": ("wide",),
        }),
        ("Team Member 1 - Image", {
            "fields": ("team_member_1_image",),
            "classes": ("wide",),
        }),
        ("Team Member 2 - Name", {
            "fields": ("team_member_2_name",),
            "classes": ("wide",),
        }),
        ("Team Member 2 - Title (IT / EN / DE)", {
            "fields": ("team_member_2_title",),
            "classes": ("wide",),
        }),
        ("Team Member 2 - Image", {
            "fields": ("team_member_2_image",),
            "classes": ("wide",),
        }),
    )


@admin.register(ContactPage)
class ContactPageAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("Company Name", {
            "fields": ("company_name",),
            "classes": ("wide",),
        }),
        ("Company Description (IT / EN / DE)", {
            "fields": ("description",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("Address - Building Name", {
            "fields": ("address_building",),
            "classes": ("wide",),
            "description": "This address will also be displayed in the Footer",
        }),
        ("Address - Street", {
            "fields": ("address_street",),
            "classes": ("wide",),
        }),
        ("Address - City/Postal Code", {
            "fields": ("address_city",),
            "classes": ("wide",),
        }),
        ("Phone Number 1", {
            "fields": ("phone_1",),
            "classes": ("wide",),
        }),
        ("Phone Number 2", {
            "fields": ("phone_2",),
            "classes": ("wide",),
        }),
        ("Email Address", {
            "fields": ("email",),
            "classes": ("wide",),
        }),
        ("WhatsApp Number (for link)", {
            "fields": ("whatsapp_number",),
            "classes": ("wide",),
        }),
        ("Google Maps Embed URL", {
            "fields": ("map_embed_url",),
            "classes": ("wide",),
        }),
        ("Social Link - WhatsApp", {
            "fields": ("social_whatsapp",),
            "classes": ("wide",),
        }),
        ("Social Link - Instagram", {
            "fields": ("social_instagram",),
            "classes": ("wide",),
        }),
        ("Social Link - Facebook", {
            "fields": ("social_facebook",),
            "classes": ("wide",),
        }),
        ("Social Link - LinkedIn", {
            "fields": ("social_linkedin",),
            "classes": ("wide",),
        }),
    )


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(SingletonAdmin):
    list_display = ["__str__", "updated_at"]

    fieldsets = (
        ("Privacy Policy Title (IT / EN / DE)", {
            "fields": ("privacy_title",),
            "classes": ("wide",),
            "description": 'Format: {"it": "Italian", "en": "English", "de": "German"}',
        }),
        ("Data Controller (IT / EN / DE)", {
            "fields": ("data_controller",),
            "classes": ("wide",),
        }),
        ("Legal Basis (IT / EN / DE)", {
            "fields": ("legal_basis",),
            "classes": ("wide",),
        }),
        ("Data Collection Purposes (IT / EN / DE)", {
            "fields": ("data_purposes",),
            "classes": ("wide",),
        }),
        ("Data Sharing (IT / EN / DE)", {
            "fields": ("data_sharing",),
            "classes": ("wide",),
        }),
        ("Data Storage (IT / EN / DE)", {
            "fields": ("data_storage",),
            "classes": ("wide",),
        }),
        ("Retention Period (IT / EN / DE)", {
            "fields": ("retention_period",),
            "classes": ("wide",),
        }),
        ("User Rights (IT / EN / DE)", {
            "fields": ("user_rights",),
            "classes": ("wide",),
        }),
        ("Cookie Policy Title (IT / EN / DE)", {
            "fields": ("cookie_title",),
            "classes": ("wide",),
        }),
        ("Cookie Types (IT / EN / DE)", {
            "fields": ("cookie_types",),
            "classes": ("wide",),
        }),
        ("Consent Requirements (IT / EN / DE)", {
            "fields": ("consent_requirements",),
            "classes": ("wide",),
        }),
        ("Cookies Listed (IT / EN / DE)", {
            "fields": ("cookies_listed",),
            "classes": ("wide",),
        }),
    )
