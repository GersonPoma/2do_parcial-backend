from datetime import datetime

from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_bulk import BulkModelViewSet

from apps.alumno_actividad.filters import AlumnoActividadFilter
from apps.alumno_actividad.models import AlumnoActividad
from apps.alumno_actividad.serializers import AlumnoActividadSerializer
from apps.notificacion.notificaciones_academicas import notificar_alumno_actividad, notificar_tutor_alumno_actividad, \
    notificar_actividad_creada, notificar_tutores_actividad_creada
from apps.usuario.models import Usuario
from apps.alumno_curso.models import AlumnoCurso
from apps.horario.models import Horario


class AlumnoActividadViewSet(BulkModelViewSet):
    serializer_class = AlumnoActividadSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlumnoActividadFilter

    def get_queryset(self):
        user = self.request.user

        materia = self.request.query_params.get("id_materia")
        curso = self.request.query_params.get("id_curso")
        gestion = self.request.query_params.get("gestion")
        trimestre = self.request.query_params.get("trimestre")

        # ⚠️ Detecta si es un PATCH o PUT en lote (no tiene self.action)
        if self.request.method in ['PATCH', 'PUT'] and isinstance(self.request.data, list):
            return AlumnoActividad.objects.all()

        # ✅ También permite acceso sin filtros para retrieve/destroy
        if self.action in ['retrieve', 'partial_update', 'update', 'destroy']:
            return AlumnoActividad.objects.all()

        if not gestion:
            gestion = datetime.now().year

        # Para no repetir el mismo orden
        order_fields = ['id_actividad__trimestre', 'id_actividad__fecha_entrega']

        # ADMIN: requiere curso, materia y gestión
        if user.rol == Usuario.ADMIN:
            required = {"id_curso": curso, "id_materia": materia, "gestion": gestion}
            missing = [k for k, v in required.items() if not v]
            if missing:
                raise ValidationError(f"Debe especificar los siguientes campos: {', '.join(missing)}.")

            filters = {
                'id_actividad__id_curso': curso,
                'id_actividad__id_materia': materia,
                'id_actividad__gestion': gestion,
            }
            if trimestre:
                filters['id_actividad__trimestre'] = trimestre

            return AlumnoActividad.objects.filter(**filters).select_related(
                'id_alumno_curso__id_alumno',
                'id_alumno_curso__id_curso',
                'id_actividad__id_materia',
                'id_actividad__id_dimension',
                'id_actividad__id_profesor'
            ).order_by(*order_fields)

        # Otros roles: materia es obligatoria, gestión se infiere si no viene
        if not materia:
            raise ValidationError("Debe especificar materia.")
        if not gestion:
            gestion = datetime.now().year

        filters = {
            'id_actividad__id_materia': materia,
            'id_actividad__gestion': gestion,
        }
        if trimestre:
            filters['id_actividad__trimestre'] = trimestre

        if user.rol == Usuario.PROFESOR:
            if not curso:
                raise ValidationError("Debe especificar curso.")

            if not Horario.objects.filter(
                id_profesor=user,
                id_curso_id=curso,
                id_materia_id=materia,
                gestion=gestion
            ).exists():
                return AlumnoActividad.objects.none()

            filters['id_actividad__id_curso'] = curso
            filters['id_actividad__id_profesor'] = user

            return AlumnoActividad.objects.filter(**filters).select_related(
                'id_alumno_curso__id_alumno',
                'id_alumno_curso__id_curso',
                'id_actividad__id_materia',
                'id_actividad__id_dimension',
                'id_actividad__id_profesor'
            ).order_by(*order_fields)

        if user.rol == Usuario.ALUMNO:
            alumno_curso = AlumnoCurso.objects.filter(id_alumno=user, gestion=gestion).first()
            if not alumno_curso:
                return AlumnoActividad.objects.none()

            filters['id_alumno_curso'] = alumno_curso

            return AlumnoActividad.objects.filter(**filters).select_related(
                'id_actividad__id_materia',
                'id_actividad__id_dimension',
                'id_alumno_curso__id_curso'
            ).order_by(*order_fields)

        if user.rol == Usuario.TUTOR:
            id_alumno = self.request.query_params.get("id_alumno")

            if not id_alumno:
                raise ValidationError("Debe proporcionar el parámetro 'id_alumno'.")

            if not user.alumnos.filter(id=id_alumno).exists():
                raise PermissionDenied("No tienes acceso a este alumno.")

            alumno_curso = AlumnoCurso.objects.filter(id_alumno_id=id_alumno, gestion=gestion).first()
            if not alumno_curso:
                return AlumnoActividad.objects.none()

            filters['id_alumno_curso'] = alumno_curso

            return AlumnoActividad.objects.filter(**filters).select_related(
                'id_actividad__id_materia',
                'id_actividad__id_dimension',
                'id_alumno_curso__id_curso'
            ).order_by(*order_fields)

        return AlumnoActividad.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if user.rol not in [Usuario.ADMIN, Usuario.PROFESOR]:
            raise PermissionDenied("No tienes permiso para asignar o modificar actividades.")

        try:
            instances = serializer.save()

            # Asegurar que .save() de cada instancia se llame individualmente
            if isinstance(instances, list):
                for instance in instances:
                    instance.save()
                    notificar_actividad_creada(instance)
                    notificar_tutores_actividad_creada(instance)
            else:
                instances.save()
                notificar_actividad_creada(instances)
                notificar_tutores_actividad_creada(instances)

        except IntegrityError:
            raise ValidationError("Uno o más registros ya existen. No se permiten duplicados.")

    def perform_update(self, serializer):
        user = self.request.user
        instances = serializer.save()

        if isinstance(instances, list):
            for i, instance in enumerate(instances):
                actividad = instance.id_actividad
                if user.rol != Usuario.ADMIN and actividad.id_profesor != user:
                    raise PermissionDenied("No puedes modificar esta nota.")

                old_nota = AlumnoActividad.objects.get(pk=instance.pk).nota if instance.pk else None
                instance.save()  # ejecuta clean, estado y resumen
                # Notificaciones push
                notificar_alumno_actividad(instance, old_nota)
                notificar_tutor_alumno_actividad(instance, old_nota)
        else:
            instance = instances
            actividad = instance.id_actividad
            if user.rol != Usuario.ADMIN and actividad.id_profesor != user:
                raise PermissionDenied("No puedes modificar esta nota.")

            old_nota = AlumnoActividad.objects.get(pk=instance.pk).nota if instance.pk else None
            instance.save()

            # Notificaciones push
            notificar_alumno_actividad(instance, old_nota)
            notificar_tutor_alumno_actividad(instance, old_nota)

    def perform_destroy(self, instance):
        user = self.request.user

        if user.rol == Usuario.ADMIN:
            instance.delete()
            return

        if instance.id_actividad.id_profesor != user:
            raise PermissionDenied("No puedes eliminar esta nota.")
        instance.delete()