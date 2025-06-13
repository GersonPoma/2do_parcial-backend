from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_bulk import BulkModelViewSet

from common.permissions import OrPermissions, IsAdmin, IsProfesor, IsSecretario, IsDirector, IsTutor
from .models import AlumnoCurso
from .serializers import AlumnoCursoSerializer
from ..usuario.models import Usuario


# Create your views here.

# class AlumnoCursoViewSet(viewsets.ModelViewSet):
#     queryset = AlumnoCurso.objects.all()
#     serializer_class = AlumnoCursoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['gestion', 'id_alumno', 'id_curso']
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             return [OrPermissions(IsAdmin, IsProfesor)]
#
#         return [IsAdmin()]

class AlumnoCursoBulkViewSet(BulkModelViewSet):
    queryset = AlumnoCurso.objects.all()
    serializer_class = AlumnoCursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gestion', 'id_alumno', 'id_curso']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsProfesor, IsSecretario, IsDirector, IsTutor)]

        return [IsAdmin(), IsSecretario(), IsDirector]

    def get_queryset(self):
        user = self.request.user
        gestion = self.request.query_params.get('gestion') or datetime.now().year
        curso_id = self.request.query_params.get('id_curso')
        alumno_id = self.request.query_params.get('id_alumno')

        if user.rol == Usuario.TUTOR:
            return self._obtener_alumnos_del_tutor(user, gestion)

        if user.rol in [Usuario.ADMIN, Usuario.PROFESOR, Usuario.DIRECTOR, Usuario.SECRETARIO]:
            return self._filtrar_por_gestion_y_filtros_generales(gestion, curso_id, alumno_id)

        return AlumnoCurso.objects.none()

    def _obtener_alumnos_del_tutor(self, user, gestion):
        return AlumnoCurso.objects.filter(
            id_alumno__tutor=user,
            gestion=gestion
        ).select_related('id_alumno', 'id_curso')

    def _filtrar_por_gestion_y_filtros_generales(self, gestion, curso_id=None, alumno_id=None):
        queryset = AlumnoCurso.objects.filter(gestion=gestion)

        if curso_id:
            queryset = queryset.filter(id_curso_id=curso_id)

        if alumno_id:
            queryset = queryset.filter(id_alumno_id=alumno_id)

        return queryset.select_related('id_alumno', 'id_curso')