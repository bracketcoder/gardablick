from urllib.parse import quote

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import action
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ["full_name", "email", "phone", "source", "is_read", "created_at", "view_link", "reply_link"]
    list_filter = ["is_read", "source", "created_at"]
    search_fields = ["first_name", "last_name", "email", "phone", "message"]
    list_editable = ["is_read"]
    ordering = ["-created_at"]

    # Make all fields read-only in detail view (except is_read)
    readonly_fields = [
        "first_name", "last_name", "email", "phone",
        "message", "source", "property_ref",
        "privacy_accepted", "updates_accepted",
        "created_at", "reply_button"
    ]

    fieldsets = (
        ("Contact Info", {
            "fields": ("first_name", "last_name", "email", "phone"),
        }),
        ("Message", {
            "fields": ("message", "source", "property_ref"),
        }),
        ("Consent", {
            "fields": ("privacy_accepted", "updates_accepted"),
        }),
        ("Status", {
            "fields": ("is_read", "created_at"),
        }),
        ("Actions", {
            "fields": ("reply_button",),
        }),
    )

    def has_add_permission(self, request):
        """Disable adding messages from admin - they come from the website."""
        return False

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """Automatically mark message as read when viewed."""
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=["is_read"])
        return super().change_view(request, object_id, form_url, extra_context)

    @admin.display(description="Name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    @admin.display(description="View")
    def view_link(self, obj):
        url = reverse("admin:contacts_contactmessage_change", args=[obj.pk])
        return format_html(
            '<a href="{}" class="text-primary-600 hover:text-primary-700">View</a>',
            url
        )

    @admin.display(description="Reply")
    def reply_link(self, obj):
        subject = quote(f"Re: Your inquiry to Gardablick")
        body = quote(f"Dear {obj.first_name},\n\nThank you for contacting Gardablick.\n\n")
        mailto = f"mailto:{obj.email}?subject={subject}&body={body}"
        return format_html(
            '<a href="{}" class="text-primary-600 hover:text-primary-700" target="_blank">Reply</a>',
            mailto
        )

    @admin.display(description="Reply via Email")
    def reply_button(self, obj):
        if not obj.pk:
            return "-"
        subject = quote(f"Re: Your inquiry to Gardablick")
        body = quote(f"Dear {obj.first_name},\n\nThank you for contacting Gardablick.\n\n---\nOriginal message:\n{obj.message}\n")
        mailto = f"mailto:{obj.email}?subject={subject}&body={body}"
        return format_html(
            '<a href="{}" class="inline-flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors" target="_blank">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>'
            'Reply to {}</a>',
            mailto,
            obj.first_name
        )


def unread_count(request):
    """Returns the count of unread messages for sidebar badge."""
    count = ContactMessage.objects.filter(is_read=False).count()
    return count if count > 0 else ""
