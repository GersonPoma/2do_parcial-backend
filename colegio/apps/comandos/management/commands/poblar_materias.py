from django.core.management.base import BaseCommand

from apps.materia.models import Materia


class Command(BaseCommand):
    help = 'Pobla la tabla Materia con las materias del sistema.'

    def handle(self, *args, **kwargs):
        materias_data = [
            'Matemáticas',
            'Lenguaje',
            'Ciencias Naturales',
            'Ciencias Sociales',
            'Inglés',
            'Psicología',
            'Religión y Moral',
            'Educación Musical',
            'Educación Física',
            'Técnica Tecnológica',
            'Artes Plásticas',
            'Química',
            'Física',
            'Filosofía',
            'Geografía',
            'Biología',
        ]

        total = 0
        for nombre in materias_data:
            obj, created = Materia.objects.get_or_create(nombre=nombre)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Creada: {obj}'))
                total += 1
            else:
                self.stdout.write(f'Ya existía: {obj}')
        self.stdout.write(self.style.SUCCESS(f'Total materias creadas: {total}'))
