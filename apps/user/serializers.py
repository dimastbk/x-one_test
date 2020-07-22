from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


class SignInSerializer(serializers.Serializer):
    """Сериализатор авторизации на сайте."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False,
    )


class SignUpSerializer(serializers.Serializer):
    """Сериализатор регистрации на сайте."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
        validators=[validate_password],
    )

    def validate_password2(self, value):
        if self.initial_data.get("password") != value:
            raise serializers.ValidationError("Пароли не совпадают")
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор токена авторизации."""

    token = serializers.CharField()


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("password",)
        model = get_user_model()


class UserPatchSerializer(BaseUserSerializer):
    class Meta:
        fields = ("is_active",)
        model = get_user_model()


class UserSerializer(BaseUserSerializer):
    pages__sum = serializers.IntegerField()
