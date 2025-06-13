from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_bulk import BulkModelViewSet

from apps.alumno_curso.models import AlumnoCurso
from apps.horario.models import Horario
from apps.horario.serializers import HorarioSerializer
from apps.usuario.models import Usuario
from common.permissions import OrPermissions, IsAdmin, IsDirector, IsSecretario, IsAlumno, IsTutor, IsProfesor


# Create your views here.

class HorarioBulkViewSet(BulkModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'gestion', 'id_curso', 'id_materia', 'id_profesor'
    ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsDirector, IsSecretario, IsAlumno, IsTutor, IsProfesor)]

        return [IsAdmin(), IsDirector()]

    def get_queryset(self):
        user = self.request.user
        gestion = self.request.query_params.get('gestion') or datetime.now().year

        base_queryset = Horario.objects.select_related('id_curso', 'id_materia', 'id_profesor')

        if user.rol == Usuario.ALUMNO:
            cursos_ids = AlumnoCurso.objects.filter(
                id_alumno=user,
                gestion=gestion
            ).values_list('id_curso', flat=True)
            queryset = base_queryset.filter(id_curso__in=cursos_ids, gestion=gestion)

        elif user.rol == Usuario.PROFESOR:
            queryset = base_queryset.filter(id_profesor=user, gestion=gestion)

        elif user.rol == Usuario.TUTOR:
            alumnos_ids = user.alumnos.values_list('id', flat=True)
            cursos_ids = AlumnoCurso.objects.filter(
                id_alumno__in=alumnos_ids,
                gestion=gestion
            ).values_list('id_curso', flat=True)
            queryset = base_queryset.filter(id_curso__in=cursos_ids, gestion=gestion).distinct()

        elif user.rol in [Usuario.SECRETARIO, Usuario.DIRECTOR, Usuario.ADMIN]:
            queryset = base_queryset

        else:
            return Horario.objects.none()

        # Aplica filtros adicionales como id_materia, id_profesor, etc.
        return self.filter_queryset(queryset)

