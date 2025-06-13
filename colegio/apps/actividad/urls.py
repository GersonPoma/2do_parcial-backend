from rest_framework.routers import DefaultRouter
from apps.actividad.views import ActividadViewSet

router = DefaultRouter()
router.register(r'', ActividadViewSet, basename='actividades')

urlpatterns = router.urls
