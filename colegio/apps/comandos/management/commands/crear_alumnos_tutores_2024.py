from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from random import randint, choice
from datetime import date

from apps.usuario.models import Usuario
from apps.curso.models import Curso
from apps.alumno_curso.models import AlumnoCurso


class Command(BaseCommand):
    help = 'Crear alumnos promovidos y nuevos para 2024'

    def handle(self, *args, **kwargs):
        nombres = ['Juan', 'María', 'Luis', 'Ana', 'Carlos', 'Laura', 'Pedro', 'Marta', 'Diego', 'Sofía', 'José', 'Elena', 'Marco', 'Paola']
        apellidos = ['Gómez', 'Fernández', 'Rojas', 'Quispe', 'Mamani', 'Salazar', 'Cortez', 'Vargas', 'Navarro', 'Ortega', 'Pérez', 'Castro']

        niveles_2023 = ['1ro', '2do', '3ro']
        niveles_2024 = {'1ro': '2do', '2do': '3ro', '3ro': '4to'}
        paralelos = ['A', 'B', 'C']
        gestion_nueva = 2024
        total_nuevos = 0
        total_promovidos = 0

        # PROMOVER alumnos del 2023 a un nivel superior en 2024
        for nivel_2023 in niveles_2023:
            nivel_2024 = niveles_2024[nivel_2023]
            for paralelo in paralelos:
                curso_anterior = Curso.objects.get(nivel=nivel_2023, paralelo=paralelo)
                curso_nuevo = Curso.objects.get(nivel=nivel_2024, paralelo=paralelo)

                alumnos_2023 = AlumnoCurso.objects.filter(gestion=2023, id_curso=curso_anterior)

                for registro in alumnos_2023:
                    AlumnoCurso.objects.create(
                        gestion=gestion_nueva,
                        id_alumno=registro.id_alumno,
                        id_curso=curso_nuevo
                    )
                    total_promovidos += 1

        # CREAR 60 NUEVOS alumnos con sus tutores para 1ro A/B/C en 2024
        ci_alumno = Usuario.objects.filter(rol=Usuario.ALUMNO).order_by('-ci').first()
        ci_tutor = Usuario.objects.filter(rol=Usuario.TUTOR).order_by('-ci').first()
        ci_alumno = int(ci_alumno.ci) + 1 if ci_alumno else 8000000
        ci_tutor = int(ci_tutor.ci) + 1 if ci_tutor else 9000000

        password_alumno = 'Alumno2024'
        password_tutor = 'Tutor2024'

        for paralelo in paralelos:
            curso = Curso.objects.get(nivel='1ro', paralelo=paralelo)

            for _ in range(20):
                nombre_alumno = choice(nombres)
                apellido_alumno = choice(apellidos)
                fecha_nac_alumno = date(2012, randint(1, 12), randint(1, 28))  # Aprox. 12 años en 2024

                nombre_tutor = choice(nombres)
                apellido_tutor = choice(apellidos)
                fecha_nac_tutor = date(randint(1975, 1990), randint(1, 12), randint(1, 28))
                telefono = f"7{randint(1000000, 9999999)}"
                direccion = f"Calle {choice(['Junín', 'Sucre', 'Ayacucho', 'Colón'])} #{randint(100, 999)}, Santa Cruz"
                correo_tutor = f"{nombre_tutor.lower()}.{apellido_tutor.lower()}@gmail.com"

                tutor = Usuario.objects.create_user(
                    username=str(ci_tutor),
                    password=password_tutor,
                    ci=str(ci_tutor),
                    nombre=nombre_tutor,
                    apellido=apellido_tutor,
                    rol=Usuario.TUTOR,
                    fecha_nacimiento=fecha_nac_tutor,
                    telefono=telefono,
                    direccion=direccion,
                    correo=correo_tutor,
                    is_active=True
                )
                ci_tutor += 1

                correo_alumno = f"{nombre_alumno.lower()}.{apellido_alumno.lower()}@gmail.com"
                telefono_alumno = telefono if randint(0, 1) else None
                direccion_alumno = direccion

                alumno = Usuario.objects.create_user(
                    username=str(ci_alumno),
                    password=password_alumno,
                    ci=str(ci_alumno),
                    nombre=nombre_alumno,
                    apellido=apellido_alumno,
                    rol=Usuario.ALUMNO,
                    fecha_nacimiento=fecha_nac_alumno,
                    telefono=telefono_alumno,
                    direccion=direccion_alumno,
                    correo=correo_alumno,
                    tutor=tutor,
                    is_active=True
                )
                ci_alumno += 1

                AlumnoCurso.objects.create(
                    gestion=gestion_nueva,
                    id_alumno=alumno,
                    id_curso=curso
                )
                total_nuevos += 1

                self.stdout.write(self.style.SUCCESS(
                    f"Alumno nuevo creado: {alumno.nombre} {alumno.apellido} - 1ro {paralelo}"
                ))

        self.stdout.write(self.style.SUCCESS(
            f"Total promovidos: {total_promovidos} | Nuevos alumnos: {total_nuevos} en gestión {gestion_nueva}"
        ))
