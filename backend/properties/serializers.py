from rest_framework import serializers
from .models import Property, PropertyImage, LANGUAGES


def media_path(image_field):
    """Return a root-relative path like /media/properties/main/img.png"""
    if image_field and hasattr(image_field, "url"):
        return image_field.url
    return None


def localize(value, lang, fallback="it"):
    """Extract a localized string/list from a JSON translation field."""
    if isinstance(value, dict):
        return value.get(lang) or value.get(fallback, "")
    return value


class PropertyImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PropertyImage
        fields = ["id", "image", "order"]

    def get_image(self, obj):
        return media_path(obj.image)


class PropertyListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            "id", "image", "title", "price", "location",
            "ref", "area", "bedrooms", "bathrooms",
        ]

    def _lang(self):
        request = self.context.get("request")
        if request:
            return request.query_params.get("lang", "it")
        return "it"

    def get_image(self, obj):
        return media_path(obj.main_image)

    def get_title(self, obj):
        return localize(obj.title, self._lang())

    def get_price(self, obj):
        price_int = int(obj.price)
        formatted = f"{price_int:,}".replace(",", ".")
        return f"{formatted}€"

    def get_area(self, obj):
        area_val = int(obj.area) if obj.area == int(obj.area) else obj.area
        return f"{area_val}m²"


class PropertyDetailSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    gallery_images = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    composition = serializers.SerializerMethodField()
    composition_note = serializers.SerializerMethodField()
    location_note = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    commercial_area = serializers.SerializerMethodField()
    net_area = serializers.SerializerMethodField()
    condominium_fees = serializers.SerializerMethodField()
    map_location = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            "id", "title", "location", "price", "ref",
            "area", "commercial_area", "net_area",
            "bedrooms", "bathrooms", "total_rooms",
            "energy_class", "condominium_fees",
            "description", "composition", "composition_note",
            "location_note", "main_image", "gallery_images",
            "map_location",
        ]

    def _lang(self):
        request = self.context.get("request")
        if request:
            return request.query_params.get("lang", "it")
        return "it"

    def get_title(self, obj):
        return localize(obj.title, self._lang())

    def get_description(self, obj):
        return localize(obj.description, self._lang())

    def get_composition(self, obj):
        return localize(obj.composition, self._lang())

    def get_composition_note(self, obj):
        return localize(obj.composition_note, self._lang())

    def get_location_note(self, obj):
        return localize(obj.location_note, self._lang())

    def get_main_image(self, obj):
        return media_path(obj.main_image)

    def get_gallery_images(self, obj):
        images = obj.gallery_images.all()
        return [media_path(img.image) for img in images if img.image]

    def get_price(self, obj):
        price_int = int(obj.price)
        formatted = f"{price_int:,}".replace(",", ".")
        return f"{formatted}€"

    def get_area(self, obj):
        area_val = int(obj.area) if obj.area == int(obj.area) else obj.area
        return f"{area_val}m²"

    def get_commercial_area(self, obj):
        if obj.commercial_area:
            val = int(obj.commercial_area) if obj.commercial_area == int(obj.commercial_area) else obj.commercial_area
            return f"{val}m²"
        return None

    def get_net_area(self, obj):
        if obj.net_area:
            val = int(obj.net_area) if obj.net_area == int(obj.net_area) else obj.net_area
            return f"{val}m²"
        return None

    def get_condominium_fees(self, obj):
        if obj.condominium_fees:
            val = int(obj.condominium_fees) if obj.condominium_fees == int(obj.condominium_fees) else obj.condominium_fees
            return f"{val}€"
        return None

    def get_map_location(self, obj):
        if obj.latitude and obj.longitude:
            return {"lat": float(obj.latitude), "lng": float(obj.longitude)}
        return None
