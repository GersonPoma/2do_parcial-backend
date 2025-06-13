from rest_framework import serializers

from apps.resumen_nota.models import ResumenNota


class ResumenNotaSerializer(serializers.ModelSerializer):
    nombre_materia = serializers.CharField(
        source='id_materia.nombre',
        read_only=True
    )
    class Meta:
        model = ResumenNota
        fields = '__all__'
        fields += ['nombre_materia']