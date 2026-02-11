from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "first_name", "last_name", "email", "phone",
            "message", "privacy_accepted", "updates_accepted",
            "source", "property_ref",
        ]
