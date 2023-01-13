from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Message
        fields = ("sender", "receiver", "text", "datetime",)
        read_only_fields = ("datetime",)

