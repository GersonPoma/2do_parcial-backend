from rest_framework import serializers
from apps.notificacion.models import Dispositivo

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['token', 'plataforma']