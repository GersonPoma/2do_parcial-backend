from apps.alumno_curso.models import AlumnoCurso
from apps.notificacion.utils import enviar_notificacion_push


def notificar_alumno_actividad(instance, old_nota=None):
    actividad = instance.id_actividad
    materia = actividad.id_materia.nombre
    titulo_actividad = actividad.titulo
    dimension = actividad.id_dimension.nombre

    if dimension not in ['Hacer', 'Saber']:
        return

    alumno = instance.id_alumno_curso.id_alumno
    tokens = alumno.dispositivos.values_list('token', flat=True)
    if not tokens or instance.nota is None:
        return

    if old_nota is None:
        titulo = f"Actividad {titulo_actividad} calificada"
        mensaje = f"La actividad {titulo_actividad} de la materia {materia} ha sido calificada."
    elif instance.nota != old_nota:
        titulo = "Nota actualizada"
        mensaje = f"La nota de la actividad {titulo_actividad} en la materia {materia} ha sido modificada."
    else:
        return

    enviar_notificacion_push(
        tokens,
        titulo=titulo,
        mensaje=mensaje,
        data={
            "actividad_id": actividad.id,
            "materia": materia,
            "titulo_actividad": titulo_actividad,
        }
    )

def notificar_actividad_creada(actividad):
    if actividad.id_dimension.nombre not in ['Hacer', 'Saber']:
        return

    materia = actividad.id_materia.nombre
    titulo = actividad.titulo

    alumnos_curso = AlumnoCurso.objects.filter(
        id_curso=actividad.id_curso,
        gestion=actividad.gestion
    ).select_related('id_alumno')

    for ac in alumnos_curso:
        alumno = ac.id_alumno
        tokens = alumno.dispositivos.values_list('token', flat=True)
        if not tokens:
            continue

        enviar_notificacion_push(
            tokens,
            titulo="Actividad creada",
            mensaje=f"Se ha creado una nueva actividad '{titulo}' para la materia {materia}.",
            data={
                "actividad_id": actividad.id,
                "materia": materia,
                "titulo_actividad": titulo,
                "tipo": "actividad_creada"
            }
        )

def notificar_tutor_alumno_actividad(instance, old_nota=None):
    actividad = instance.id_actividad
    dimension = actividad.id_dimension.nombre
    if dimension not in ['Hacer', 'Saber']:
        return

    alumno = instance.id_alumno_curso.id_alumno
    tutor = alumno.tutor

    if not tutor:
        return  # el alumno no tiene tutor asignado

    materia = actividad.id_materia.nombre
    titulo_actividad = actividad.titulo

    if instance.nota is None:
        return

    if old_nota is None:
        titulo = f"{alumno.get_nombre_completo} calificado"
        mensaje = f"{alumno.get_nombre_completo} ha recibido una nota en {titulo_actividad} ({materia})."
    elif instance.nota != old_nota:
        titulo = f"Nota de {alumno.get_nombre_completo} actualizada"
        mensaje = f"La nota de {alumno.get_nombre_completo} en {titulo_actividad} ({materia}) ha sido modificada."
    else:
        return

    tokens = tutor.dispositivos.values_list('token', flat=True)
    if tokens:
        enviar_notificacion_push(
            tokens,
            titulo=titulo,
            mensaje=mensaje,
            data={
                "actividad_id": actividad.id,
                "materia": materia,
                "titulo_actividad": titulo_actividad,
                "alumno": alumno.get_nombre_completo,
                "tipo": "nota_tutor"
            }
        )

def notificar_tutores_actividad_creada(actividad):
    if actividad.id_dimension.nombre not in ['Hacer', 'Saber']:
        return

    materia = actividad.id_materia.nombre
    titulo = actividad.titulo

    alumnos_curso = AlumnoCurso.objects.filter(
        id_curso=actividad.id_curso,
        gestion=actividad.gestion
    ).select_related('id_alumno')

    for ac in alumnos_curso:
        alumno = ac.id_alumno
        tutor = alumno.tutor
        if not tutor:
            continue

        tokens = tutor.dispositivos.values_list('token', flat=True)
        if not tokens:
            continue

        enviar_notificacion_push(
            tokens,
            titulo="Actividad asignada",
            mensaje=f"A {alumno.get_nombre_completo} se le asignó '{titulo}' en {materia}.",
            data={
                "actividad_id": actividad.id,
                "materia": materia,
                "titulo_actividad": titulo,
                "alumno": alumno.get_nombre_completo,
                "tipo": "actividad_tutor"
            }
        )
