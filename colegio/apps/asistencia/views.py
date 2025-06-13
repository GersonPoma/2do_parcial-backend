from datetime import datetime

from django.db import IntegrityError
from rest_framework_bulk import BulkModelViewSet
from rest_framework.exceptions import PermissionDenied, ValidationError
from django_filters.rest_framework import DjangoFilterBackend

from apps.alumno_curso.models import AlumnoCurso
from apps.asistencia.models import Asistencia
from apps.asistencia.serializers import AsistenciaSerializer
from apps.asistencia.filters import AsistenciaFilter
from apps.horario.models import Horario
from apps.usuario.models import Usuario


class AsistenciaBulkViewSet(BulkModelViewSet):
    serializer_class = AsistenciaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AsistenciaFilter

    def get_queryset(self):
        user = self.request.user
        gestion = self.request.query_params.get('gestion') or datetime.now().year

        if user.rol in [Usuario.ADMIN, Usuario.DIRECTOR]:
            return self._asistencias_filtradas()

        if user.rol == Usuario.PROFESOR:
            return self._asistencias_del_profesor(user, gestion)

        if user.rol == Usuario.ALUMNO:
            return self._asistencias_del_alumno(user, gestion)

        if user.rol == Usuario.TUTOR:
            return self._asistencias_del_tutor(user, gestion)

        return Asistencia.objects.none()

    def _asistencias_base(self):
        return Asistencia.objects.select_related(
            'id_alumno_curso__id_alumno',
            'id_alumno_curso__id_curso',
            'id_materia'
        ).order_by('id_alumno_curso__id_alumno__apellido')

    def _asistencias_filtradas(self):
        """
        Para ADMIN y DIRECTOR: permite todos los filtros definidos en el filterset.
        """
        return self.filter_queryset(self._asistencias_base())

    def _asistencias_del_profesor(self, profesor, gestion):
        curso_id = self.request.query_params.get('id_curso')
        materia_id = self.request.query_params.get('id_materia')

        if not curso_id or not materia_id:
            raise ValidationError("Debe proporcionar 'id_curso' y 'id_materia'.")

        if not Horario.objects.filter(
                id_profesor=profesor,
                id_curso_id=curso_id,
                id_materia_id=materia_id,
                gestion=gestion
        ).exists():
            raise ValidationError("No estás autorizado para ver esta asistencia.")

        base_qs = self._asistencias_base().filter(
            id_alumno_curso__id_curso_id=curso_id,
            id_alumno_curso__gestion=gestion,
            id_materia_id=materia_id
        )
        return self.filter_queryset(base_qs)

    def _asistencias_del_alumno(self, alumno, gestion):
        id_materia = self.request.query_params.get('id_materia')
        if not id_materia:
            raise ValidationError("Debe especificar el parámetro 'id_materia'.")

        alumno_curso = AlumnoCurso.objects.filter(id_alumno=alumno, gestion=gestion).first()
        if not alumno_curso:
            return Asistencia.objects.none()

        base_qs = self._asistencias_base().filter(
            id_alumno_curso=alumno_curso,
            id_materia_id=id_materia
        )
        return self.filter_queryset(base_qs)

    def _asistencias_del_tutor(self, tutor, gestion):
        id_alumno = self.request.query_params.get("id_alumno")
        id_materia = self.request.query_params.get("id_materia")

        if not id_alumno or not id_materia:
            raise ValidationError("Debe proporcionar 'id_alumno' e 'id_materia'.")

        # Verifica que el alumno pertenezca al tutor
        if not tutor.alumnos.filter(id=id_alumno).exists():
            raise PermissionDenied("No tienes permiso para ver la asistencia de este alumno.")

        alumno_curso = AlumnoCurso.objects.filter(id_alumno_id=id_alumno, gestion=gestion).first()
        if not alumno_curso:
            return Asistencia.objects.none()

        queryset = self._asistencias_base().filter(
            id_alumno_curso=alumno_curso,
            id_materia_id=id_materia
        )

        return self.filter_queryset(queryset)

    def perform_create(self, serializer):
        user = self.request.user

        if user.rol not in [Usuario.ADMIN, Usuario.PROFESOR]:
            raise PermissionDenied("No tienes permiso para registrar asistencias.")
        try:
            serializer.save()
        except IntegrityError:
            raise ValidationError("Ya existe un registro de asistencia para uno o más alumnos en esa fecha.")

    def perform_update(self, serializer):
        user = self.request.user

        if user.rol not in [Usuario.ADMIN, Usuario.PROFESOR]:
            raise PermissionDenied("No puedes modificar asistencias.")

        # Soporte para PATCH en lote
        if isinstance(serializer.validated_data, list):
            for i, data in enumerate(serializer.validated_data):
                if user.rol == Usuario.ADMIN:
                    continue  # admin puede todo

                asistencia = self.get_queryset().filter(pk=data.get('id')).first()
                if not asistencia:
                    raise ValidationError(f"Asistencia con ID {data.get('id')} no encontrada.")

                alumno_curso = asistencia.id_alumno_curso
                if not Horario.objects.filter(
                        id_profesor=user,
                        id_materia=asistencia.id_materia,
                        id_curso=alumno_curso.id_curso,
                        gestion=alumno_curso.gestion
                ).exists():
                    raise PermissionDenied(
                        f"No puedes modificar la asistencia con ID {asistencia.id} (no dictas esa clase)."
                    )

        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user

        if user.rol != Usuario.ADMIN:
            raise PermissionDenied("Solo el administrador puede eliminar asistencias.")
        instance.delete()