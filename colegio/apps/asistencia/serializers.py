from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin

from ..alumno_curso.serializers import DetalleAlumnoCursoSerializer
from ..asistencia.models import Asistencia
from ..horario.models import Horario
from ..usuario.models import Usuario


class AsistenciaSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    detalle_alumno_curso = DetalleAlumnoCursoSerializer(
        source='id_alumno_curso',
        read_only=True
    )

    class Meta:
        model = Asistencia
        fields = ['id', 'fecha', 'presente', 'id_alumno_curso',
                  'detalle_alumno_curso', 'id_materia']
        extra_kwargs = {
            'fecha': {'read_only': True}
        }

    def validate(self, data):
        user = self.context['request'].user

        if user.rol == Usuario.PROFESOR:
            alumno_curso = data['id_alumno_curso']
            if not Horario.objects.filter(
                    id_profesor=user,
                    id_materia=data['id_materia'],
                    id_curso=alumno_curso.id_curso,
                    gestion=alumno_curso.gestion
            ).exists():
                raise serializers.ValidationError(
                    "No estás autorizado para marcar asistencia en este curso o materia."
                )
        return data