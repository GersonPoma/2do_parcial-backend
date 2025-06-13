from rest_framework.routers import DefaultRouter

from apps.dimension_evaluada.views import DimensionEvaluadaViewSet

router = DefaultRouter()
router.register(r'', DimensionEvaluadaViewSet, basename='dimesione-evaluada')

urlpatterns = router.urls