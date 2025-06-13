from datetime import datetime

from rest_framework import viewsets

from common.permissions import IsAdmin, IsDirector, IsSecretario, OrPermissions, IsAlumno, IsTutor, IsProfesor
from .models import Curso
from .serializers import CursoSerializer
from ..alumno_curso.models import AlumnoCurso
from ..horario.models import Horario
from ..usuario.models import Usuario


# Create your views here.

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsDirector, IsSecretario, IsAlumno, IsTutor, IsProfesor)]

        return [IsAdmin(), IsDirector]

    def get_queryset(self):
        user = self.request.user
        year_actual = datetime.now().year

        # Admin, Director, Secretario: Ven todos los cursos
        if user.rol in [Usuario.ADMIN, Usuario.DIRECTOR, Usuario.SECRETARIO]:
            return super().get_queryset()

        # Si es profesor, filtrar cursos que imparte en la gestión actual
        if user.rol == Usuario.PROFESOR:
            # Obtener IDs de cursos donde el profesor tiene horarios en la gestión
            cursos_ids = Horario.objects.filter(
                id_profesor=user,
                gestion=year_actual
            ).values_list('id_curso', flat=True).distinct()

            return self.queryset.filter(id__in=cursos_ids)

        # Alumno: Cursos donde está inscrito en el año actual
        if user.rol == Usuario.ALUMNO:
            cursos_ids = AlumnoCurso.objects.filter(
                id_alumno=user,
                gestion=year_actual
            ).values_list('id_curso', flat=True)

            return self.queryset.filter(id__in=cursos_ids)

        # Tutor: Cursos de sus alumnos en el año actual
        if user.rol == Usuario.TUTOR:
            alumnos_ids = user.alumnos.values_list('id', flat=True)
            cursos_ids = AlumnoCurso.objects.filter(
                id_alumno__in=alumnos_ids,
                gestion=year_actual
            ).values_list('id_curso', flat=True)

            return self.queryset.filter(id__in=cursos_ids)

        return Curso.objects.none()