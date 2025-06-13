from django.db import models

# Create your models here.

class DimensionEvaluada(models.Model):
    SER = 'Ser'
    SABER = 'Saber'
    HACER = 'Hacer'
    DECIDIR = 'Decidir'
    AUTOEVALUACION = 'Autoevaluación'

    DIMENSIONES = [
        (SER, 'Ser'),
        (SABER, 'Saber'),
        (HACER, 'Hacer'),
        (DECIDIR, 'Decidir'),
        (AUTOEVALUACION, 'Autoevaluación'),
    ]

    nombre = models.CharField(max_length=30, choices=DIMENSIONES, unique=True)
    puntaje_maximo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nombre} ({self.puntaje_maximo} pts)'