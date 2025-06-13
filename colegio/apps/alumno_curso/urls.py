from rest_framework.routers import DefaultRouter

from apps.alumno_curso.views import AlumnoCursoBulkViewSet

router = DefaultRouter()

router.register(r'', AlumnoCursoBulkViewSet, basename='alumnos_cursos')

urlpatterns = router.urls