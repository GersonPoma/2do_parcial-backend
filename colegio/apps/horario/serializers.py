from dataclasses import fields

from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin

from apps.horario.models import Horario
from apps.usuario.models import Usuario


class HorarioSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    nombre_materia = serializers.CharField(
        source='id_materia.nombre',
        read_only=True
    )
    nombre_profesor = serializers.CharField(
        source='id_profesor.get_nombre_completo',
        read_only=True
    )

    class Meta:
        model = Horario
        fields = '__all__'
        extra_kwargs = {
            'nombre_materia': {'read_only': True},
            'nombre_profesor': {'read_only': True}
        }

    def validate_id_profesor(self, value):
        if value.rol != Usuario.PROFESOR:
            raise serializers.ValidationError("El usuario no tiene rol de profesor.")
        return value