from collections import defaultdict
from apps.alumno_actividad.models import AlumnoActividad
from apps.dimension_evaluada.models import DimensionEvaluada
from apps.resumen_nota.models import ResumenNota

def calcular_promedio_por_dimension(alumno_curso, materia, trimestre, gestion):
    actividades = AlumnoActividad.objects.filter(
        id_alumno_curso=alumno_curso,
        id_actividad__id_materia=materia,
        id_actividad__trimestre=trimestre,
        id_actividad__gestion=gestion
    ).select_related('id_actividad__id_dimension')

    dimension_notas = defaultdict(list)

    for act in actividades:
        dimension_nombre = act.id_actividad.id_dimension.nombre
        nota = act.nota if act.nota is not None else 0
        dimension_notas[dimension_nombre].append(nota)

    promedios = {}
    for dimension_nombre, _ in DimensionEvaluada.DIMENSIONES:
        notas = dimension_notas.get(dimension_nombre, [])
        promedio = sum(notas) / len(notas) if notas else 0
        promedios[dimension_nombre] = round(promedio, 2)

    return promedios


def calcular_nota_trimestral(promedios_por_dimension):
    return round(sum(promedios_por_dimension.values()), 2)


def actualizar_estado_y_nota_anual(resumen):
    notas = [
        resumen.nota_1erT or 0,
        resumen.nota_2doT or 0,
        resumen.nota_3erT or 0,
    ]
    resumen.nota_anual = round(sum(notas) / 3)

    if all(n is not None for n in [resumen.nota_1erT, resumen.nota_2doT, resumen.nota_3erT]):
        resumen.estado = (
            ResumenNota.APROBADO if resumen.nota_anual >= 51 else ResumenNota.REPROBADO
        )
    else:
        resumen.estado = ResumenNota.EN_PROCESO


def actualizar_resumen_nota(alumno_actividad):
    actividad = alumno_actividad.id_actividad
    alumno_curso = alumno_actividad.id_alumno_curso
    materia = actividad.id_materia
    trimestre = actividad.trimestre
    gestion = actividad.gestion

    resumen, _ = ResumenNota.objects.get_or_create(
        id_alumno_curso=alumno_curso,
        id_materia=materia
    )

    promedios = calcular_promedio_por_dimension(alumno_curso, materia, trimestre, gestion)
    nota_trimestral = calcular_nota_trimestral(promedios)

    if trimestre == 1:
        resumen.nota_1erT = nota_trimestral
    elif trimestre == 2:
        resumen.nota_2doT = nota_trimestral
    elif trimestre == 3:
        resumen.nota_3erT = nota_trimestral

    actualizar_estado_y_nota_anual(resumen)
    resumen.save()
