from django.db import models

from apps.alumno_curso.models import AlumnoCurso
from apps.materia.models import Materia


# Create your models here.

class ResumenNota(models.Model):
    APROBADO = 'APROBADO/A'
    REPROBADO = 'REPROBADO/A'
    EN_PROCESO = 'EN PROCESO'

    ESTADOS = [
        (APROBADO, 'Aprobado/a'),
        (REPROBADO, 'Reprobado/a'),
        (EN_PROCESO, 'En proceso'),
    ]

    nota_1erT = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_2doT = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_3erT = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_anual = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    estado = models.CharField(
        max_length=12, choices=ESTADOS, default=EN_PROCESO
    )
    id_alumno_curso = models.ForeignKey(
        AlumnoCurso,
        on_delete=models.PROTECT,
        related_name='resumen_notas'
    )
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        related_name='resumen_notas'
    )

    class Meta:
        unique_together = ['id_alumno_curso', 'id_materia']