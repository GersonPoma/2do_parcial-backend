from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from apps.actividad.models import Actividad
from apps.alumno_curso.models import AlumnoCurso


# Create your models here.

class AlumnoActividad(models.Model):
    ENTREGADO = 'ENTREGADO'
    ATRASADO = 'ATRASADO'
    PENDIENTE = 'PENDIENTE'

    ESTADOS = [
        (ENTREGADO, 'Entregado'),
        (ATRASADO, 'Atrasado'),
        (PENDIENTE, 'Pendiente'),
    ]

    id_actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name='alumnos'
    )
    id_alumno_curso = models.ForeignKey(
        AlumnoCurso,
        on_delete=models.CASCADE,
        related_name='actividades'
    )
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha_entregada = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)

    class Meta:
        unique_together = ('id_actividad', 'id_alumno_curso')

    def clean(self):
        # Validación: nota no puede exceder el puntaje máximo de la dimensión
        if self.nota is not None:
            puntaje_max = self.id_actividad.id_dimension.puntaje_maximo
            if self.nota > puntaje_max:
                raise ValidationError(
                    f"La nota ingresada ({self.nota}) no puede superar el puntaje máximo ({puntaje_max}) "
                    f"de la dimensión '{self.id_actividad.id_dimension.nombre}'."
                )

            # Si no se envió fecha_entregada, la asumimos como hoy
            if not self.fecha_entregada:
                self.fecha_entregada = date.today()

        # Estado según la fecha de entrega
        if self.fecha_entregada:
            if self.fecha_entregada > self.id_actividad.fecha_entrega:
                self.estado = self.ATRASADO
            else:
                self.estado = self.ENTREGADO
        else:
            self.estado = self.PENDIENTE

    def save(self, *args, **kwargs):
        self.full_clean()
        is_new = self._state.adding
        old_nota = None

        if not is_new and self.pk:
            old_nota = AlumnoActividad.objects.filter(pk=self.pk).values_list('nota', flat=True).first()

        super().save(*args, **kwargs)

        if self.nota is not None and (is_new or self.nota != old_nota):
            from apps.resumen_nota.utils import actualizar_resumen_nota
            actualizar_resumen_nota(self)

    def __str__(self):
        return f'{self.id_alumno_curso.id_alumno.get_nombre_completo} - {self.id_actividad.titulo} - {self.estado}'