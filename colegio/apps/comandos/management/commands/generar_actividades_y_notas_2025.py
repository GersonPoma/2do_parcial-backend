from django.core.management.base import BaseCommand
from datetime import date
import random

from apps.horario.models import Horario
from apps.dimension_evaluada.models import DimensionEvaluada
from apps.actividad.models import Actividad
from apps.alumno_actividad.models import AlumnoActividad
from apps.alumno_curso.models import AlumnoCurso
from apps.resumen_nota.utils import actualizar_resumen_nota


class Command(BaseCommand):
    help = 'Genera actividades y calificaciones simuladas para el 1er trimestre de 2025'

    def handle(self, *args, **kwargs):
        GESTION = 2025
        TRIMESTRE = 1
        FECHA_ENTREGA = date(2025, 4, 3)
        tipos = ['TAREA', 'EXAMEN', 'PRACTICO', 'OTRO']

        dimensiones = DimensionEvaluada.objects.all()
        total_actividades = 0
        total_notas = 0

        # Agrupar por curso, materia y profesor — evita duplicar por bloque/día
        horarios = Horario.objects.filter(gestion=GESTION).select_related('id_curso', 'id_materia', 'id_profesor')
        grupos = set(
            (h.id_curso.id, h.id_materia.id, h.id_profesor.id)
            for h in horarios
        )

        for curso_id, materia_id, profesor_id in grupos:
            curso = Horario.objects.filter(id_curso=curso_id).first().id_curso
            materia = Horario.objects.filter(id_materia=materia_id).first().id_materia
            profesor = Horario.objects.filter(id_profesor=profesor_id).first().id_profesor

            for dimension in dimensiones:
                cantidad = 1 if dimension.nombre == DimensionEvaluada.AUTOEVALUACION else 2

                for n in range(1, cantidad + 1):
                    titulo = f'{dimension.nombre} - {tipos[n % 4]} {n}T{TRIMESTRE}'
                    tipo = tipos[n % 4]

                    actividad = Actividad.objects.create(
                        titulo=titulo,
                        tipo=tipo,
                        fecha_entrega=FECHA_ENTREGA,
                        gestion=GESTION,
                        trimestre=TRIMESTRE,
                        id_materia=materia,
                        id_curso=curso,
                        id_profesor=profesor,
                        id_dimension=dimension
                    )
                    total_actividades += 1

                    alumnos = AlumnoCurso.objects.filter(id_curso=curso, gestion=GESTION).select_related('id_alumno')
                    alumno_actividad_objs = []

                    maximo = float(dimension.puntaje_maximo)

                    for alumno in alumnos:
                        nota = round(random.uniform(maximo * 0.6, maximo), 2)
                        estado = AlumnoActividad.ENTREGADO  # Asumimos entrega puntual

                        obj = AlumnoActividad(
                            id_actividad=actividad,
                            id_alumno_curso=alumno,
                            nota=nota,
                            fecha_entregada=FECHA_ENTREGA,
                            estado=estado
                        )
                        alumno_actividad_objs.append(obj)

                    AlumnoActividad.objects.bulk_create(alumno_actividad_objs, batch_size=1000)
                    total_notas += len(alumno_actividad_objs)

                    for obj in alumno_actividad_objs:
                        actualizar_resumen_nota(obj)

        self.stdout.write(self.style.SUCCESS(
            f"Se crearon {total_actividades} actividades y {total_notas} calificaciones para el 1er trimestre de 2025."
        ))