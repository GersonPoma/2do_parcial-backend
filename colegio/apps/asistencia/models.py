from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from apps.alumno_curso.models import AlumnoCurso
from apps.materia.models import Materia


# Create your models here.

class Asistencia(models.Model):
    fecha = models.DateField(default=timezone.localdate)
    presente = models.BooleanField()
    id_alumno_curso = models.ForeignKey(
        AlumnoCurso,
        on_delete=models.PROTECT,
        related_name='asistencias'
    )
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        related_name='asistencias'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fecha', 'id_alumno_curso', 'id_materia'],
                name='unique_asistencia_alumno_fecha_materia'
            )
        ]

    def clean(self):
        if not self.pk and Asistencia.objects.filter(
                fecha=self.fecha,
                id_alumno_curso=self.id_alumno_curso,
                id_materia=self.id_materia
        ).exists():
            raise ValidationError(
                "Ya existe una asistencia para este alumno en esta materia y fecha."
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # llama a clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.id_alumno_curso.id_alumno.get_nombre_completo} '
                f'{self.id_materia.nombre} {self.id_alumno_curso.id_curso.nivel} '
                f'{self.id_alumno_curso.id_curso.paralelo} {self.id_alumno_curso.gestion} '
                f'{self.presente}')