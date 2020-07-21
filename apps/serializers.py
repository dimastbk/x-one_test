from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    """Сериализатор ошибок."""

    detail = serializers.CharField()
