from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.blog.models import BlogPage
from apps.blog.serializers import BlogPageSerializer


class BlogPageViewSet(ModelViewSet):
    queryset = BlogPage.objects.select_related("user")
    serializer_class = BlogPageSerializer

    def get_permissions(self):
        if self.action == "list":
            return (permissions.AllowAny(),)
        if self.action == "destroy":
            return (permissions.IsAdminUser(),)
        return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        qs = super().get_queryset()
        if not (self.request.user and self.request.user.is_staff):
            return qs.filter(is_published=True)
        return qs
