from rest_framework.routers import DefaultRouter

from apps.user.views import AuthViewSet, UserViewSet

router = DefaultRouter()
router.register("", AuthViewSet, basename="auth")
router.register("", UserViewSet, basename="user")
urlpatterns = router.urls
