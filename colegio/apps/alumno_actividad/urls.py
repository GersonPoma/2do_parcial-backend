from rest_framework.routers import DefaultRouter
from apps.alumno_actividad.views import AlumnoActividadViewSet

router = DefaultRouter()
router.register(r'', AlumnoActividadViewSet, basename='alumnos-actividades')

urlpatterns = router.urls
