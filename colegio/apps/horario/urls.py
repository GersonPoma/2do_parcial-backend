from rest_framework.routers import DefaultRouter

from apps.horario.views import HorarioBulkViewSet

router = DefaultRouter()
router.register(r'', HorarioBulkViewSet, basename='horarios')
urlpatterns = router.urls