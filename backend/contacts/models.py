from django.db import models


class ContactMessage(models.Model):
    SOURCE_CHOICES = [
        ("contact", "Contact Page"),
        ("property", "Property Detail"),
        ("vendi", "Sell Page"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    privacy_accepted = models.BooleanField(default=False)
    updates_accepted = models.BooleanField(default=False)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="contact")
    property_ref = models.CharField(max_length=50, blank=True, help_text="Property reference if from detail page")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} ({self.get_source_display()})"
