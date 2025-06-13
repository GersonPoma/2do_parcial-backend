from datetime import datetime
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from common.permissions import OrPermissions, IsAdmin, IsDirector, IsSecretario, IsTutor, IsAlumno, IsProfesor
from .models import Materia
from .serializers import MateriaSerializer
from ..alumno_curso.models import AlumnoCurso
from ..usuario.models import Usuario


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsDirector, IsSecretario, IsTutor, IsAlumno, IsProfesor)]
        return [IsAdmin()]

    def get_queryset(self):
        user = self.request.user
        year_actual = self.request.query_params.get('gestion') or datetime.now().year

        # Admin, Director, Secretario: Acceso completo
        if user.rol in [Usuario.ADMIN, Usuario.DIRECTOR, Usuario.SECRETARIO]:
            return super().get_queryset()

        # Profesor: Solo materias que imparte en la gestión actual
        if user.rol == Usuario.PROFESOR:
            return self._get_materias_profesor(user, year_actual)

        # Alumno: Solo materias matriculadas en la gestión actual
        if user.rol == Usuario.ALUMNO:
            return self._get_materias_alumno(user, year_actual)

        # Tutor: Materias de sus alumnos en la gestión actual
        if user.rol == Usuario.TUTOR:
            return self._get_materias_tutor(user, year_actual)

        return Materia.objects.none()

    def _get_materias_profesor(self, user, year):
        """Obtiene materias que el profesor imparte en la gestión indicada, y opcionalmente en un curso específico"""
        id_curso = self.request.query_params.get('id_curso')

        filtros = {
            'horarios__id_profesor': user,
            'horarios__gestion': year
        }

        if id_curso:
            filtros['horarios__id_curso'] = id_curso

        return Materia.objects.filter(**filtros).distinct()

    def _get_materias_alumno(self, alumno, year):
        """Obtiene materias del alumno via Curso -> Horario"""
        cursos_alumno = AlumnoCurso.objects.filter(
            id_alumno=alumno,
            gestion=year
        ).values_list('id_curso', flat=True)

        return Materia.objects.filter(
            horarios__id_curso__in=cursos_alumno,
            horarios__gestion=year
        ).distinct()

    def _get_materias_tutor(self, tutor, year):
        """Obtiene materias de sus alumnos, con opción de filtrar por un alumno específico"""
        id_alumno = self.request.query_params.get('id_alumno')

        if id_alumno:
            if not tutor.alumnos.filter(id=id_alumno).exists():
                raise PermissionDenied("No tienes permiso para ver las materias de este alumno.")

            alumno = tutor.alumnos.get(id=id_alumno)
            return self._get_materias_alumno(alumno, year)

        # Si no se especifica alumno, mostrar materias de todos sus alumnos
        alumnos_ids = tutor.alumnos.values_list('id', flat=True)

        cursos_alumnos = AlumnoCurso.objects.filter(
            id_alumno__in=alumnos_ids,
            gestion=year
        ).values_list('id_curso', flat=True)

        return Materia.objects.filter(
            horarios__id_curso__in=cursos_alumnos,
            horarios__gestion=year
        ).distinct()