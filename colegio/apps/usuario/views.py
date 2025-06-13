from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from common.permissions import IsAdmin, IsDirector, IsSecretario, OrPermissions, IsAlumno, IsTutor, IsProfesor
from .serializers import UsuarioSerializer, ProfesorSerializer, \
    AlumnoSerializer, DirectorSerializer, SecretarioSerializer, TutorSerializer
from .models import Usuario

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'rol']

# Super clase para los perfiles
class PerfilViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin | IsDirector | IsSecretario]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ci', 'nombre', 'apellido']

    def get_permissions(self):
        if self.action == 'retrieve':
            return [OrPermissions(IsAlumno, IsTutor, IsProfesor, IsDirector, IsSecretario, IsAdmin)]
        return [OrPermissions(IsAdmin, IsDirector, IsSecretario)]

class ProfesorViewSet(PerfilViewSet):
    queryset = Usuario.objects.filter(rol=Usuario.PROFESOR)
    serializer_class = ProfesorSerializer

class AlumnoViewSet(PerfilViewSet):
    queryset = Usuario.objects.filter(rol=Usuario.ALUMNO)
    serializer_class = AlumnoSerializer

class DirectorViewSet(PerfilViewSet):
    queryset = Usuario.objects.filter(rol=Usuario.DIRECTOR)
    serializer_class = DirectorSerializer

class SecretarioViewSet(PerfilViewSet):
    queryset = Usuario.objects.filter(rol=Usuario.SECRETARIO)
    serializer_class = SecretarioSerializer

class TutorViewSet(PerfilViewSet):
    queryset = Usuario.objects.filter(rol=Usuario.TUTOR)
    serializer_class = TutorSerializer