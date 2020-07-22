from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from apps.blog.models import BlogPage
from apps.blog.serializers import PageSerializer, ShortPageSerializer


class BlogPageViewSet(ModelViewSet):
    queryset = BlogPage.objects.select_related("user")
    serializer_class = ShortPageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return (permissions.AllowAny(),)
        if self.action == "destroy":
            return (permissions.IsAdminUser(),)
        return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(is_published=True)
        return qs

    def get_object(self):
        page = super().get_object()
        if page.is_published or (
            self.request.user.is_authenticated
            and (self.request.user.is_staff or page.user == self.request.user)
        ):
            return page
        raise PermissionDenied()

    def get_serializer_class(self):
        if self.action in ("create", "retrieve", "partial_update", "update"):
            return PageSerializer
        return ShortPageSerializer
