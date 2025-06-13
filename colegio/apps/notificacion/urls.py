from django.urls import path
from apps.notificacion.views import RegistrarDispositivoView

urlpatterns = [
    path('registrar-dispositivo/', RegistrarDispositivoView.as_view(), name='registrar_dispositivo'),
]
