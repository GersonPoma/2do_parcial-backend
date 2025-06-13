from django.core.management.base import BaseCommand
from datetime import date, timedelta
import random

from apps.horario.models import Horario
from apps.alumno_curso.models import AlumnoCurso
from apps.asistencia.models import Asistencia


class Command(BaseCommand):
    help = "Genera asistencias simuladas para el 1er trimestre del año 2025 (90% asistencia)"

    def handle(self, *args, **kwargs):
        fecha_inicio = date(2025, 2, 3)     # Inicio del año escolar 2025
        fecha_fin = date(2025, 4, 3)        # Fin del primer trimestre

        dias_laborales = []
        fecha_actual = fecha_inicio
        while fecha_actual <= fecha_fin:
            if fecha_actual.weekday() < 5:  # Lunes a Viernes
                dias_laborales.append(fecha_actual)
            fecha_actual += timedelta(days=1)

        total_asistencias_creadas = 0
        alumnos = AlumnoCurso.objects.select_related("id_alumno", "id_curso").filter(gestion=2025)

        for alumno_curso in alumnos:
            curso = alumno_curso.id_curso
            horarios = Horario.objects.filter(id_curso=curso, gestion=2025)

            for dia in dias_laborales:
                dia_map = {
                    "MONDAY": "LUNES",
                    "TUESDAY": "MARTES",
                    "WEDNESDAY": "MIERCOLES",
                    "THURSDAY": "JUEVES",
                    "FRIDAY": "VIERNES",
                }

                nombre_dia = dia_map.get(dia.strftime("%A").upper())
                if not nombre_dia:
                    continue

                clases_hoy = horarios.filter(dia_semana=nombre_dia)
                materias_asistidas = set()

                for clase in clases_hoy:
                    if clase.id_materia in materias_asistidas:
                        continue
                    materias_asistidas.add(clase.id_materia)

                    presente = random.random() < 0.90  # 90% probabilidad de estar presente

                    Asistencia.objects.get_or_create(
                        fecha=dia,
                        id_alumno_curso=alumno_curso,
                        id_materia=clase.id_materia,
                        defaults={'presente': presente}
                    )
                    total_asistencias_creadas += 1

        self.stdout.write(self.style.SUCCESS(
            f"🎓 Asistencias creadas para el 1er trimestre de 2025: {total_asistencias_creadas}"
        ))
