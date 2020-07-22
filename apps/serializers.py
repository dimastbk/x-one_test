from rest_framework import serializers


class EmptySerializer(serializers.Serializer):
    pass


class ErrorSerializer(serializers.Serializer):
    """Сериализатор ошибок."""

    detail = serializers.CharField()
