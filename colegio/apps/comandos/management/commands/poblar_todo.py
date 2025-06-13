from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Ejecuta todos los comandos de poblamiento: dimensiones, cursos, materias, profesores.'

    def handle(self, *args, **kwargs):
        comandos = [
            ('Dimensiones', 'poblar_dimensiones'),
            ('Cursos', 'poblar_cursos'),
            ('Materias', 'poblar_materias'),
            ('Profesores', 'poblar_profesores'),
            ('Horarios', 'poblar_horario'),
            ('Alumno y Tutores 2022', 'crear_alumnos_tutores_2022'),
            ('Alumno y Tutores 2023', 'crear_alumnos_tutores_2023'),
            ('Alumno y Tutores 2024', 'crear_alumnos_tutores_2024'),
            ('Alumno y Tutores 2025', 'crear_alumnos_tutores_2025'),
            ('Actividades', 'generar_actividades_y_notas_2025'),
            ('Asistencias', 'generar_asistencias'),
        ]

        for nombre, comando in comandos:
            self.stdout.write(self.style.NOTICE(f"Ejecutando: {nombre}..."))
            try:
                call_command(comando)
            except CommandError as e:
                self.stdout.write(self.style.ERROR(f'Error en {comando}: {e}'))

        self.stdout.write(self.style.SUCCESS("Poblamiento completo: dimensiones, cursos, materias y profesores."))
