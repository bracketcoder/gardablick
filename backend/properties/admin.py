from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Property, PropertyImage


class PropertyImageInline(TabularInline):
    model = PropertyImage
    extra = 3
    fields = ["image", "order"]


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = [
        "ref", "get_title_it", "location", "price",
        "bedrooms", "bathrooms", "is_active", "created_at",
    ]
    list_filter = ["is_active", "location", "property_type", "bedrooms", "bathrooms"]
    search_fields = ["ref", "location"]
    list_editable = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "ref", "location", "price", "property_type", "is_active",
            ),
        }),
        ("Title (IT / EN / DE)", {
            "fields": ("title",),
            "description": 'JSON format: {"it": "...", "en": "...", "de": "..."}',
        }),
        ("Areas", {
            "fields": ("area", "commercial_area", "net_area"),
        }),
        ("Rooms", {
            "fields": ("bedrooms", "bathrooms", "total_rooms"),
        }),
        ("Details", {
            "fields": ("energy_class", "condominium_fees"),
        }),
        ("Description (IT / EN / DE)", {
            "fields": ("description",),
            "description": 'JSON format: {"it": "...", "en": "...", "de": "..."}',
        }),
        ("Composition (IT / EN / DE)", {
            "fields": ("composition", "composition_note"),
            "description": (
                'composition: {"it": [...], "en": [...], "de": [...]}\n'
                'composition_note: {"it": "...", "en": "...", "de": "..."}'
            ),
        }),
        ("Location Note (IT / EN / DE)", {
            "fields": ("location_note",),
        }),
        ("Main Image", {
            "fields": ("main_image",),
        }),
        ("Map Location", {
            "fields": ("latitude", "longitude"),
        }),
        ("Metadata", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    inlines = [PropertyImageInline]

    @admin.display(description="Title (IT)")
    def get_title_it(self, obj):
        if isinstance(obj.title, dict):
            return obj.title.get("it", "")
        return str(obj.title)
