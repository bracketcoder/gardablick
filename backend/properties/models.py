from django.db import models

LANGUAGES = ("it", "en", "de")

PROPERTY_TYPE_CHOICES = [
    ("appartamento", "Apartment"),
    ("attico", "Penthouse"),
    ("garage", "Garage"),
    ("casa-singola", "Detached house"),
    ("rustico", "Farmhouse"),
    ("terreno", "Building land"),
    ("villa", "Villa"),
    ("villa-bifamiliare", "Semi-detached villa"),
    ("villa-schiera", "Terraced villa"),
]


def empty_translations():
    return {"it": "", "en": "", "de": ""}


def empty_translations_list():
    return {"it": [], "en": [], "de": []}


class Property(models.Model):
    # Translatable fields (JSON: {"it": "...", "en": "...", "de": "..."})
    title = models.JSONField(default=empty_translations, help_text='{"it": "...", "en": "...", "de": "..."}')
    description = models.JSONField(default=empty_translations, blank=True, help_text='{"it": "...", "en": "...", "de": "..."}')
    composition = models.JSONField(default=empty_translations_list, blank=True, help_text='{"it": [...], "en": [...], "de": [...]}')
    composition_note = models.JSONField(default=empty_translations, blank=True, help_text='{"it": "...", "en": "...", "de": "..."}')
    location_note = models.JSONField(default=empty_translations, blank=True, help_text='{"it": "...", "en": "...", "de": "..."}')

    # Non-translatable fields
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    ref = models.CharField(max_length=50, unique=True)

    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total area in m²")
    commercial_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    total_rooms = models.IntegerField(null=True, blank=True)

    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES, blank=True)
    energy_class = models.CharField(max_length=10, blank=True)
    condominium_fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    main_image = models.ImageField(upload_to="properties/main/")

    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ["-created_at"]

    def __str__(self):
        title_str = self.title.get("it", "") if isinstance(self.title, dict) else str(self.title)
        return f"{self.ref} - {title_str}"


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ImageField(upload_to="properties/gallery/")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Image for {self.property.ref}"
