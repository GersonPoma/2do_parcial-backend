from datetime import date
from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin

from apps.alumno_actividad.models import AlumnoActividad

class AlumnoActividadSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    alumno_nombre = serializers.CharField(
        source='id_alumno_curso.id_alumno.get_nombre_completo',
        read_only=True
    )
    actividad_titulo = serializers.CharField(
        source='id_actividad.titulo',
        read_only=True
    )
    estado = serializers.CharField(read_only=True)
    trimestre = serializers.IntegerField(
        source='id_actividad.trimestre',
        read_only=True
    )
    fecha_entrega = serializers.DateField(
        source='id_actividad.fecha_entrega',
        read_only=True
    )

    class Meta:
        model = AlumnoActividad
        fields = [
            'id',
            'id_actividad',
            'actividad_titulo',
            'trimestre',
            'id_alumno_curso',
            'alumno_nombre',
            'nota',
            'fecha_entregada',
            'estado',
            'fecha_entrega',
        ]

    def validate(self, data):
        actividad = data.get('id_actividad') or getattr(self.instance, 'id_actividad', None)
        alumno_curso = data.get('id_alumno_curso') or getattr(self.instance, 'id_alumno_curso', None)
        nota = data.get('nota', getattr(self.instance, 'nota', None))
        fecha_entregada = data.get('fecha_entregada', getattr(self.instance, 'fecha_entregada', None))

        if not actividad or not alumno_curso:
            raise serializers.ValidationError("Debe enviar actividad y alumno_curso.")

        if actividad.id_curso != alumno_curso.id_curso:
            raise serializers.ValidationError("El alumno no pertenece al curso de la actividad.")

        if actividad.gestion != alumno_curso.gestion:
            raise serializers.ValidationError("El alumno no está inscrito en la gestión de la actividad.")

        if nota is not None:
            puntaje_max = actividad.id_dimension.puntaje_maximo
            if nota > puntaje_max:
                raise serializers.ValidationError(
                    f"La nota no puede ser mayor que el puntaje máximo de la dimensión ({puntaje_max})."
                )

        if fecha_entregada and fecha_entregada > date.today():
            raise serializers.ValidationError("La fecha de entrega no puede ser mayor que la fecha actual.")

        return data

    def update(self, instance, validated_data):
        # Bulk update: validated_data es lista
        if isinstance(validated_data, list):
            for i, item in enumerate(validated_data):
                self.validate(item)
                fecha = item.get('fecha_entregada')
                actividad = item.get('id_actividad') or self.instance[i].id_actividad
                self.instance[i].estado = self.calcular_estado(fecha, actividad)
        else:
            fecha = validated_data.get('fecha_entregada')
            actividad = validated_data.get('id_actividad') or instance.id_actividad
            validated_data['estado'] = self.calcular_estado(fecha, actividad)

        return super().update(instance, validated_data)

    def calcular_estado(self, fecha, actividad):
        if fecha and actividad:
            return AlumnoActividad.ATRASADO if fecha > actividad.fecha_entrega else AlumnoActividad.ENTREGADO
        return AlumnoActividad.PENDIENTE