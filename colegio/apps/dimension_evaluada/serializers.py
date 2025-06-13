from rest_framework import serializers
from apps.dimension_evaluada.models import DimensionEvaluada

class DimensionEvaluadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimensionEvaluada
        fields = '__all__'