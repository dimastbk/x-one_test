from django.contrib.auth import authenticate, get_user_model
from django.db import models

from rest_framework import mixins, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_yasg.utils import swagger_auto_schema

from apps.blog.models import BlogPage
from apps.serializers import EmptySerializer, ErrorSerializer
from apps.user.serializers import (
    BaseUserSerializer,
    SignInSerializer,
    SignUpSerializer,
    TokenSerializer,
    UserPatchSerializer,
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
            user = authenticate(
                request=request,
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
        except get_user_model().DoesNotExist:
            raise APIException({"detail": "Неверный логин или пароль", "code": "auth"})

        if not user:
            raise APIException({"detail": "Неверный логин или пароль", "code": "auth"})

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


class UserViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = (
        get_user_model().objects.prefetch_related("pages").annotate(models.Sum("pages"))
    )
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: EmptySerializer,
            APIException.status_code: ErrorSerializer(),
        },
    )
    @action(methods=("delete",), detail=True)
    def delete_all_pages(self, request, pk=None):
        if request.user.is_staff and pk:
            BlogPage.objects.filter(user_id=pk).delete()
        return Response()

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: BaseUserSerializer,
            APIException.status_code: ErrorSerializer(),
        },
    )
    @action(methods=("get",), detail=False)
    def userinfo(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=request.auth.user_id)
        serializer = BaseUserSerializer(instance=user)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ("partial_update", "update"):
            return UserPatchSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "userinfo":
            return (permissions.IsAuthenticated(),)
        return (permissions.IsAdminUser(),)
