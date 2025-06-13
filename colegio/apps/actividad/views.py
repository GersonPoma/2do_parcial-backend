from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.actividad.models import Actividad
from apps.actividad.serializers import ActividadSerializer
from apps.alumno_actividad.models import AlumnoActividad
from apps.alumno_curso.models import AlumnoCurso
from apps.horario.models import Horario
from apps.usuario.models import Usuario


class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_curso', 'gestion', 'id_materia', 'trimestre']

    def get_queryset(self):
        user = self.request.user
        queryset = Actividad.objects.select_related(
            'id_curso', 'id_materia', 'id_profesor', 'id_dimension'
        )

        # ADMIN y DIRECTOR: ven todo
        if user.rol in [Usuario.ADMIN, Usuario.DIRECTOR]:
            return queryset

        # PROFESOR: solo sus actividades
        if user.rol == Usuario.PROFESOR:
            curso = self.request.query_params.get('id_curso')
            materia = self.request.query_params.get('id_materia')
            gestion = self.request.query_params.get('gestion')
            trimestre = self.request.query_params.get('trimestre')

            queryset = queryset.filter(id_profesor=user)

            # Validar que realmente dicta esa materia en ese curso y gestión
            if curso and materia and gestion:
                if not Horario.objects.filter(
                    id_profesor=user,
                    id_curso_id=curso,
                    id_materia_id=materia,
                    gestion=gestion
                ).exists():
                    return Actividad.objects.none()

            # Aplicar filtros (gestion y materia son comunes)
            if curso:
                queryset = queryset.filter(id_curso_id=curso)
            if materia:
                queryset = queryset.filter(id_materia_id=materia)
            if gestion:
                queryset = queryset.filter(gestion=gestion)
            if trimestre:
                queryset = queryset.filter(trimestre=trimestre)
            return queryset

        # ALUMNO no debe acceder
        return Actividad.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if user.rol not in [Usuario.ADMIN, Usuario.PROFESOR]:
            raise PermissionDenied("No tienes permiso para crear actividades.")

        if user.rol == Usuario.PROFESOR:
            serializer.validated_data['id_profesor'] = user
            profesor = user
        else:
            profesor = serializer.validated_data.get('id_profesor')
            if not profesor:
                raise ValidationError("Debes especificar el profesor responsable.")

        curso = serializer.validated_data['id_curso']
        materia = serializer.validated_data['id_materia']
        gestion = serializer.validated_data['gestion']

        if not Horario.objects.filter(
                id_profesor=profesor,
                id_curso=curso,
                id_materia=materia,
                gestion=gestion
        ).exists():
            raise ValidationError("El profesor no dicta esta materia en ese curso y gestión.")

        actividad = serializer.save(id_profesor=user)

        # Crear AlumnoActividad para todos los alumnos inscritos en el curso y gestión
        alumnos_curso = AlumnoCurso.objects.filter(
            id_curso=actividad.id_curso,
            gestion=actividad.gestion
        )

        alumno_actividades = [
            AlumnoActividad(id_actividad=actividad, id_alumno_curso=alumno)
            for alumno in alumnos_curso
        ]

        try:
            AlumnoActividad.objects.bulk_create(alumno_actividades)
        except IntegrityError:
            raise ValidationError("Ya existen registros de esta actividad para uno o más alumnos.")

    def perform_update(self, serializer):
        user = self.request.user
        actividad = self.get_object()

        if user.rol == Usuario.ADMIN:
            serializer.save()
            return

        if actividad.id_profesor != user:
            raise PermissionDenied("Solo puedes modificar tus propias actividades.")

        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user

        if user.rol == Usuario.ADMIN:
            instance.delete()
            return

        if instance.id_profesor != user:
            raise PermissionDenied("Solo puedes eliminar tus propias actividades.")

        instance.delete()
