from django.core.exceptions import ValidationError
from django.db import models

from apps.curso.models import Curso
from apps.dimension_evaluada.models import DimensionEvaluada
from apps.materia.models import Materia
from apps.usuario.models import Usuario


# Create your models here.

class Actividad(models.Model):
    TIPOS = [
        ('TAREA', 'Tarea'),
        ('EXAMEN', 'Examen'),
        ('PRACTICO', 'Práctico'),
        ('OTRO', 'Otro'),
    ]

    TRIMESTRE = [
        (1, 'Primer Trimestre'),
        (2, 'Segundo Trimestre'),
        (3, 'Tercer Trimestre'),
    ]

    titulo = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    gestion = models.IntegerField()
    trimestre = models.IntegerField(choices=TRIMESTRE)

    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        related_name='actividades'
    )
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name='actividades'
    )
    id_profesor = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        limit_choices_to={'rol': Usuario.PROFESOR},
        related_name='actividades_creadas'
    )
    id_dimension = models.ForeignKey(
        DimensionEvaluada,
        on_delete=models.PROTECT,
        related_name='actividades'
    )

    def clean(self):
        from apps.horario.models import Horario

        if not Horario.objects.filter(
            id_profesor=self.id_profesor,
            id_materia=self.id_materia,
            id_curso=self.id_curso,
            gestion=self.gestion
        ).exists():
            raise ValidationError('El profesor no dicta esa materia en el curso indicado para esta gestión.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.titulo} - {self.id_materia.nombre} - {self.id_curso}'