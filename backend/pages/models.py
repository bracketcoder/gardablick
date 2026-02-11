from django.db import models


LANGUAGES = ("it", "en", "de")


def empty_translations():
    return {"it": "", "en": "", "de": ""}


class SingletonModel(models.Model):
    """Base class for singleton models."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def get_field_translation(self, field_name, lang="it"):
        """Get translated value for a field, with fallback to Italian."""
        value = getattr(self, field_name, {})
        if isinstance(value, dict):
            return value.get(lang) or value.get("it", "")
        return str(value)


class PrivacyPolicy(SingletonModel):
    """Singleton model for Privacy Policy content with multi-language support."""

    # Privacy Policy Section
    privacy_title = models.JSONField(default=empty_translations, verbose_name="Privacy Policy Title (IT / EN / DE)")
    data_controller = models.JSONField(default=empty_translations, verbose_name="Data Controller (IT / EN / DE)")
    legal_basis = models.JSONField(default=empty_translations, verbose_name="Legal Basis (IT / EN / DE)")
    data_purposes = models.JSONField(default=empty_translations, verbose_name="Data Collection Purposes (IT / EN / DE)")
    data_sharing = models.JSONField(default=empty_translations, verbose_name="Data Sharing (IT / EN / DE)")
    data_storage = models.JSONField(default=empty_translations, verbose_name="Data Storage (IT / EN / DE)")
    retention_period = models.JSONField(default=empty_translations, verbose_name="Retention Period (IT / EN / DE)")
    user_rights = models.JSONField(default=empty_translations, verbose_name="User Rights (IT / EN / DE)")

    # Cookie Policy Section
    cookie_title = models.JSONField(default=empty_translations, verbose_name="Cookie Policy Title (IT / EN / DE)")
    cookie_types = models.JSONField(default=empty_translations, verbose_name="Cookie Types (IT / EN / DE)")
    consent_requirements = models.JSONField(default=empty_translations, verbose_name="Consent Requirements (IT / EN / DE)")
    cookies_listed = models.JSONField(default=empty_translations, verbose_name="Cookies Listed (IT / EN / DE)")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"

    def __str__(self):
        return "Privacy Policy"


class HomePage(SingletonModel):
    """Singleton model for Home page content."""

    # About Section
    about_subtitle = models.JSONField(default=empty_translations, verbose_name="About Subtitle (IT / EN / DE)")
    about_heading = models.JSONField(default=empty_translations, verbose_name="About Heading (IT / EN / DE)")
    about_paragraph1 = models.JSONField(default=empty_translations, verbose_name="About Paragraph 1 (IT / EN / DE)")
    about_paragraph2 = models.JSONField(default=empty_translations, verbose_name="About Paragraph 2 (IT / EN / DE)")
    about_image = models.ImageField(upload_to="pages/home/", blank=True, verbose_name="About Section Image")

    # Services Section
    services_subtitle = models.JSONField(default=empty_translations, verbose_name="Services Subtitle (IT / EN / DE)")
    services_heading = models.JSONField(default=empty_translations, verbose_name="Services Heading (IT / EN / DE)")
    services_paragraph1 = models.JSONField(default=empty_translations, verbose_name="Services Paragraph 1 (IT / EN / DE)")
    services_paragraph2 = models.JSONField(default=empty_translations, verbose_name="Services Paragraph 2 (IT / EN / DE)")
    services_image = models.ImageField(upload_to="pages/home/", blank=True, verbose_name="Services Section Image")

    # Service Icons Section (5 services)
    service_icon_1_title = models.JSONField(default=empty_translations, verbose_name="Service Icon 1 Title (IT / EN / DE)")
    service_icon_1_image = models.ImageField(upload_to="pages/home/icons/", blank=True, verbose_name="Service Icon 1 Image")
    service_icon_2_title = models.JSONField(default=empty_translations, verbose_name="Service Icon 2 Title (IT / EN / DE)")
    service_icon_2_image = models.ImageField(upload_to="pages/home/icons/", blank=True, verbose_name="Service Icon 2 Image")
    service_icon_3_title = models.JSONField(default=empty_translations, verbose_name="Service Icon 3 Title (IT / EN / DE)")
    service_icon_3_image = models.ImageField(upload_to="pages/home/icons/", blank=True, verbose_name="Service Icon 3 Image")
    service_icon_4_title = models.JSONField(default=empty_translations, verbose_name="Service Icon 4 Title (IT / EN / DE)")
    service_icon_4_image = models.ImageField(upload_to="pages/home/icons/", blank=True, verbose_name="Service Icon 4 Image")
    service_icon_5_title = models.JSONField(default=empty_translations, verbose_name="Service Icon 5 Title (IT / EN / DE)")
    service_icon_5_image = models.ImageField(upload_to="pages/home/icons/", blank=True, verbose_name="Service Icon 5 Image")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"

    def __str__(self):
        return "Home Page"


class SellPage(SingletonModel):
    """Singleton model for Sell (Vendi) page content."""

    # Intro Section
    intro_subtitle = models.JSONField(default=empty_translations, verbose_name="Intro Subtitle (IT / EN / DE)")
    intro_heading = models.JSONField(default=empty_translations, verbose_name="Intro Heading (IT / EN / DE)")
    intro_description = models.JSONField(default=empty_translations, verbose_name="Intro Description (IT / EN / DE)")
    intro_image = models.ImageField(upload_to="pages/sell/", blank=True, verbose_name="Intro Section Image")

    # Services Section (5 services with title and description)
    service_1_title = models.JSONField(default=empty_translations, verbose_name="Service 1 Title (IT / EN / DE)")
    service_1_description = models.JSONField(default=empty_translations, verbose_name="Service 1 Description (IT / EN / DE)")
    service_1_icon = models.ImageField(upload_to="pages/sell/icons/", blank=True, verbose_name="Service 1 Icon")

    service_2_title = models.JSONField(default=empty_translations, verbose_name="Service 2 Title (IT / EN / DE)")
    service_2_description = models.JSONField(default=empty_translations, verbose_name="Service 2 Description (IT / EN / DE)")
    service_2_icon = models.ImageField(upload_to="pages/sell/icons/", blank=True, verbose_name="Service 2 Icon")

    service_3_title = models.JSONField(default=empty_translations, verbose_name="Service 3 Title (IT / EN / DE)")
    service_3_description = models.JSONField(default=empty_translations, verbose_name="Service 3 Description (IT / EN / DE)")
    service_3_icon = models.ImageField(upload_to="pages/sell/icons/", blank=True, verbose_name="Service 3 Icon")

    service_4_title = models.JSONField(default=empty_translations, verbose_name="Service 4 Title (IT / EN / DE)")
    service_4_description = models.JSONField(default=empty_translations, verbose_name="Service 4 Description (IT / EN / DE)")
    service_4_icon = models.ImageField(upload_to="pages/sell/icons/", blank=True, verbose_name="Service 4 Icon")

    service_5_title = models.JSONField(default=empty_translations, verbose_name="Service 5 Title (IT / EN / DE)")
    service_5_description = models.JSONField(default=empty_translations, verbose_name="Service 5 Description (IT / EN / DE)")
    service_5_icon = models.ImageField(upload_to="pages/sell/icons/", blank=True, verbose_name="Service 5 Icon")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sell Page"
        verbose_name_plural = "Sell Page"

    def __str__(self):
        return "Sell Page"


class ServicePage(SingletonModel):
    """Singleton model for Services page content."""

    # Service 1
    service_1_title = models.JSONField(default=empty_translations, verbose_name="Service 1 Title (IT / EN / DE)")
    service_1_description = models.JSONField(default=empty_translations, verbose_name="Service 1 Description (IT / EN / DE)")
    service_1_icon = models.ImageField(upload_to="pages/services/icons/", blank=True, verbose_name="Service 1 Icon")
    service_1_image = models.ImageField(upload_to="pages/services/", blank=True, verbose_name="Service 1 Image")

    # Service 2
    service_2_title = models.JSONField(default=empty_translations, verbose_name="Service 2 Title (IT / EN / DE)")
    service_2_description = models.JSONField(default=empty_translations, verbose_name="Service 2 Description (IT / EN / DE)")
    service_2_icon = models.ImageField(upload_to="pages/services/icons/", blank=True, verbose_name="Service 2 Icon")
    service_2_image = models.ImageField(upload_to="pages/services/", blank=True, verbose_name="Service 2 Image")

    # Service 3
    service_3_title = models.JSONField(default=empty_translations, verbose_name="Service 3 Title (IT / EN / DE)")
    service_3_description = models.JSONField(default=empty_translations, verbose_name="Service 3 Description (IT / EN / DE)")
    service_3_icon = models.ImageField(upload_to="pages/services/icons/", blank=True, verbose_name="Service 3 Icon")
    service_3_image = models.ImageField(upload_to="pages/services/", blank=True, verbose_name="Service 3 Image")

    # Service 4
    service_4_title = models.JSONField(default=empty_translations, verbose_name="Service 4 Title (IT / EN / DE)")
    service_4_description = models.JSONField(default=empty_translations, verbose_name="Service 4 Description (IT / EN / DE)")
    service_4_icon = models.ImageField(upload_to="pages/services/icons/", blank=True, verbose_name="Service 4 Icon")
    service_4_image = models.ImageField(upload_to="pages/services/", blank=True, verbose_name="Service 4 Image")

    # Service 5
    service_5_title = models.JSONField(default=empty_translations, verbose_name="Service 5 Title (IT / EN / DE)")
    service_5_description = models.JSONField(default=empty_translations, verbose_name="Service 5 Description (IT / EN / DE)")
    service_5_icon = models.ImageField(upload_to="pages/services/icons/", blank=True, verbose_name="Service 5 Icon")
    service_5_image = models.ImageField(upload_to="pages/services/", blank=True, verbose_name="Service 5 Image")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Page"

    def __str__(self):
        return "Service Page"


class AboutPage(SingletonModel):
    """Singleton model for About page content."""

    # Agency Section
    agency_subtitle = models.JSONField(default=empty_translations, verbose_name="Agency Subtitle (IT / EN / DE)")
    agency_heading = models.JSONField(default=empty_translations, verbose_name="Agency Heading (IT / EN / DE)")
    agency_paragraph1 = models.JSONField(default=empty_translations, verbose_name="Agency Paragraph 1 (IT / EN / DE)")
    agency_paragraph2 = models.JSONField(default=empty_translations, verbose_name="Agency Paragraph 2 (IT / EN / DE)")
    agency_image = models.ImageField(upload_to="pages/about/", blank=True, verbose_name="Agency Section Image")

    # Team Section - Member 1
    team_member_1_name = models.CharField(max_length=100, blank=True, verbose_name="Team Member 1 Name")
    team_member_1_title = models.JSONField(default=empty_translations, verbose_name="Team Member 1 Title (IT / EN / DE)")
    team_member_1_image = models.ImageField(upload_to="pages/about/team/", blank=True, verbose_name="Team Member 1 Image")

    # Team Section - Member 2
    team_member_2_name = models.CharField(max_length=100, blank=True, verbose_name="Team Member 2 Name")
    team_member_2_title = models.JSONField(default=empty_translations, verbose_name="Team Member 2 Title (IT / EN / DE)")
    team_member_2_image = models.ImageField(upload_to="pages/about/team/", blank=True, verbose_name="Team Member 2 Image")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return "About Page"


class ContactPage(SingletonModel):
    """Singleton model for Contact page content. Also used by Footer."""

    # Contact Info
    company_name = models.CharField(max_length=100, default="GARDABLICK", verbose_name="Company Name")
    description = models.JSONField(default=empty_translations, verbose_name="Description (IT / EN / DE)")

    # Address
    address_building = models.CharField(max_length=100, blank=True, verbose_name="Building Name (e.g., Palazzo Morgante)")
    address_street = models.CharField(max_length=200, blank=True, verbose_name="Street Address")
    address_city = models.CharField(max_length=100, blank=True, verbose_name="City/Postal Code (e.g., 25087 - Salò (BS))")

    # Contact Details
    phone_1 = models.CharField(max_length=50, blank=True, verbose_name="Phone Number 1")
    phone_2 = models.CharField(max_length=50, blank=True, verbose_name="Phone Number 2")
    email = models.EmailField(blank=True, verbose_name="Email Address")
    whatsapp_number = models.CharField(max_length=50, blank=True, verbose_name="WhatsApp Number (for link)")

    # Map
    map_embed_url = models.URLField(max_length=500, blank=True, verbose_name="Google Maps Embed URL")

    # Social Links
    social_whatsapp = models.URLField(blank=True, verbose_name="WhatsApp Link")
    social_instagram = models.URLField(blank=True, verbose_name="Instagram Link")
    social_facebook = models.URLField(blank=True, verbose_name="Facebook Link")
    social_linkedin = models.URLField(blank=True, verbose_name="LinkedIn Link")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

    def __str__(self):
        return "Contact Page"
