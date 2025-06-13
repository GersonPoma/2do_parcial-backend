from django.core.management.base import BaseCommand
from apps.dimension_evaluada.models import DimensionEvaluada


class Command(BaseCommand):
    help = 'Pobla la tabla DimensionEvaluada con las dimensiones predeterminadas.'

    def handle(self, *args, **kwargs):
        dimensiones_data = [
            {'nombre': 'Ser', 'puntaje_maximo': 5},
            {'nombre': 'Saber', 'puntaje_maximo': 45},
            {'nombre': 'Hacer', 'puntaje_maximo': 40},
            {'nombre': 'Decidir', 'puntaje_maximo': 5},
            {'nombre': 'Autoevaluación', 'puntaje_maximo': 5},
        ]

        total = 0
        for data in dimensiones_data:
            obj, created = DimensionEvaluada.objects.get_or_create(
                nombre=data['nombre'],
                defaults={'puntaje_maximo': data['puntaje_maximo']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Creada: {obj}'))
                total += 1
            else:
                self.stdout.write(f'Ya existe: {obj}')
        self.stdout.write(self.style.SUCCESS(f'Total dimensiones creadas: {total}'))
