from rest_framework.routers import DefaultRouter
from src.drf_versioning import views

router = DefaultRouter()

router.register("", views.VersionViewSet, basename="version")

urlpatterns = router.urls
