from django.core.management.base import BaseCommand
from datetime import time

from apps.usuario.models import Usuario
from apps.materia.models import Materia
from apps.curso.models import Curso
from apps.horario.models import Horario


class Command(BaseCommand):
    help = 'Pobla el horario del curso 4to C'

    def handle(self, *args, **kwargs):
        gestion = 2025
        nombre_curso = ("4to", "C")

        bloques = {
            1: (time(7, 30), time(8, 15)),
            2: (time(8, 15), time(9, 0)),
            3: (time(9, 0), time(9, 45)),
            4: (time(9, 55), time(10, 40)),
            5: (time(10, 40), time(11, 25)),
            6: (time(11, 35), time(12, 20)),
            7: (time(12, 20), time(13, 5)),
        }

        horario_data = [
            # (día, bloque, materia, CI del profesor)
            ("LUNES", 1, "Educación Física", "10016"),
            ("LUNES", 2, "Educación Física", "10016"),
            ("LUNES", 3, "Ciencias Naturales", "10015"),
            ("LUNES", 4, "Ciencias Naturales", "10015"),
            ("LUNES", 5, "Artes Plásticas", "10009"),
            ("LUNES", 6, "Filosofía", "10008"),
            ("LUNES", 7, "Ciencias Sociales", "10019"),

            ("MARTES", 1, "Física", "10017"),
            ("MARTES", 2, "Física", "10017"),
            ("MARTES", 3, "Inglés", "10005"),
            ("MARTES", 4, "Religión y Moral", "10010"),
            ("MARTES", 5, "Lenguaje", "10020"),
            ("MARTES", 6, "Lenguaje", "10020"),
            ("MARTES", 7, "Matemáticas", "10014"),

            ("MIERCOLES", 1, "Educación Musical", "10007"),
            ("MIERCOLES", 2, "Educación Musical", "10007"),
            ("MIERCOLES", 3, "Matemáticas", "10014"),
            ("MIERCOLES", 4, "Matemáticas", "10014"),
            ("MIERCOLES", 5, "Química", "10018"),
            ("MIERCOLES", 6, "Química", "10018"),
            ("MIERCOLES", 7, "Técnica Tecnológica", "10002"),

            ("JUEVES", 1, "Lenguaje", "10020"),
            ("JUEVES", 2, "Lenguaje", "10020"),
            ("JUEVES", 3, "Inglés", "10005"),
            ("JUEVES", 4, "Inglés", "10005"),
            ("JUEVES", 5, "Artes Plásticas", "10009"),
            ("JUEVES", 6, "Ciencias Sociales", "10019"),
            ("JUEVES", 7, "Ciencias Sociales", "10019"),

            ("VIERNES", 1, "Matemáticas", "10014"),
            ("VIERNES", 2, "Matemáticas", "10014"),
            ("VIERNES", 3, "Inglés", "10005"),
            ("VIERNES", 4, "Inglés", "10005"),
            ("VIERNES", 5, "Filosofía", "10008"),
            ("VIERNES", 6, "Ciencias Naturales", "10015"),
            ("VIERNES", 7, "Ciencias Naturales", "10015"),
        ]

        curso = Curso.objects.get(nivel=nombre_curso[0], paralelo=nombre_curso[1])

        for dia, bloque, materia_nombre, ci_profesor in horario_data:
            hora_inicio, hora_salida = bloques[bloque]
            materia = Materia.objects.get(nombre=materia_nombre)
            profesor = Usuario.objects.get(ci=ci_profesor)

            Horario.objects.create(
                gestion=gestion,
                dia_semana=dia,
                hora_inicio=hora_inicio,
                hora_salida=hora_salida,
                id_curso=curso,
                id_materia=materia,
                id_profesor=profesor
            )

        self.stdout.write(self.style.SUCCESS("Horario del curso 4to C creado con éxito."))
