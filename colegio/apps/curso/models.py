from django.db import models

# Create your models here.

class Curso(models.Model):
    nivel = models.CharField(max_length=3)
    paralelo = models.CharField(max_length=1)
    etapa = models.CharField(max_length=10, default='Secundaria')
    aula = models.CharField(max_length=5)

    @property
    def get_detalle_curso(self):
        return f"{self.nivel} {self.paralelo}"

    def __str__(self):
        return f'{self.nivel} {self.paralelo}'