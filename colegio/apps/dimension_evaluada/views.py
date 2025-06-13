from rest_framework import viewsets

from apps.dimension_evaluada.models import DimensionEvaluada
from apps.dimension_evaluada.serializers import DimensionEvaluadaSerializer
from common.permissions import IsAdmin, OrPermissions, IsProfesor, IsDirector, IsSecretario


# Create your views here.


class DimensionEvaluadaViewSet(viewsets.ModelViewSet):
    queryset = DimensionEvaluada.objects.all()
    serializer_class = DimensionEvaluadaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsProfesor, IsDirector, IsSecretario)]

        return [IsAdmin()]