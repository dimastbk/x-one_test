from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogPageViewSet

router = DefaultRouter()
router.register("", BlogPageViewSet, basename="blog")
urlpatterns = router.urls
