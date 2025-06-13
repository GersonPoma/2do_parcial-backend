from rest_framework import serializers
from apps.actividad.models import Actividad
from apps.horario.models import Horario
from apps.usuario.models import Usuario


class ActividadSerializer(serializers.ModelSerializer):
    profesor_nombre = serializers.CharField(
        source='id_profesor.get_nombre_completo', read_only=True
    )
    curso_nombre = serializers.CharField(
        source='id_curso.get_detalle_curso', read_only=True
    )
    materia_nombre = serializers.CharField(
        source='id_materia.nombre', read_only=True
    )
    dimension_nombre = serializers.CharField(
        source='id_dimesion.nombre', read_only=True
    )

    class Meta:
        model = Actividad
        fields = [
            'id',
            'titulo',
            'fecha_entrega',
            'tipo',
            'gestion',
            'trimestre',
            'id_materia',
            'materia_nombre',
            'id_curso',
            'curso_nombre',
            'id_profesor',
            'profesor_nombre',
            'id_dimension',
            'dimension_nombre',
        ]
        read_only_fields = ['id_profesor']  # lo estableceremos desde el request

    def validate(self, data):
        request = self.context['request']
        user = request.user

        if user.rol == Usuario.PROFESOR:
            # Asignamos automáticamente el profesor autenticado
            data['id_profesor'] = user
            profesor = user
        elif user.rol == Usuario.ADMIN:
            if 'id_profesor' not in data:
                raise serializers.ValidationError("Debes especificar el profesor para la actividad.")

            profesor = data['id_profesor']
        else:
            raise serializers.ValidationError("No tienes permiso para crear actividades.")

        if not Horario.objects.filter(
                id_profesor=profesor,
                id_materia=data['id_materia'],
                id_curso=data['id_curso'],
                gestion=data['gestion']
        ).exists():
            raise serializers.ValidationError("No dictas esta materia en ese curso durante esta gestión.")

        return data