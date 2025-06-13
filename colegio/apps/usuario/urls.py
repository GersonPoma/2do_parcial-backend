from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, ProfesorViewSet, AlumnoViewSet, TutorViewSet, \
    DirectorViewSet, SecretarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'profesores', ProfesorViewSet, basename='profesores')
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'tutores', TutorViewSet, basename='tutores')
router.register(r'director', DirectorViewSet, basename='director')
router.register(r'secretario', SecretarioViewSet, basename='secretario')

# Agregamos las rutas del router al final
urlpatterns = router.urls