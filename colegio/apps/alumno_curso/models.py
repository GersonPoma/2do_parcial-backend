from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from apps.curso.models import Curso
from apps.usuario.models import Usuario

# Create your models here.

class AlumnoCurso(models.Model):
    gestion = models.IntegerField(default=datetime.now().year)
    id_alumno = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='cursos_inscritos'
    )
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name='alumnos_inscritos'
    )

    class Meta:
        ordering = ['id_alumno__apellido']

    def clean(self):
        if self.id_alumno.rol != Usuario.ALUMNO:
            raise ValidationError('El usuario seleccionado no tiene el rol de alumno.')

    def save(self, *args, **kwargs):
        self.full_clean()   # Esto llama a clean() antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.id_alumno.nombre} {self.id_curso.nivel} {self.id_curso.paralelo}'
                f' {self.gestion}')