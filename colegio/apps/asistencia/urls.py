from rest_framework.routers import DefaultRouter

from apps.asistencia.views import AsistenciaBulkViewSet

router = DefaultRouter()
router.register(r'', AsistenciaBulkViewSet, basename='asistencias')

urlpatterns = router.urls