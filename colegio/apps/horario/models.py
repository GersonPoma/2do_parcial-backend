from django.core.exceptions import ValidationError
from django.db import models

from apps.curso.models import Curso
from apps.materia.models import Materia
from apps.usuario.models import Usuario


# Create your models here.

class Horario(models.Model):
    LUNES = 'LUNES'
    MARTES = 'MARTES'
    MIERCOLES = 'MIERCOLES'
    JUEVES = 'JUEVES'
    VIERNES = 'VIERNES'
    SABADO = 'SABADO'

    DIAS_SEMANA = [
        (LUNES, 'lunes'),
        (MARTES, 'Martes'),
        (MIERCOLES, 'Miércoles'),
        (JUEVES, 'Jueves'),
        (VIERNES, 'Viernes'),
        (SABADO, 'Sábado'),
    ]

    gestion = models.IntegerField()
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_salida = models.TimeField()
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name='horarios'
    )
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        related_name='horarios'
    )
    id_profesor = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='horarios'
    )

    def clean(self):
        if self.id_profesor.rol != Usuario.PROFESOR:
            raise ValidationError('El usuario seleccionado no tiene el rol de profesor.')

    def save(self, *args, **kwargs):
        self.full_clean()   # Esto llama a clean() antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.id_profesor.get_nombre_completo} {self.dia_semana}'
                f'{self.hora_inicio} {self.hora_salida} {self.gestion}')