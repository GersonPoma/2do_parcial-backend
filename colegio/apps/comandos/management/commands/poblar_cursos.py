from django.core.management.base import BaseCommand

from apps.curso.models import Curso

class Command(BaseCommand):
    help = 'Pobla la tabla Curso con cursos de 1ro a 4to, paralelos A, B y C.'

    def handle(self, *args, **kwargs):
        niveles = ['1ro', '2do', '3ro', '4to']
        paralelos = ['A', 'B', 'C']

        total_creados = 0
        for nivel in niveles:
            for paralelo in paralelos:
                aula = f"{nivel[0]}{paralelo}"  # Ej: 1A, 2B...
                obj, created = Curso.objects.get_or_create(
                    nivel=nivel,
                    paralelo=paralelo,
                    defaults={
                        'etapa': 'Secundaria',
                        'aula': aula
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Curso creado: {obj}'))
                    total_creados += 1
                else:
                    self.stdout.write(f'Curso ya existía: {obj}')

        self.stdout.write(self.style.SUCCESS(f'Total cursos creados: {total_creados}'))
