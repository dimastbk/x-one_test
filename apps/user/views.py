from django.contrib.auth import get_user_model
from django.db import models

from rest_framework import mixins, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_yasg.utils import swagger_auto_schema

from apps.serializers import ErrorSerializer
from apps.user.serializers import (
    SignInSerializer,
    SignUpSerializer,
    TokenSerializer,
    UserSerializer,
)


class AuthViewSet(GenericViewSet):
    @swagger_auto_schema(
        request_body=SignInSerializer,
        responses={
            status.HTTP_200_OK: TokenSerializer,
            APIException.status_code: ErrorSerializer(),
        },
    )
    @action(methods=("post",), detail=False)
    def signin(self, request, *args, **kwargs):
        """Авторизация на сайте."""
        serializer = SignInSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        try:
            user = get_user_model().objects.get(
                username=serializer.validated_data["username"]
            )
        except get_user_model().DoesNotExist:
            raise APIException("Неверный логин или пароль")

        if not user.check_password(serializer.validated_data["password"]):
            raise APIException("Неверный логин или пароль")

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    @swagger_auto_schema(
        request_body=SignUpSerializer,
        responses={
            status.HTTP_200_OK: TokenSerializer,
            APIException.status_code: ErrorSerializer(),
        },
    )
    @action(methods=("post",), detail=False)
    def signup(self, request, *args, **kwargs):
        """Регистрация на сайте."""
        serializer = SignUpSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = get_user_model()(
            username=serializer.validated_data["username"], is_active=True
        )
        user.set_password(serializer.validated_data["password"])
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = (
        get_user_model().objects.prefetch_related("pages").annotate(models.Sum("pages"))
    )
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenSerializer,
            APIException.status_code: ErrorSerializer(),
        },
    )
    @action(methods=("put",), detail=True)
    def block(self, request):
        pass
