from django.db import models
from django.conf import settings

class Dispositivo(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='dispositivos',
        on_delete=models.CASCADE
    )
    token = models.CharField(max_length=255, unique=True)
    plataforma = models.CharField(max_length=10, choices=[("android", "Android"), ("ios", "iOS")])
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario} - {self.plataforma} - {self.token[:10]}..."
