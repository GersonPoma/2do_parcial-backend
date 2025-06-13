from rest_framework.routers import DefaultRouter

from .views import MateriaViewSet

router = DefaultRouter()

router.register(r'', MateriaViewSet, basename='materia')

urlpatterns = router.urls