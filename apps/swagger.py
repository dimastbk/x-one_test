from django.urls import path

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


def swagger_urls():
    """Настройка Swagger UI."""
    schema_view = get_schema_view(
        openapi.Info(title="X-One Blog API", default_version="v1",),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    return [
        path(
            "",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
