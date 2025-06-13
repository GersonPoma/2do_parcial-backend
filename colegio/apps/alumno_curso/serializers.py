from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin

from .models import AlumnoCurso
from ..usuario.models import Usuario


class AlumnoCursoSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    nombre_completo_alumno = serializers.SerializerMethodField()
    curso = serializers.SerializerMethodField()

    gestion = serializers.IntegerField(required=False)

    class Meta:
        model = AlumnoCurso
        fields = ['id', 'gestion', 'nombre_completo_alumno', 'id_alumno',
                  'curso', 'id_curso']

    def validate_id_alumno(self, value):
        if value.rol != Usuario.ALUMNO:
            raise serializers.ValidationError("El usuario no tiene rol de alumno.")
        return value

    def get_nombre_completo_alumno(self, obj):
        return obj.id_alumno.get_nombre_completo

    def get_curso(self, obj):
        return obj.id_curso.get_detalle_curso

class DetalleAlumnoCursoSerializer(serializers.ModelSerializer):
    nombre_completo_alumno = serializers.SerializerMethodField()
    curso = serializers.SerializerMethodField()

    class Meta:
        model = AlumnoCurso
        fields = ['id', 'nombre_completo_alumno', 'curso']

    def get_nombre_completo_alumno(self, obj):
        return obj.id_alumno.get_nombre_completo

    def get_curso(self, obj):
        return obj.id_curso.get_detalle_curso