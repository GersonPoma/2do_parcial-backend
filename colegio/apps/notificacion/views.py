from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.notificacion.models import Dispositivo
from apps.notificacion.serializers import DispositivoSerializer

class RegistrarDispositivoView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DispositivoSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            plataforma = serializer.validated_data['plataforma']
            usuario = request.user

            dispositivo, creado = Dispositivo.objects.update_or_create(
                token=token,
                defaults={'usuario': usuario, 'plataforma': plataforma},
            )

            msg = "Dispositivo registrado." if creado else "Dispositivo actualizado."
            return Response({"detail": msg}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)