from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from apps.usuario.models import Usuario
from apps.curso.models import Curso
from apps.alumno_curso.models import AlumnoCurso

class Command(BaseCommand):
    help = 'Crea 240 alumnos y 240 tutores únicos, asignando 20 alumnos por curso desde 1ro A hasta 4to C (2022)'

    def handle(self, *args, **kwargs):
        curso_1ro_A = Curso.objects.get(nivel='1ro', paralelo='A')
        curso_1ro_B = Curso.objects.get(nivel='1ro', paralelo='B')
        curso_1ro_C = Curso.objects.get(nivel='1ro', paralelo='C')
        curso_2do_A = Curso.objects.get(nivel='2do', paralelo='A')
        curso_2do_B = Curso.objects.get(nivel='2do', paralelo='B')
        curso_2do_C = Curso.objects.get(nivel='2do', paralelo='C')
        curso_3ro_A = Curso.objects.get(nivel='3ro', paralelo='A')
        curso_3ro_B = Curso.objects.get(nivel='3ro', paralelo='B')
        curso_3ro_C = Curso.objects.get(nivel='3ro', paralelo='C')
        curso_4to_A = Curso.objects.get(nivel='4to', paralelo='A')
        curso_4to_B = Curso.objects.get(nivel='4to', paralelo='B')
        curso_4to_C = Curso.objects.get(nivel='4to', paralelo='C')

        tutor_1 = Usuario.objects.create_user(
            username='9000001',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000001',
            nombre='Ana',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-04-11', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            is_active=True
        )
        alumno_1 = Usuario.objects.create_user(
            username='8000001',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000001',
            nombre='María',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='75879299' if '75879299' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-20', '%Y-%m-%d')),
            correo='maría.garcía@gmail.com',
            tutor=tutor_1,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_1, id_curso=curso_1ro_A)
        tutor_2 = Usuario.objects.create_user(
            username='9000002',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000002',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='75766041' if '75766041' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-12-28', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            is_active=True
        )
        alumno_2 = Usuario.objects.create_user(
            username='8000002',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000002',
            nombre='Marco',
            apellido='Pérez',
            direccion='Av. Virgen de Cotoca',
            telefono='68731317' if '68731317' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-22', '%Y-%m-%d')),
            correo='marco.pérez@gmail.com',
            tutor=tutor_2,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_2, id_curso=curso_1ro_A)
        tutor_3 = Usuario.objects.create_user(
            username='9000003',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000003',
            nombre='Ana',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1983-03-10', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_3 = Usuario.objects.create_user(
            username='8000003',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000003',
            nombre='Marco',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-27', '%Y-%m-%d')),
            correo='marco.soto@gmail.com',
            tutor=tutor_3,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_3, id_curso=curso_1ro_A)
        tutor_4 = Usuario.objects.create_user(
            username='9000004',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000004',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='72544402' if '72544402' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1972-11-14', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_4 = Usuario.objects.create_user(
            username='8000004',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000004',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-10', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            tutor=tutor_4,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_4, id_curso=curso_1ro_A)
        tutor_5 = Usuario.objects.create_user(
            username='9000005',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000005',
            nombre='María',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-06-15', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_5 = Usuario.objects.create_user(
            username='8000005',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000005',
            nombre='Carlos',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='66158599' if '66158599' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-23', '%Y-%m-%d')),
            correo='carlos.mamani@gmail.com',
            tutor=tutor_5,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_5, id_curso=curso_1ro_A)
        tutor_6 = Usuario.objects.create_user(
            username='9000006',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000006',
            nombre='Pedro',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='62394728' if '62394728' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-27', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            is_active=True
        )
        alumno_6 = Usuario.objects.create_user(
            username='8000006',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000006',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Barrio Los Chacos',
            telefono='76080515' if '76080515' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-02', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            tutor=tutor_6,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_6, id_curso=curso_1ro_A)
        tutor_7 = Usuario.objects.create_user(
            username='9000007',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000007',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1995-03-29', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_7 = Usuario.objects.create_user(
            username='8000007',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000007',
            nombre='Pedro',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='68672404' if '68672404' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-22', '%Y-%m-%d')),
            correo='pedro.mamani@gmail.com',
            tutor=tutor_7,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_7, id_curso=curso_1ro_A)
        tutor_8 = Usuario.objects.create_user(
            username='9000008',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000008',
            nombre='María',
            apellido='Soto',
            direccion='Zona Centro',
            telefono='74301771' if '74301771' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1979-10-22', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            is_active=True
        )
        alumno_8 = Usuario.objects.create_user(
            username='8000008',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000008',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-09-09', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            tutor=tutor_8,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_8, id_curso=curso_1ro_A)
        tutor_9 = Usuario.objects.create_user(
            username='9000009',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000009',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='64534614' if '64534614' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-11-15', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            is_active=True
        )
        alumno_9 = Usuario.objects.create_user(
            username='8000009',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000009',
            nombre='María',
            apellido='Flores',
            direccion='Zona Centro',
            telefono='73730729' if '73730729' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-25', '%Y-%m-%d')),
            correo='maría.flores@gmail.com',
            tutor=tutor_9,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_9, id_curso=curso_1ro_A)
        tutor_10 = Usuario.objects.create_user(
            username='9000010',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000010',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='77998363' if '77998363' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1996-04-08', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_10 = Usuario.objects.create_user(
            username='8000010',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000010',
            nombre='Pedro',
            apellido='García',
            direccion='Av. Virgen de Cotoca',
            telefono='70295992' if '70295992' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-22', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            tutor=tutor_10,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_10, id_curso=curso_1ro_A)
        tutor_11 = Usuario.objects.create_user(
            username='9000011',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000011',
            nombre='Carlos',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-07-05', '%Y-%m-%d')),
            correo='carlos.gómez@gmail.com',
            is_active=True
        )
        alumno_11 = Usuario.objects.create_user(
            username='8000011',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000011',
            nombre='Laura',
            apellido='Vargas',
            direccion='Av. Roca y Coronado',
            telefono='66567572' if '66567572' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-23', '%Y-%m-%d')),
            correo='laura.vargas@gmail.com',
            tutor=tutor_11,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_11, id_curso=curso_1ro_A)
        tutor_12 = Usuario.objects.create_user(
            username='9000012',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000012',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='66958746' if '66958746' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-05', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            is_active=True
        )
        alumno_12 = Usuario.objects.create_user(
            username='8000012',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000012',
            nombre='Pedro',
            apellido='Mamani',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-28', '%Y-%m-%d')),
            correo='pedro.mamani@gmail.com',
            tutor=tutor_12,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_12, id_curso=curso_1ro_A)
        tutor_13 = Usuario.objects.create_user(
            username='9000013',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000013',
            nombre='Jorge',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='71446348' if '71446348' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-12-03', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            is_active=True
        )
        alumno_13 = Usuario.objects.create_user(
            username='8000013',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000013',
            nombre='Jorge',
            apellido='Flores',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-11-05', '%Y-%m-%d')),
            correo='jorge.flores@gmail.com',
            tutor=tutor_13,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_13, id_curso=curso_1ro_A)
        tutor_14 = Usuario.objects.create_user(
            username='9000014',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000014',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-10-10', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_14 = Usuario.objects.create_user(
            username='8000014',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000014',
            nombre='Luis',
            apellido='García',
            direccion='Barrio Equipetrol',
            telefono='69494504' if '69494504' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-09', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            tutor=tutor_14,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_14, id_curso=curso_1ro_A)
        tutor_15 = Usuario.objects.create_user(
            username='9000015',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000015',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='63426945' if '63426945' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-08-20', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_15 = Usuario.objects.create_user(
            username='8000015',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000015',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-20', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            tutor=tutor_15,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_15, id_curso=curso_1ro_A)
        tutor_16 = Usuario.objects.create_user(
            username='9000016',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000016',
            nombre='Elena',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='75989064' if '75989064' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-11-30', '%Y-%m-%d')),
            correo='elena.mamani@gmail.com',
            is_active=True
        )
        alumno_16 = Usuario.objects.create_user(
            username='8000016',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000016',
            nombre='Lucía',
            apellido='Flores',
            direccion='Av. Banzer',
            telefono='64162569' if '64162569' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-14', '%Y-%m-%d')),
            correo='lucía.flores@gmail.com',
            tutor=tutor_16,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_16, id_curso=curso_1ro_A)
        tutor_17 = Usuario.objects.create_user(
            username='9000017',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000017',
            nombre='Carlos',
            apellido='Flores',
            direccion='Av. Cristo Redentor',
            telefono='63663050' if '63663050' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-08-01', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            is_active=True
        )
        alumno_17 = Usuario.objects.create_user(
            username='8000017',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000017',
            nombre='Ana',
            apellido='Vargas',
            direccion='Av. Roca y Coronado',
            telefono='75277425' if '75277425' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-23', '%Y-%m-%d')),
            correo='ana.vargas@gmail.com',
            tutor=tutor_17,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_17, id_curso=curso_1ro_A)
        tutor_18 = Usuario.objects.create_user(
            username='9000018',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000018',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-07-14', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            is_active=True
        )
        alumno_18 = Usuario.objects.create_user(
            username='8000018',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000018',
            nombre='Jorge',
            apellido='Quispe',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-09-13', '%Y-%m-%d')),
            correo='jorge.quispe@gmail.com',
            tutor=tutor_18,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_18, id_curso=curso_1ro_A)
        tutor_19 = Usuario.objects.create_user(
            username='9000019',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000019',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-08-12', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_19 = Usuario.objects.create_user(
            username='8000019',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000019',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-09-30', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            tutor=tutor_19,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_19, id_curso=curso_1ro_A)
        tutor_20 = Usuario.objects.create_user(
            username='9000020',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000020',
            nombre='Luis',
            apellido='García',
            direccion='Zona Centro',
            telefono='63376286' if '63376286' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-07-17', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            is_active=True
        )
        alumno_20 = Usuario.objects.create_user(
            username='8000020',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000020',
            nombre='Carlos',
            apellido='Pérez',
            direccion='Barrio Equipetrol',
            telefono='69297545' if '69297545' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-13', '%Y-%m-%d')),
            correo='carlos.pérez@gmail.com',
            tutor=tutor_20,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_20, id_curso=curso_1ro_A)
        tutor_21 = Usuario.objects.create_user(
            username='9000021',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000021',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-11', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            is_active=True
        )
        alumno_21 = Usuario.objects.create_user(
            username='8000021',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000021',
            nombre='María',
            apellido='Pérez',
            direccion='Zona Centro',
            telefono='69845842' if '69845842' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-30', '%Y-%m-%d')),
            correo='maría.pérez@gmail.com',
            tutor=tutor_21,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_21, id_curso=curso_1ro_B)
        tutor_22 = Usuario.objects.create_user(
            username='9000022',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000022',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='77187077' if '77187077' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_22 = Usuario.objects.create_user(
            username='8000022',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000022',
            nombre='Carlos',
            apellido='Pérez',
            direccion='Barrio Equipetrol',
            telefono='64432080' if '64432080' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-14', '%Y-%m-%d')),
            correo='carlos.pérez@gmail.com',
            tutor=tutor_22,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_22, id_curso=curso_1ro_B)
        tutor_23 = Usuario.objects.create_user(
            username='9000023',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000023',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='73436319' if '73436319' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-08-11', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            is_active=True
        )
        alumno_23 = Usuario.objects.create_user(
            username='8000023',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000023',
            nombre='Pedro',
            apellido='Pérez',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-12', '%Y-%m-%d')),
            correo='pedro.pérez@gmail.com',
            tutor=tutor_23,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_23, id_curso=curso_1ro_B)
        tutor_24 = Usuario.objects.create_user(
            username='9000024',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000024',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-06', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            is_active=True
        )
        alumno_24 = Usuario.objects.create_user(
            username='8000024',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000024',
            nombre='María',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-05-20', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            tutor=tutor_24,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_24, id_curso=curso_1ro_B)
        tutor_25 = Usuario.objects.create_user(
            username='9000025',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000025',
            nombre='Marco',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='61618380' if '61618380' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-10-02', '%Y-%m-%d')),
            correo='marco.soto@gmail.com',
            is_active=True
        )
        alumno_25 = Usuario.objects.create_user(
            username='8000025',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000025',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='64487275' if '64487275' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-11-12', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            tutor=tutor_25,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_25, id_curso=curso_1ro_B)
        tutor_26 = Usuario.objects.create_user(
            username='9000026',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000026',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-01-22', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            is_active=True
        )
        alumno_26 = Usuario.objects.create_user(
            username='8000026',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000026',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-24', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            tutor=tutor_26,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_26, id_curso=curso_1ro_B)
        tutor_27 = Usuario.objects.create_user(
            username='9000027',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000027',
            nombre='Luis',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='65242022' if '65242022' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-03-10', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            is_active=True
        )
        alumno_27 = Usuario.objects.create_user(
            username='8000027',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000027',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Equipetrol',
            telefono='69088675' if '69088675' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-04', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            tutor=tutor_27,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_27, id_curso=curso_1ro_B)
        tutor_28 = Usuario.objects.create_user(
            username='9000028',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000028',
            nombre='Jorge',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='61832169' if '61832169' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1987-09-29', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            is_active=True
        )
        alumno_28 = Usuario.objects.create_user(
            username='8000028',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000028',
            nombre='Laura',
            apellido='Gómez',
            direccion='Zona El Trompillo',
            telefono='65618391' if '65618391' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-05-11', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            tutor=tutor_28,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_28, id_curso=curso_1ro_B)
        tutor_29 = Usuario.objects.create_user(
            username='9000029',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000029',
            nombre='Luis',
            apellido='Flores',
            direccion='Zona El Trompillo',
            telefono='60244304' if '60244304' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-08-26', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            is_active=True
        )
        alumno_29 = Usuario.objects.create_user(
            username='8000029',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000029',
            nombre='Lucía',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='72804144' if '72804144' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-30', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            tutor=tutor_29,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_29, id_curso=curso_1ro_B)
        tutor_30 = Usuario.objects.create_user(
            username='9000030',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000030',
            nombre='Luis',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='74103407' if '74103407' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-05-11', '%Y-%m-%d')),
            correo='luis.mamani@gmail.com',
            is_active=True
        )
        alumno_30 = Usuario.objects.create_user(
            username='8000030',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000030',
            nombre='Pedro',
            apellido='Gómez',
            direccion='Av. Roca y Coronado',
            telefono='61157467' if '61157467' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-14', '%Y-%m-%d')),
            correo='pedro.gómez@gmail.com',
            tutor=tutor_30,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_30, id_curso=curso_1ro_B)
        tutor_31 = Usuario.objects.create_user(
            username='9000031',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000031',
            nombre='Laura',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='75904215' if '75904215' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-12-14', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            is_active=True
        )
        alumno_31 = Usuario.objects.create_user(
            username='8000031',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000031',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Av. Virgen de Cotoca',
            telefono='62038195' if '62038195' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-05-18', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            tutor=tutor_31,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_31, id_curso=curso_1ro_B)
        tutor_32 = Usuario.objects.create_user(
            username='9000032',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000032',
            nombre='Laura',
            apellido='Flores',
            direccion='Av. Roca y Coronado',
            telefono='63497745' if '63497745' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-09-01', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_32 = Usuario.objects.create_user(
            username='8000032',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000032',
            nombre='Ana',
            apellido='Gómez',
            direccion='Barrio Los Chacos',
            telefono='68634761' if '68634761' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-07-19', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            tutor=tutor_32,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_32, id_curso=curso_1ro_B)
        tutor_33 = Usuario.objects.create_user(
            username='9000033',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000033',
            nombre='Laura',
            apellido='García',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1973-07-18', '%Y-%m-%d')),
            correo='laura.garcía@gmail.com',
            is_active=True
        )
        alumno_33 = Usuario.objects.create_user(
            username='8000033',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000033',
            nombre='Marco',
            apellido='Vargas',
            direccion='Av. Cristo Redentor',
            telefono='66181767' if '66181767' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-21', '%Y-%m-%d')),
            correo='marco.vargas@gmail.com',
            tutor=tutor_33,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_33, id_curso=curso_1ro_B)
        tutor_34 = Usuario.objects.create_user(
            username='9000034',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000034',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-12-18', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_34 = Usuario.objects.create_user(
            username='8000034',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000034',
            nombre='Marco',
            apellido='Vargas',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-20', '%Y-%m-%d')),
            correo='marco.vargas@gmail.com',
            tutor=tutor_34,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_34, id_curso=curso_1ro_B)
        tutor_35 = Usuario.objects.create_user(
            username='9000035',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000035',
            nombre='Laura',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='66177430' if '66177430' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1969-06-18', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            is_active=True
        )
        alumno_35 = Usuario.objects.create_user(
            username='8000035',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000035',
            nombre='Lucía',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='74548478' if '74548478' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-01-17', '%Y-%m-%d')),
            correo='lucía.garcía@gmail.com',
            tutor=tutor_35,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_35, id_curso=curso_1ro_B)
        tutor_36 = Usuario.objects.create_user(
            username='9000036',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000036',
            nombre='Luis',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='66942628' if '66942628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-03', '%Y-%m-%d')),
            correo='luis.torres@gmail.com',
            is_active=True
        )
        alumno_36 = Usuario.objects.create_user(
            username='8000036',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000036',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='73558841' if '73558841' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-26', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            tutor=tutor_36,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_36, id_curso=curso_1ro_B)
        tutor_37 = Usuario.objects.create_user(
            username='9000037',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000037',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1980-09-15', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_37 = Usuario.objects.create_user(
            username='8000037',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000037',
            nombre='Luis',
            apellido='García',
            direccion='Av. Virgen de Cotoca',
            telefono='64537041' if '64537041' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-13', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            tutor=tutor_37,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_37, id_curso=curso_1ro_B)
        tutor_38 = Usuario.objects.create_user(
            username='9000038',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000038',
            nombre='Pedro',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='70061577' if '70061577' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-08-12', '%Y-%m-%d')),
            correo='pedro.pérez@gmail.com',
            is_active=True
        )
        alumno_38 = Usuario.objects.create_user(
            username='8000038',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000038',
            nombre='Laura',
            apellido='Mamani',
            direccion='Zona Centro',
            telefono='61064755' if '61064755' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-30', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            tutor=tutor_38,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_38, id_curso=curso_1ro_B)
        tutor_39 = Usuario.objects.create_user(
            username='9000039',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000039',
            nombre='María',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='69278628' if '69278628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-08', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_39 = Usuario.objects.create_user(
            username='8000039',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000039',
            nombre='María',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-20', '%Y-%m-%d')),
            correo='maría.rojas@gmail.com',
            tutor=tutor_39,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_39, id_curso=curso_1ro_B)
        tutor_40 = Usuario.objects.create_user(
            username='9000040',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000040',
            nombre='Laura',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='62142118' if '62142118' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1988-05-30', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_40 = Usuario.objects.create_user(
            username='8000040',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000040',
            nombre='Marco',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='76928408' if '76928408' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-10-17', '%Y-%m-%d')),
            correo='marco.vargas@gmail.com',
            tutor=tutor_40,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_40, id_curso=curso_1ro_B)
        tutor_41 = Usuario.objects.create_user(
            username='9000041',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000041',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Av. Virgen de Cotoca',
            telefono='78074961' if '78074961' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-06-23', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_41 = Usuario.objects.create_user(
            username='8000041',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000041',
            nombre='Pedro',
            apellido='Mamani',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-15', '%Y-%m-%d')),
            correo='pedro.mamani@gmail.com',
            tutor=tutor_41,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_41, id_curso=curso_1ro_C)
        tutor_42 = Usuario.objects.create_user(
            username='9000042',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000042',
            nombre='Luis',
            apellido='Gómez',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-07-20', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            is_active=True
        )
        alumno_42 = Usuario.objects.create_user(
            username='8000042',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000042',
            nombre='Pedro',
            apellido='Gómez',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-07-12', '%Y-%m-%d')),
            correo='pedro.gómez@gmail.com',
            tutor=tutor_42,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_42, id_curso=curso_1ro_C)
        tutor_43 = Usuario.objects.create_user(
            username='9000043',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000043',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='70508550' if '70508550' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-08-08', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            is_active=True
        )
        alumno_43 = Usuario.objects.create_user(
            username='8000043',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000043',
            nombre='Laura',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='64784062' if '64784062' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-17', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            tutor=tutor_43,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_43, id_curso=curso_1ro_C)
        tutor_44 = Usuario.objects.create_user(
            username='9000044',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000044',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='68713474' if '68713474' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-11-03', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            is_active=True
        )
        alumno_44 = Usuario.objects.create_user(
            username='8000044',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000044',
            nombre='Ana',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-07-02', '%Y-%m-%d')),
            correo='ana.flores@gmail.com',
            tutor=tutor_44,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_44, id_curso=curso_1ro_C)
        tutor_45 = Usuario.objects.create_user(
            username='9000045',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000045',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-05-15', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            is_active=True
        )
        alumno_45 = Usuario.objects.create_user(
            username='8000045',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000045',
            nombre='Elena',
            apellido='García',
            direccion='Barrio Equipetrol',
            telefono='76844993' if '76844993' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-04', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            tutor=tutor_45,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_45, id_curso=curso_1ro_C)
        tutor_46 = Usuario.objects.create_user(
            username='9000046',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000046',
            nombre='Laura',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='66635150' if '66635150' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-06-06', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            is_active=True
        )
        alumno_46 = Usuario.objects.create_user(
            username='8000046',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000046',
            nombre='Luis',
            apellido='Pérez',
            direccion='Av. Roca y Coronado',
            telefono='75270648' if '75270648' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-31', '%Y-%m-%d')),
            correo='luis.pérez@gmail.com',
            tutor=tutor_46,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_46, id_curso=curso_1ro_C)
        tutor_47 = Usuario.objects.create_user(
            username='9000047',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000047',
            nombre='Elena',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='79850106' if '79850106' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-08', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            is_active=True
        )
        alumno_47 = Usuario.objects.create_user(
            username='8000047',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000047',
            nombre='Laura',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='78981609' if '78981609' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-11-07', '%Y-%m-%d')),
            correo='laura.vargas@gmail.com',
            tutor=tutor_47,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_47, id_curso=curso_1ro_C)
        tutor_48 = Usuario.objects.create_user(
            username='9000048',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000048',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='73036060' if '73036060' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1966-12-30', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            is_active=True
        )
        alumno_48 = Usuario.objects.create_user(
            username='8000048',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000048',
            nombre='Laura',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-05-01', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            tutor=tutor_48,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_48, id_curso=curso_1ro_C)
        tutor_49 = Usuario.objects.create_user(
            username='9000049',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000049',
            nombre='Marco',
            apellido='Torres',
            direccion='Barrio Urbarí',
            telefono='71097732' if '71097732' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-14', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_49 = Usuario.objects.create_user(
            username='8000049',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000049',
            nombre='Elena',
            apellido='García',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-01-04', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            tutor=tutor_49,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_49, id_curso=curso_1ro_C)
        tutor_50 = Usuario.objects.create_user(
            username='9000050',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000050',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='64804300' if '64804300' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-08-06', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_50 = Usuario.objects.create_user(
            username='8000050',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000050',
            nombre='Marco',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='70255008' if '70255008' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-02-28', '%Y-%m-%d')),
            correo='marco.garcía@gmail.com',
            tutor=tutor_50,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_50, id_curso=curso_1ro_C)
        tutor_51 = Usuario.objects.create_user(
            username='9000051',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000051',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            is_active=True
        )
        alumno_51 = Usuario.objects.create_user(
            username='8000051',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000051',
            nombre='Luis',
            apellido='Quispe',
            direccion='Av. Banzer',
            telefono='75646965' if '75646965' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-12-02', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            tutor=tutor_51,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_51, id_curso=curso_1ro_C)
        tutor_52 = Usuario.objects.create_user(
            username='9000052',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000052',
            nombre='Marco',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='69945029' if '69945029' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-09-30', '%Y-%m-%d')),
            correo='marco.quispe@gmail.com',
            is_active=True
        )
        alumno_52 = Usuario.objects.create_user(
            username='8000052',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000052',
            nombre='Carlos',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-08-22', '%Y-%m-%d')),
            correo='carlos.quispe@gmail.com',
            tutor=tutor_52,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_52, id_curso=curso_1ro_C)
        tutor_53 = Usuario.objects.create_user(
            username='9000053',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000053',
            nombre='Marco',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='72420478' if '72420478' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1993-12-22', '%Y-%m-%d')),
            correo='marco.flores@gmail.com',
            is_active=True
        )
        alumno_53 = Usuario.objects.create_user(
            username='8000053',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000053',
            nombre='Jorge',
            apellido='Pérez',
            direccion='Zona Centro',
            telefono='73331473' if '73331473' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-07-11', '%Y-%m-%d')),
            correo='jorge.pérez@gmail.com',
            tutor=tutor_53,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_53, id_curso=curso_1ro_C)
        tutor_54 = Usuario.objects.create_user(
            username='9000054',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000054',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='67877721' if '67877721' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-11-21', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            is_active=True
        )
        alumno_54 = Usuario.objects.create_user(
            username='8000054',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000054',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio 4 de Noviembre',
            telefono='73131371' if '73131371' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-14', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            tutor=tutor_54,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_54, id_curso=curso_1ro_C)
        tutor_55 = Usuario.objects.create_user(
            username='9000055',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000055',
            nombre='Ana',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-05-02', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_55 = Usuario.objects.create_user(
            username='8000055',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000055',
            nombre='Luis',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='61787590' if '61787590' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-05-08', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_55,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_55, id_curso=curso_1ro_C)
        tutor_56 = Usuario.objects.create_user(
            username='9000056',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000056',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-10-14', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            is_active=True
        )
        alumno_56 = Usuario.objects.create_user(
            username='8000056',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000056',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='60503917' if '60503917' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-06-22', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            tutor=tutor_56,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_56, id_curso=curso_1ro_C)
        tutor_57 = Usuario.objects.create_user(
            username='9000057',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000057',
            nombre='Marco',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='67388847' if '67388847' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-02-23', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_57 = Usuario.objects.create_user(
            username='8000057',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000057',
            nombre='Luis',
            apellido='Pérez',
            direccion='Zona Centro',
            telefono='73481168' if '73481168' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-18', '%Y-%m-%d')),
            correo='luis.pérez@gmail.com',
            tutor=tutor_57,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_57, id_curso=curso_1ro_C)
        tutor_58 = Usuario.objects.create_user(
            username='9000058',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000058',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Zona El Trompillo',
            telefono='61748434' if '61748434' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-10-01', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_58 = Usuario.objects.create_user(
            username='8000058',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000058',
            nombre='Pedro',
            apellido='Quispe',
            direccion='Zona Centro',
            telefono='63568670' if '63568670' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-24', '%Y-%m-%d')),
            correo='pedro.quispe@gmail.com',
            tutor=tutor_58,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_58, id_curso=curso_1ro_C)
        tutor_59 = Usuario.objects.create_user(
            username='9000059',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000059',
            nombre='Elena',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='74166864' if '74166864' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-29', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            is_active=True
        )
        alumno_59 = Usuario.objects.create_user(
            username='8000059',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000059',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Virgen de Cotoca',
            telefono='73847892' if '73847892' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-03-17', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            tutor=tutor_59,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_59, id_curso=curso_1ro_C)
        tutor_60 = Usuario.objects.create_user(
            username='9000060',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000060',
            nombre='Laura',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='71224148' if '71224148' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-14', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_60 = Usuario.objects.create_user(
            username='8000060',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000060',
            nombre='Pedro',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2010-04-26', '%Y-%m-%d')),
            correo='pedro.soto@gmail.com',
            tutor=tutor_60,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_60, id_curso=curso_1ro_C)
        tutor_61 = Usuario.objects.create_user(
            username='9000061',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000061',
            nombre='Ana',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-04-11', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            is_active=True
        )
        alumno_61 = Usuario.objects.create_user(
            username='8000061',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000061',
            nombre='Luis',
            apellido='Pérez',
            direccion='Av. Virgen de Cotoca',
            telefono='67044392' if '67044392' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-21', '%Y-%m-%d')),
            correo='luis.pérez@gmail.com',
            tutor=tutor_61,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_61, id_curso=curso_2do_A)
        tutor_62 = Usuario.objects.create_user(
            username='9000062',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000062',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='75766041' if '75766041' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-12-28', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            is_active=True
        )
        alumno_62 = Usuario.objects.create_user(
            username='8000062',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000062',
            nombre='Jorge',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='72088590' if '72088590' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-02-23', '%Y-%m-%d')),
            correo='jorge.rojas@gmail.com',
            tutor=tutor_62,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_62, id_curso=curso_2do_A)
        tutor_63 = Usuario.objects.create_user(
            username='9000063',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000063',
            nombre='Ana',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1983-03-10', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_63 = Usuario.objects.create_user(
            username='8000063',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000063',
            nombre='Luis',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='67023554' if '67023554' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-18', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_63,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_63, id_curso=curso_2do_A)
        tutor_64 = Usuario.objects.create_user(
            username='9000064',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000064',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='72544402' if '72544402' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1972-11-14', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_64 = Usuario.objects.create_user(
            username='8000064',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000064',
            nombre='Jorge',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='61007769' if '61007769' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-10', '%Y-%m-%d')),
            correo='jorge.mamani@gmail.com',
            tutor=tutor_64,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_64, id_curso=curso_2do_A)
        tutor_65 = Usuario.objects.create_user(
            username='9000065',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000065',
            nombre='María',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-06-15', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_65 = Usuario.objects.create_user(
            username='8000065',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000065',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-07', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            tutor=tutor_65,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_65, id_curso=curso_2do_A)
        tutor_66 = Usuario.objects.create_user(
            username='9000066',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000066',
            nombre='Pedro',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='62394728' if '62394728' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-27', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            is_active=True
        )
        alumno_66 = Usuario.objects.create_user(
            username='8000066',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000066',
            nombre='Elena',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='63706810' if '63706810' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-05-28', '%Y-%m-%d')),
            correo='elena.vargas@gmail.com',
            tutor=tutor_66,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_66, id_curso=curso_2do_A)
        tutor_67 = Usuario.objects.create_user(
            username='9000067',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000067',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1995-03-29', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_67 = Usuario.objects.create_user(
            username='8000067',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000067',
            nombre='Jorge',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-05', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            tutor=tutor_67,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_67, id_curso=curso_2do_A)
        tutor_68 = Usuario.objects.create_user(
            username='9000068',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000068',
            nombre='María',
            apellido='Soto',
            direccion='Zona Centro',
            telefono='74301771' if '74301771' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1979-10-22', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            is_active=True
        )
        alumno_68 = Usuario.objects.create_user(
            username='8000068',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000068',
            nombre='Jorge',
            apellido='Pérez',
            direccion='Barrio 4 de Noviembre',
            telefono='67339972' if '67339972' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-02', '%Y-%m-%d')),
            correo='jorge.pérez@gmail.com',
            tutor=tutor_68,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_68, id_curso=curso_2do_A)
        tutor_69 = Usuario.objects.create_user(
            username='9000069',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000069',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='64534614' if '64534614' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-11-15', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            is_active=True
        )
        alumno_69 = Usuario.objects.create_user(
            username='8000069',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000069',
            nombre='Luis',
            apellido='García',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-28', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            tutor=tutor_69,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_69, id_curso=curso_2do_A)
        tutor_70 = Usuario.objects.create_user(
            username='9000070',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000070',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='77998363' if '77998363' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1996-04-08', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_70 = Usuario.objects.create_user(
            username='8000070',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000070',
            nombre='Lucía',
            apellido='Flores',
            direccion='Zona Centro',
            telefono='61164060' if '61164060' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-28', '%Y-%m-%d')),
            correo='lucía.flores@gmail.com',
            tutor=tutor_70,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_70, id_curso=curso_2do_A)
        tutor_71 = Usuario.objects.create_user(
            username='9000071',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000071',
            nombre='Carlos',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-07-05', '%Y-%m-%d')),
            correo='carlos.gómez@gmail.com',
            is_active=True
        )
        alumno_71 = Usuario.objects.create_user(
            username='8000071',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000071',
            nombre='Ana',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-12', '%Y-%m-%d')),
            correo='ana.torres@gmail.com',
            tutor=tutor_71,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_71, id_curso=curso_2do_A)
        tutor_72 = Usuario.objects.create_user(
            username='9000072',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000072',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='66958746' if '66958746' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-05', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            is_active=True
        )
        alumno_72 = Usuario.objects.create_user(
            username='8000072',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000072',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-19', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            tutor=tutor_72,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_72, id_curso=curso_2do_A)
        tutor_73 = Usuario.objects.create_user(
            username='9000073',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000073',
            nombre='Jorge',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='71446348' if '71446348' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-12-03', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            is_active=True
        )
        alumno_73 = Usuario.objects.create_user(
            username='8000073',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000073',
            nombre='Luis',
            apellido='Vargas',
            direccion='Barrio 4 de Noviembre',
            telefono='79354435' if '79354435' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-02', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            tutor=tutor_73,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_73, id_curso=curso_2do_A)
        tutor_74 = Usuario.objects.create_user(
            username='9000074',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000074',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-10-10', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_74 = Usuario.objects.create_user(
            username='8000074',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000074',
            nombre='Carlos',
            apellido='García',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-02', '%Y-%m-%d')),
            correo='carlos.garcía@gmail.com',
            tutor=tutor_74,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_74, id_curso=curso_2do_A)
        tutor_75 = Usuario.objects.create_user(
            username='9000075',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000075',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='63426945' if '63426945' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-08-20', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_75 = Usuario.objects.create_user(
            username='8000075',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000075',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='65450959' if '65450959' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-08', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            tutor=tutor_75,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_75, id_curso=curso_2do_A)
        tutor_76 = Usuario.objects.create_user(
            username='9000076',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000076',
            nombre='Elena',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='75989064' if '75989064' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-11-30', '%Y-%m-%d')),
            correo='elena.mamani@gmail.com',
            is_active=True
        )
        alumno_76 = Usuario.objects.create_user(
            username='8000076',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000076',
            nombre='Ana',
            apellido='Vargas',
            direccion='Barrio 4 de Noviembre',
            telefono='69349307' if '69349307' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-06-02', '%Y-%m-%d')),
            correo='ana.vargas@gmail.com',
            tutor=tutor_76,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_76, id_curso=curso_2do_A)
        tutor_77 = Usuario.objects.create_user(
            username='9000077',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000077',
            nombre='Carlos',
            apellido='Flores',
            direccion='Av. Cristo Redentor',
            telefono='63663050' if '63663050' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-08-01', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            is_active=True
        )
        alumno_77 = Usuario.objects.create_user(
            username='8000077',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000077',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-16', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            tutor=tutor_77,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_77, id_curso=curso_2do_A)
        tutor_78 = Usuario.objects.create_user(
            username='9000078',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000078',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-07-14', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            is_active=True
        )
        alumno_78 = Usuario.objects.create_user(
            username='8000078',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000078',
            nombre='Elena',
            apellido='Gómez',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-24', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            tutor=tutor_78,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_78, id_curso=curso_2do_A)
        tutor_79 = Usuario.objects.create_user(
            username='9000079',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000079',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-08-12', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_79 = Usuario.objects.create_user(
            username='8000079',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000079',
            nombre='Jorge',
            apellido='Vargas',
            direccion='Av. Cristo Redentor',
            telefono='61546108' if '61546108' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-23', '%Y-%m-%d')),
            correo='jorge.vargas@gmail.com',
            tutor=tutor_79,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_79, id_curso=curso_2do_A)
        tutor_80 = Usuario.objects.create_user(
            username='9000080',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000080',
            nombre='Luis',
            apellido='García',
            direccion='Zona Centro',
            telefono='63376286' if '63376286' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-07-17', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            is_active=True
        )
        alumno_80 = Usuario.objects.create_user(
            username='8000080',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000080',
            nombre='Lucía',
            apellido='Pérez',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-06-14', '%Y-%m-%d')),
            correo='lucía.pérez@gmail.com',
            tutor=tutor_80,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_80, id_curso=curso_2do_A)
        tutor_81 = Usuario.objects.create_user(
            username='9000081',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000081',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-11', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            is_active=True
        )
        alumno_81 = Usuario.objects.create_user(
            username='8000081',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000081',
            nombre='Marco',
            apellido='Mamani',
            direccion='Barrio Equipetrol',
            telefono='74173667' if '74173667' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-02', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_81,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_81, id_curso=curso_2do_B)
        tutor_82 = Usuario.objects.create_user(
            username='9000082',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000082',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='77187077' if '77187077' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_82 = Usuario.objects.create_user(
            username='8000082',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000082',
            nombre='Jorge',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='67349707' if '67349707' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-12', '%Y-%m-%d')),
            correo='jorge.garcía@gmail.com',
            tutor=tutor_82,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_82, id_curso=curso_2do_B)
        tutor_83 = Usuario.objects.create_user(
            username='9000083',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000083',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='73436319' if '73436319' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-08-11', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            is_active=True
        )
        alumno_83 = Usuario.objects.create_user(
            username='8000083',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000083',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='76856458' if '76856458' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-04-08', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            tutor=tutor_83,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_83, id_curso=curso_2do_B)
        tutor_84 = Usuario.objects.create_user(
            username='9000084',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000084',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-06', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            is_active=True
        )
        alumno_84 = Usuario.objects.create_user(
            username='8000084',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000084',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='76955255' if '76955255' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-09', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            tutor=tutor_84,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_84, id_curso=curso_2do_B)
        tutor_85 = Usuario.objects.create_user(
            username='9000085',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000085',
            nombre='Marco',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='61618380' if '61618380' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-10-02', '%Y-%m-%d')),
            correo='marco.soto@gmail.com',
            is_active=True
        )
        alumno_85 = Usuario.objects.create_user(
            username='8000085',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000085',
            nombre='Ana',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='73748731' if '73748731' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-24', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            tutor=tutor_85,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_85, id_curso=curso_2do_B)
        tutor_86 = Usuario.objects.create_user(
            username='9000086',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000086',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-01-22', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            is_active=True
        )
        alumno_86 = Usuario.objects.create_user(
            username='8000086',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000086',
            nombre='Jorge',
            apellido='García',
            direccion='Barrio Los Chacos',
            telefono='71146119' if '71146119' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-05-22', '%Y-%m-%d')),
            correo='jorge.garcía@gmail.com',
            tutor=tutor_86,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_86, id_curso=curso_2do_B)
        tutor_87 = Usuario.objects.create_user(
            username='9000087',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000087',
            nombre='Luis',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='65242022' if '65242022' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-03-10', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            is_active=True
        )
        alumno_87 = Usuario.objects.create_user(
            username='8000087',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000087',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-03', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            tutor=tutor_87,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_87, id_curso=curso_2do_B)
        tutor_88 = Usuario.objects.create_user(
            username='9000088',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000088',
            nombre='Jorge',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='61832169' if '61832169' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1987-09-29', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            is_active=True
        )
        alumno_88 = Usuario.objects.create_user(
            username='8000088',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000088',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Zona El Trompillo',
            telefono='63061065' if '63061065' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-04-22', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            tutor=tutor_88,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_88, id_curso=curso_2do_B)
        tutor_89 = Usuario.objects.create_user(
            username='9000089',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000089',
            nombre='Luis',
            apellido='Flores',
            direccion='Zona El Trompillo',
            telefono='60244304' if '60244304' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-08-26', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            is_active=True
        )
        alumno_89 = Usuario.objects.create_user(
            username='8000089',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000089',
            nombre='Elena',
            apellido='García',
            direccion='Barrio Equipetrol',
            telefono='69941058' if '69941058' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-10-27', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            tutor=tutor_89,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_89, id_curso=curso_2do_B)
        tutor_90 = Usuario.objects.create_user(
            username='9000090',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000090',
            nombre='Luis',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='74103407' if '74103407' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-05-11', '%Y-%m-%d')),
            correo='luis.mamani@gmail.com',
            is_active=True
        )
        alumno_90 = Usuario.objects.create_user(
            username='8000090',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000090',
            nombre='Marco',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='79475057' if '79475057' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-17', '%Y-%m-%d')),
            correo='marco.vargas@gmail.com',
            tutor=tutor_90,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_90, id_curso=curso_2do_B)
        tutor_91 = Usuario.objects.create_user(
            username='9000091',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000091',
            nombre='Laura',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='75904215' if '75904215' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-12-14', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            is_active=True
        )
        alumno_91 = Usuario.objects.create_user(
            username='8000091',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000091',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='66838157' if '66838157' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-22', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            tutor=tutor_91,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_91, id_curso=curso_2do_B)
        tutor_92 = Usuario.objects.create_user(
            username='9000092',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000092',
            nombre='Laura',
            apellido='Flores',
            direccion='Av. Roca y Coronado',
            telefono='63497745' if '63497745' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-09-01', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_92 = Usuario.objects.create_user(
            username='8000092',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000092',
            nombre='Ana',
            apellido='Pérez',
            direccion='Av. Banzer',
            telefono='68540811' if '68540811' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-04', '%Y-%m-%d')),
            correo='ana.pérez@gmail.com',
            tutor=tutor_92,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_92, id_curso=curso_2do_B)
        tutor_93 = Usuario.objects.create_user(
            username='9000093',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000093',
            nombre='Laura',
            apellido='García',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1973-07-18', '%Y-%m-%d')),
            correo='laura.garcía@gmail.com',
            is_active=True
        )
        alumno_93 = Usuario.objects.create_user(
            username='8000093',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000093',
            nombre='Marco',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='74912456' if '74912456' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-24', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_93,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_93, id_curso=curso_2do_B)
        tutor_94 = Usuario.objects.create_user(
            username='9000094',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000094',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-12-18', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_94 = Usuario.objects.create_user(
            username='8000094',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000094',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-24', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            tutor=tutor_94,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_94, id_curso=curso_2do_B)
        tutor_95 = Usuario.objects.create_user(
            username='9000095',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000095',
            nombre='Laura',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='66177430' if '66177430' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1969-06-18', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            is_active=True
        )
        alumno_95 = Usuario.objects.create_user(
            username='8000095',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000095',
            nombre='Ana',
            apellido='Torres',
            direccion='Barrio Urbarí',
            telefono='76724735' if '76724735' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-29', '%Y-%m-%d')),
            correo='ana.torres@gmail.com',
            tutor=tutor_95,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_95, id_curso=curso_2do_B)
        tutor_96 = Usuario.objects.create_user(
            username='9000096',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000096',
            nombre='Luis',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='66942628' if '66942628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-03', '%Y-%m-%d')),
            correo='luis.torres@gmail.com',
            is_active=True
        )
        alumno_96 = Usuario.objects.create_user(
            username='8000096',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000096',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-12-07', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            tutor=tutor_96,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_96, id_curso=curso_2do_B)
        tutor_97 = Usuario.objects.create_user(
            username='9000097',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000097',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1980-09-15', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_97 = Usuario.objects.create_user(
            username='8000097',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000097',
            nombre='Carlos',
            apellido='Flores',
            direccion='Zona Centro',
            telefono='75939062' if '75939062' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-08', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            tutor=tutor_97,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_97, id_curso=curso_2do_B)
        tutor_98 = Usuario.objects.create_user(
            username='9000098',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000098',
            nombre='Pedro',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='70061577' if '70061577' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-08-12', '%Y-%m-%d')),
            correo='pedro.pérez@gmail.com',
            is_active=True
        )
        alumno_98 = Usuario.objects.create_user(
            username='8000098',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000098',
            nombre='Elena',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='64026424' if '64026424' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-29', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            tutor=tutor_98,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_98, id_curso=curso_2do_B)
        tutor_99 = Usuario.objects.create_user(
            username='9000099',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000099',
            nombre='María',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='69278628' if '69278628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-08', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_99 = Usuario.objects.create_user(
            username='8000099',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000099',
            nombre='Lucía',
            apellido='Gómez',
            direccion='Av. Cristo Redentor',
            telefono='69945332' if '69945332' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-12', '%Y-%m-%d')),
            correo='lucía.gómez@gmail.com',
            tutor=tutor_99,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_99, id_curso=curso_2do_B)
        tutor_100 = Usuario.objects.create_user(
            username='9000100',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000100',
            nombre='Laura',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='62142118' if '62142118' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1988-05-30', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_100 = Usuario.objects.create_user(
            username='8000100',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000100',
            nombre='Jorge',
            apellido='Rojas',
            direccion='Barrio Los Chacos',
            telefono='68439806' if '68439806' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-16', '%Y-%m-%d')),
            correo='jorge.rojas@gmail.com',
            tutor=tutor_100,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_100, id_curso=curso_2do_B)
        tutor_101 = Usuario.objects.create_user(
            username='9000101',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000101',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Av. Virgen de Cotoca',
            telefono='78074961' if '78074961' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-06-23', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_101 = Usuario.objects.create_user(
            username='8000101',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000101',
            nombre='María',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='70217939' if '70217939' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-06-08', '%Y-%m-%d')),
            correo='maría.gómez@gmail.com',
            tutor=tutor_101,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_101, id_curso=curso_2do_C)
        tutor_102 = Usuario.objects.create_user(
            username='9000102',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000102',
            nombre='Luis',
            apellido='Gómez',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-07-20', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            is_active=True
        )
        alumno_102 = Usuario.objects.create_user(
            username='8000102',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000102',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-11-26', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            tutor=tutor_102,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_102, id_curso=curso_2do_C)
        tutor_103 = Usuario.objects.create_user(
            username='9000103',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000103',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='70508550' if '70508550' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-08-08', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            is_active=True
        )
        alumno_103 = Usuario.objects.create_user(
            username='8000103',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000103',
            nombre='Luis',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='78981785' if '78981785' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-05-28', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_103,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_103, id_curso=curso_2do_C)
        tutor_104 = Usuario.objects.create_user(
            username='9000104',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000104',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='68713474' if '68713474' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-11-03', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            is_active=True
        )
        alumno_104 = Usuario.objects.create_user(
            username='8000104',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000104',
            nombre='María',
            apellido='Soto',
            direccion='Barrio 4 de Noviembre',
            telefono='67124568' if '67124568' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-25', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            tutor=tutor_104,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_104, id_curso=curso_2do_C)
        tutor_105 = Usuario.objects.create_user(
            username='9000105',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000105',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-05-15', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            is_active=True
        )
        alumno_105 = Usuario.objects.create_user(
            username='8000105',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000105',
            nombre='Carlos',
            apellido='Quispe',
            direccion='Zona El Trompillo',
            telefono='64640717' if '64640717' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-26', '%Y-%m-%d')),
            correo='carlos.quispe@gmail.com',
            tutor=tutor_105,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_105, id_curso=curso_2do_C)
        tutor_106 = Usuario.objects.create_user(
            username='9000106',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000106',
            nombre='Laura',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='66635150' if '66635150' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-06-06', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            is_active=True
        )
        alumno_106 = Usuario.objects.create_user(
            username='8000106',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000106',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona Centro',
            telefono='63688230' if '63688230' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-08-23', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            tutor=tutor_106,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_106, id_curso=curso_2do_C)
        tutor_107 = Usuario.objects.create_user(
            username='9000107',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000107',
            nombre='Elena',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='79850106' if '79850106' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-08', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            is_active=True
        )
        alumno_107 = Usuario.objects.create_user(
            username='8000107',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000107',
            nombre='Jorge',
            apellido='Mamani',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-16', '%Y-%m-%d')),
            correo='jorge.mamani@gmail.com',
            tutor=tutor_107,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_107, id_curso=curso_2do_C)
        tutor_108 = Usuario.objects.create_user(
            username='9000108',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000108',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='73036060' if '73036060' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1966-12-30', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            is_active=True
        )
        alumno_108 = Usuario.objects.create_user(
            username='8000108',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000108',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-28', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            tutor=tutor_108,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_108, id_curso=curso_2do_C)
        tutor_109 = Usuario.objects.create_user(
            username='9000109',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000109',
            nombre='Marco',
            apellido='Torres',
            direccion='Barrio Urbarí',
            telefono='71097732' if '71097732' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-14', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_109 = Usuario.objects.create_user(
            username='8000109',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000109',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-26', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            tutor=tutor_109,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_109, id_curso=curso_2do_C)
        tutor_110 = Usuario.objects.create_user(
            username='9000110',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000110',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='64804300' if '64804300' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-08-06', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_110 = Usuario.objects.create_user(
            username='8000110',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000110',
            nombre='Ana',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='71192456' if '71192456' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-26', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            tutor=tutor_110,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_110, id_curso=curso_2do_C)
        tutor_111 = Usuario.objects.create_user(
            username='9000111',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000111',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            is_active=True
        )
        alumno_111 = Usuario.objects.create_user(
            username='8000111',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000111',
            nombre='Jorge',
            apellido='Torres',
            direccion='Av. Virgen de Cotoca',
            telefono='67941027' if '67941027' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-29', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            tutor=tutor_111,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_111, id_curso=curso_2do_C)
        tutor_112 = Usuario.objects.create_user(
            username='9000112',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000112',
            nombre='Marco',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='69945029' if '69945029' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-09-30', '%Y-%m-%d')),
            correo='marco.quispe@gmail.com',
            is_active=True
        )
        alumno_112 = Usuario.objects.create_user(
            username='8000112',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000112',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='63465584' if '63465584' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-01', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            tutor=tutor_112,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_112, id_curso=curso_2do_C)
        tutor_113 = Usuario.objects.create_user(
            username='9000113',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000113',
            nombre='Marco',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='72420478' if '72420478' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1993-12-22', '%Y-%m-%d')),
            correo='marco.flores@gmail.com',
            is_active=True
        )
        alumno_113 = Usuario.objects.create_user(
            username='8000113',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000113',
            nombre='Carlos',
            apellido='Flores',
            direccion='Zona Centro',
            telefono='64231295' if '64231295' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-01-11', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            tutor=tutor_113,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_113, id_curso=curso_2do_C)
        tutor_114 = Usuario.objects.create_user(
            username='9000114',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000114',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='67877721' if '67877721' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-11-21', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            is_active=True
        )
        alumno_114 = Usuario.objects.create_user(
            username='8000114',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000114',
            nombre='Pedro',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='71768911' if '71768911' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-19', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            tutor=tutor_114,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_114, id_curso=curso_2do_C)
        tutor_115 = Usuario.objects.create_user(
            username='9000115',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000115',
            nombre='Ana',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-05-02', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_115 = Usuario.objects.create_user(
            username='8000115',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000115',
            nombre='Marco',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='78315899' if '78315899' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-07-22', '%Y-%m-%d')),
            correo='marco.gómez@gmail.com',
            tutor=tutor_115,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_115, id_curso=curso_2do_C)
        tutor_116 = Usuario.objects.create_user(
            username='9000116',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000116',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-10-14', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            is_active=True
        )
        alumno_116 = Usuario.objects.create_user(
            username='8000116',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000116',
            nombre='Ana',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='61754047' if '61754047' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-10-02', '%Y-%m-%d')),
            correo='ana.torres@gmail.com',
            tutor=tutor_116,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_116, id_curso=curso_2do_C)
        tutor_117 = Usuario.objects.create_user(
            username='9000117',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000117',
            nombre='Marco',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='67388847' if '67388847' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-02-23', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_117 = Usuario.objects.create_user(
            username='8000117',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000117',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='63053125' if '63053125' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-03-17', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            tutor=tutor_117,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_117, id_curso=curso_2do_C)
        tutor_118 = Usuario.objects.create_user(
            username='9000118',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000118',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Zona El Trompillo',
            telefono='61748434' if '61748434' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-10-01', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_118 = Usuario.objects.create_user(
            username='8000118',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000118',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='63083724' if '63083724' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-02-12', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            tutor=tutor_118,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_118, id_curso=curso_2do_C)
        tutor_119 = Usuario.objects.create_user(
            username='9000119',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000119',
            nombre='Elena',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='74166864' if '74166864' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-29', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            is_active=True
        )
        alumno_119 = Usuario.objects.create_user(
            username='8000119',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000119',
            nombre='Pedro',
            apellido='Quispe',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-04', '%Y-%m-%d')),
            correo='pedro.quispe@gmail.com',
            tutor=tutor_119,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_119, id_curso=curso_2do_C)
        tutor_120 = Usuario.objects.create_user(
            username='9000120',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000120',
            nombre='Laura',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='71224148' if '71224148' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-14', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_120 = Usuario.objects.create_user(
            username='8000120',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000120',
            nombre='Carlos',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='61085490' if '61085490' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2009-09-22', '%Y-%m-%d')),
            correo='carlos.torres@gmail.com',
            tutor=tutor_120,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_120, id_curso=curso_2do_C)
        tutor_121 = Usuario.objects.create_user(
            username='9000121',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000121',
            nombre='Ana',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-04-11', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            is_active=True
        )
        alumno_121 = Usuario.objects.create_user(
            username='8000121',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000121',
            nombre='Marco',
            apellido='Pérez',
            direccion='Av. Banzer',
            telefono='66469276' if '66469276' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-04', '%Y-%m-%d')),
            correo='marco.pérez@gmail.com',
            tutor=tutor_121,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_121, id_curso=curso_3ro_A)
        tutor_122 = Usuario.objects.create_user(
            username='9000122',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000122',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='75766041' if '75766041' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-12-28', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            is_active=True
        )
        alumno_122 = Usuario.objects.create_user(
            username='8000122',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000122',
            nombre='Elena',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='64232166' if '64232166' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-12-05', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            tutor=tutor_122,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_122, id_curso=curso_3ro_A)
        tutor_123 = Usuario.objects.create_user(
            username='9000123',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000123',
            nombre='Ana',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1983-03-10', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_123 = Usuario.objects.create_user(
            username='8000123',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000123',
            nombre='Laura',
            apellido='Quispe',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-03', '%Y-%m-%d')),
            correo='laura.quispe@gmail.com',
            tutor=tutor_123,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_123, id_curso=curso_3ro_A)
        tutor_124 = Usuario.objects.create_user(
            username='9000124',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000124',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='72544402' if '72544402' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1972-11-14', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_124 = Usuario.objects.create_user(
            username='8000124',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000124',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='71064941' if '71064941' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-06-10', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            tutor=tutor_124,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_124, id_curso=curso_3ro_A)
        tutor_125 = Usuario.objects.create_user(
            username='9000125',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000125',
            nombre='María',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-06-15', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_125 = Usuario.objects.create_user(
            username='8000125',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000125',
            nombre='Carlos',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='61425556' if '61425556' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-16', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            tutor=tutor_125,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_125, id_curso=curso_3ro_A)
        tutor_126 = Usuario.objects.create_user(
            username='9000126',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000126',
            nombre='Pedro',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='62394728' if '62394728' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-27', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            is_active=True
        )
        alumno_126 = Usuario.objects.create_user(
            username='8000126',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000126',
            nombre='María',
            apellido='Soto',
            direccion='Zona El Trompillo',
            telefono='78156544' if '78156544' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-09-12', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            tutor=tutor_126,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_126, id_curso=curso_3ro_A)
        tutor_127 = Usuario.objects.create_user(
            username='9000127',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000127',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1995-03-29', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_127 = Usuario.objects.create_user(
            username='8000127',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000127',
            nombre='María',
            apellido='Mamani',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-07-23', '%Y-%m-%d')),
            correo='maría.mamani@gmail.com',
            tutor=tutor_127,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_127, id_curso=curso_3ro_A)
        tutor_128 = Usuario.objects.create_user(
            username='9000128',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000128',
            nombre='María',
            apellido='Soto',
            direccion='Zona Centro',
            telefono='74301771' if '74301771' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1979-10-22', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            is_active=True
        )
        alumno_128 = Usuario.objects.create_user(
            username='8000128',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000128',
            nombre='Marco',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='60799014' if '60799014' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-21', '%Y-%m-%d')),
            correo='marco.gómez@gmail.com',
            tutor=tutor_128,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_128, id_curso=curso_3ro_A)
        tutor_129 = Usuario.objects.create_user(
            username='9000129',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000129',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='64534614' if '64534614' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-11-15', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            is_active=True
        )
        alumno_129 = Usuario.objects.create_user(
            username='8000129',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000129',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-21', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            tutor=tutor_129,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_129, id_curso=curso_3ro_A)
        tutor_130 = Usuario.objects.create_user(
            username='9000130',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000130',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='77998363' if '77998363' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1996-04-08', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_130 = Usuario.objects.create_user(
            username='8000130',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000130',
            nombre='María',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='62051514' if '62051514' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-23', '%Y-%m-%d')),
            correo='maría.garcía@gmail.com',
            tutor=tutor_130,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_130, id_curso=curso_3ro_A)
        tutor_131 = Usuario.objects.create_user(
            username='9000131',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000131',
            nombre='Carlos',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-07-05', '%Y-%m-%d')),
            correo='carlos.gómez@gmail.com',
            is_active=True
        )
        alumno_131 = Usuario.objects.create_user(
            username='8000131',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000131',
            nombre='Lucía',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-09', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            tutor=tutor_131,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_131, id_curso=curso_3ro_A)
        tutor_132 = Usuario.objects.create_user(
            username='9000132',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000132',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='66958746' if '66958746' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-05', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            is_active=True
        )
        alumno_132 = Usuario.objects.create_user(
            username='8000132',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000132',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-14', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            tutor=tutor_132,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_132, id_curso=curso_3ro_A)
        tutor_133 = Usuario.objects.create_user(
            username='9000133',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000133',
            nombre='Jorge',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='71446348' if '71446348' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-12-03', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            is_active=True
        )
        alumno_133 = Usuario.objects.create_user(
            username='8000133',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000133',
            nombre='Ana',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-29', '%Y-%m-%d')),
            correo='ana.soto@gmail.com',
            tutor=tutor_133,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_133, id_curso=curso_3ro_A)
        tutor_134 = Usuario.objects.create_user(
            username='9000134',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000134',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-10-10', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_134 = Usuario.objects.create_user(
            username='8000134',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000134',
            nombre='Marco',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='71830684' if '71830684' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-09-18', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            tutor=tutor_134,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_134, id_curso=curso_3ro_A)
        tutor_135 = Usuario.objects.create_user(
            username='9000135',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000135',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='63426945' if '63426945' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-08-20', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_135 = Usuario.objects.create_user(
            username='8000135',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000135',
            nombre='Ana',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-07-06', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            tutor=tutor_135,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_135, id_curso=curso_3ro_A)
        tutor_136 = Usuario.objects.create_user(
            username='9000136',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000136',
            nombre='Elena',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='75989064' if '75989064' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-11-30', '%Y-%m-%d')),
            correo='elena.mamani@gmail.com',
            is_active=True
        )
        alumno_136 = Usuario.objects.create_user(
            username='8000136',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000136',
            nombre='Elena',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='62156047' if '62156047' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-07-27', '%Y-%m-%d')),
            correo='elena.vargas@gmail.com',
            tutor=tutor_136,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_136, id_curso=curso_3ro_A)
        tutor_137 = Usuario.objects.create_user(
            username='9000137',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000137',
            nombre='Carlos',
            apellido='Flores',
            direccion='Av. Cristo Redentor',
            telefono='63663050' if '63663050' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-08-01', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            is_active=True
        )
        alumno_137 = Usuario.objects.create_user(
            username='8000137',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000137',
            nombre='Lucía',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='68934493' if '68934493' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-17', '%Y-%m-%d')),
            correo='lucía.soto@gmail.com',
            tutor=tutor_137,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_137, id_curso=curso_3ro_A)
        tutor_138 = Usuario.objects.create_user(
            username='9000138',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000138',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-07-14', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            is_active=True
        )
        alumno_138 = Usuario.objects.create_user(
            username='8000138',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000138',
            nombre='Laura',
            apellido='Pérez',
            direccion='Barrio Los Chacos',
            telefono='70430280' if '70430280' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-19', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            tutor=tutor_138,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_138, id_curso=curso_3ro_A)
        tutor_139 = Usuario.objects.create_user(
            username='9000139',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000139',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-08-12', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_139 = Usuario.objects.create_user(
            username='8000139',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000139',
            nombre='María',
            apellido='García',
            direccion='Av. Cristo Redentor',
            telefono='60804904' if '60804904' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-11-24', '%Y-%m-%d')),
            correo='maría.garcía@gmail.com',
            tutor=tutor_139,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_139, id_curso=curso_3ro_A)
        tutor_140 = Usuario.objects.create_user(
            username='9000140',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000140',
            nombre='Luis',
            apellido='García',
            direccion='Zona Centro',
            telefono='63376286' if '63376286' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-07-17', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            is_active=True
        )
        alumno_140 = Usuario.objects.create_user(
            username='8000140',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000140',
            nombre='Pedro',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='65576756' if '65576756' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-08', '%Y-%m-%d')),
            correo='pedro.quispe@gmail.com',
            tutor=tutor_140,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_140, id_curso=curso_3ro_A)
        tutor_141 = Usuario.objects.create_user(
            username='9000141',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000141',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-11', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            is_active=True
        )
        alumno_141 = Usuario.objects.create_user(
            username='8000141',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000141',
            nombre='Jorge',
            apellido='García',
            direccion='Av. Cristo Redentor',
            telefono='68106430' if '68106430' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-09-26', '%Y-%m-%d')),
            correo='jorge.garcía@gmail.com',
            tutor=tutor_141,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_141, id_curso=curso_3ro_B)
        tutor_142 = Usuario.objects.create_user(
            username='9000142',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000142',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='77187077' if '77187077' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_142 = Usuario.objects.create_user(
            username='8000142',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000142',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-26', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            tutor=tutor_142,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_142, id_curso=curso_3ro_B)
        tutor_143 = Usuario.objects.create_user(
            username='9000143',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000143',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='73436319' if '73436319' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-08-11', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            is_active=True
        )
        alumno_143 = Usuario.objects.create_user(
            username='8000143',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000143',
            nombre='Elena',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='63205364' if '63205364' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-15', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            tutor=tutor_143,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_143, id_curso=curso_3ro_B)
        tutor_144 = Usuario.objects.create_user(
            username='9000144',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000144',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-06', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            is_active=True
        )
        alumno_144 = Usuario.objects.create_user(
            username='8000144',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000144',
            nombre='Jorge',
            apellido='Pérez',
            direccion='Av. Virgen de Cotoca',
            telefono='61853716' if '61853716' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-11', '%Y-%m-%d')),
            correo='jorge.pérez@gmail.com',
            tutor=tutor_144,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_144, id_curso=curso_3ro_B)
        tutor_145 = Usuario.objects.create_user(
            username='9000145',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000145',
            nombre='Marco',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='61618380' if '61618380' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-10-02', '%Y-%m-%d')),
            correo='marco.soto@gmail.com',
            is_active=True
        )
        alumno_145 = Usuario.objects.create_user(
            username='8000145',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000145',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-08', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            tutor=tutor_145,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_145, id_curso=curso_3ro_B)
        tutor_146 = Usuario.objects.create_user(
            username='9000146',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000146',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-01-22', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            is_active=True
        )
        alumno_146 = Usuario.objects.create_user(
            username='8000146',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000146',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-26', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            tutor=tutor_146,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_146, id_curso=curso_3ro_B)
        tutor_147 = Usuario.objects.create_user(
            username='9000147',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000147',
            nombre='Luis',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='65242022' if '65242022' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-03-10', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            is_active=True
        )
        alumno_147 = Usuario.objects.create_user(
            username='8000147',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000147',
            nombre='Laura',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='77655440' if '77655440' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-08', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            tutor=tutor_147,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_147, id_curso=curso_3ro_B)
        tutor_148 = Usuario.objects.create_user(
            username='9000148',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000148',
            nombre='Jorge',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='61832169' if '61832169' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1987-09-29', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            is_active=True
        )
        alumno_148 = Usuario.objects.create_user(
            username='8000148',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000148',
            nombre='Elena',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='64792869' if '64792869' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-11-23', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            tutor=tutor_148,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_148, id_curso=curso_3ro_B)
        tutor_149 = Usuario.objects.create_user(
            username='9000149',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000149',
            nombre='Luis',
            apellido='Flores',
            direccion='Zona El Trompillo',
            telefono='60244304' if '60244304' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-08-26', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            is_active=True
        )
        alumno_149 = Usuario.objects.create_user(
            username='8000149',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000149',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-27', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            tutor=tutor_149,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_149, id_curso=curso_3ro_B)
        tutor_150 = Usuario.objects.create_user(
            username='9000150',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000150',
            nombre='Luis',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='74103407' if '74103407' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-05-11', '%Y-%m-%d')),
            correo='luis.mamani@gmail.com',
            is_active=True
        )
        alumno_150 = Usuario.objects.create_user(
            username='8000150',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000150',
            nombre='Laura',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='60787008' if '60787008' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-02', '%Y-%m-%d')),
            correo='laura.vargas@gmail.com',
            tutor=tutor_150,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_150, id_curso=curso_3ro_B)
        tutor_151 = Usuario.objects.create_user(
            username='9000151',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000151',
            nombre='Laura',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='75904215' if '75904215' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-12-14', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            is_active=True
        )
        alumno_151 = Usuario.objects.create_user(
            username='8000151',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000151',
            nombre='María',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='62552259' if '62552259' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-08', '%Y-%m-%d')),
            correo='maría.gómez@gmail.com',
            tutor=tutor_151,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_151, id_curso=curso_3ro_B)
        tutor_152 = Usuario.objects.create_user(
            username='9000152',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000152',
            nombre='Laura',
            apellido='Flores',
            direccion='Av. Roca y Coronado',
            telefono='63497745' if '63497745' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-09-01', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_152 = Usuario.objects.create_user(
            username='8000152',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000152',
            nombre='Jorge',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='68499311' if '68499311' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-09', '%Y-%m-%d')),
            correo='jorge.vargas@gmail.com',
            tutor=tutor_152,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_152, id_curso=curso_3ro_B)
        tutor_153 = Usuario.objects.create_user(
            username='9000153',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000153',
            nombre='Laura',
            apellido='García',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1973-07-18', '%Y-%m-%d')),
            correo='laura.garcía@gmail.com',
            is_active=True
        )
        alumno_153 = Usuario.objects.create_user(
            username='8000153',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000153',
            nombre='Elena',
            apellido='Pérez',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-09-22', '%Y-%m-%d')),
            correo='elena.pérez@gmail.com',
            tutor=tutor_153,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_153, id_curso=curso_3ro_B)
        tutor_154 = Usuario.objects.create_user(
            username='9000154',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000154',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-12-18', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_154 = Usuario.objects.create_user(
            username='8000154',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000154',
            nombre='Elena',
            apellido='Gómez',
            direccion='Barrio 4 de Noviembre',
            telefono='72876659' if '72876659' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-24', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            tutor=tutor_154,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_154, id_curso=curso_3ro_B)
        tutor_155 = Usuario.objects.create_user(
            username='9000155',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000155',
            nombre='Laura',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='66177430' if '66177430' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1969-06-18', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            is_active=True
        )
        alumno_155 = Usuario.objects.create_user(
            username='8000155',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000155',
            nombre='Laura',
            apellido='Flores',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-03', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            tutor=tutor_155,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_155, id_curso=curso_3ro_B)
        tutor_156 = Usuario.objects.create_user(
            username='9000156',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000156',
            nombre='Luis',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='66942628' if '66942628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-03', '%Y-%m-%d')),
            correo='luis.torres@gmail.com',
            is_active=True
        )
        alumno_156 = Usuario.objects.create_user(
            username='8000156',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000156',
            nombre='Pedro',
            apellido='Gómez',
            direccion='Av. Roca y Coronado',
            telefono='74984855' if '74984855' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-11-19', '%Y-%m-%d')),
            correo='pedro.gómez@gmail.com',
            tutor=tutor_156,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_156, id_curso=curso_3ro_B)
        tutor_157 = Usuario.objects.create_user(
            username='9000157',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000157',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1980-09-15', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_157 = Usuario.objects.create_user(
            username='8000157',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000157',
            nombre='María',
            apellido='Quispe',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-09', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            tutor=tutor_157,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_157, id_curso=curso_3ro_B)
        tutor_158 = Usuario.objects.create_user(
            username='9000158',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000158',
            nombre='Pedro',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='70061577' if '70061577' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-08-12', '%Y-%m-%d')),
            correo='pedro.pérez@gmail.com',
            is_active=True
        )
        alumno_158 = Usuario.objects.create_user(
            username='8000158',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000158',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Roca y Coronado',
            telefono='65443846' if '65443846' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-29', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            tutor=tutor_158,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_158, id_curso=curso_3ro_B)
        tutor_159 = Usuario.objects.create_user(
            username='9000159',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000159',
            nombre='María',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='69278628' if '69278628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-08', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_159 = Usuario.objects.create_user(
            username='8000159',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000159',
            nombre='Laura',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-19', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            tutor=tutor_159,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_159, id_curso=curso_3ro_B)
        tutor_160 = Usuario.objects.create_user(
            username='9000160',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000160',
            nombre='Laura',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='62142118' if '62142118' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1988-05-30', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_160 = Usuario.objects.create_user(
            username='8000160',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000160',
            nombre='Luis',
            apellido='Soto',
            direccion='Av. Banzer',
            telefono='60037735' if '60037735' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-29', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_160,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_160, id_curso=curso_3ro_B)
        tutor_161 = Usuario.objects.create_user(
            username='9000161',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000161',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Av. Virgen de Cotoca',
            telefono='78074961' if '78074961' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-06-23', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_161 = Usuario.objects.create_user(
            username='8000161',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000161',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Av. Virgen de Cotoca',
            telefono='76111565' if '76111565' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-07-08', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            tutor=tutor_161,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_161, id_curso=curso_3ro_C)
        tutor_162 = Usuario.objects.create_user(
            username='9000162',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000162',
            nombre='Luis',
            apellido='Gómez',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-07-20', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            is_active=True
        )
        alumno_162 = Usuario.objects.create_user(
            username='8000162',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000162',
            nombre='Jorge',
            apellido='Mamani',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-03', '%Y-%m-%d')),
            correo='jorge.mamani@gmail.com',
            tutor=tutor_162,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_162, id_curso=curso_3ro_C)
        tutor_163 = Usuario.objects.create_user(
            username='9000163',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000163',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='70508550' if '70508550' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-08-08', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            is_active=True
        )
        alumno_163 = Usuario.objects.create_user(
            username='8000163',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000163',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='60369529' if '60369529' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-29', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            tutor=tutor_163,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_163, id_curso=curso_3ro_C)
        tutor_164 = Usuario.objects.create_user(
            username='9000164',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000164',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='68713474' if '68713474' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-11-03', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            is_active=True
        )
        alumno_164 = Usuario.objects.create_user(
            username='8000164',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000164',
            nombre='Carlos',
            apellido='García',
            direccion='Av. Banzer',
            telefono='70139536' if '70139536' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-06-02', '%Y-%m-%d')),
            correo='carlos.garcía@gmail.com',
            tutor=tutor_164,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_164, id_curso=curso_3ro_C)
        tutor_165 = Usuario.objects.create_user(
            username='9000165',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000165',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-05-15', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            is_active=True
        )
        alumno_165 = Usuario.objects.create_user(
            username='8000165',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000165',
            nombre='Luis',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='71655644' if '71655644' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-09-05', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            tutor=tutor_165,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_165, id_curso=curso_3ro_C)
        tutor_166 = Usuario.objects.create_user(
            username='9000166',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000166',
            nombre='Laura',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='66635150' if '66635150' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-06-06', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            is_active=True
        )
        alumno_166 = Usuario.objects.create_user(
            username='8000166',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000166',
            nombre='María',
            apellido='Vargas',
            direccion='Barrio 4 de Noviembre',
            telefono='76730947' if '76730947' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-07', '%Y-%m-%d')),
            correo='maría.vargas@gmail.com',
            tutor=tutor_166,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_166, id_curso=curso_3ro_C)
        tutor_167 = Usuario.objects.create_user(
            username='9000167',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000167',
            nombre='Elena',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='79850106' if '79850106' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-08', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            is_active=True
        )
        alumno_167 = Usuario.objects.create_user(
            username='8000167',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000167',
            nombre='Jorge',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='76964251' if '76964251' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-17', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            tutor=tutor_167,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_167, id_curso=curso_3ro_C)
        tutor_168 = Usuario.objects.create_user(
            username='9000168',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000168',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='73036060' if '73036060' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1966-12-30', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            is_active=True
        )
        alumno_168 = Usuario.objects.create_user(
            username='8000168',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000168',
            nombre='María',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-07', '%Y-%m-%d')),
            correo='maría.gómez@gmail.com',
            tutor=tutor_168,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_168, id_curso=curso_3ro_C)
        tutor_169 = Usuario.objects.create_user(
            username='9000169',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000169',
            nombre='Marco',
            apellido='Torres',
            direccion='Barrio Urbarí',
            telefono='71097732' if '71097732' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-14', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_169 = Usuario.objects.create_user(
            username='8000169',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000169',
            nombre='Jorge',
            apellido='Pérez',
            direccion='Av. Virgen de Cotoca',
            telefono='61963915' if '61963915' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-09', '%Y-%m-%d')),
            correo='jorge.pérez@gmail.com',
            tutor=tutor_169,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_169, id_curso=curso_3ro_C)
        tutor_170 = Usuario.objects.create_user(
            username='9000170',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000170',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='64804300' if '64804300' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-08-06', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_170 = Usuario.objects.create_user(
            username='8000170',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000170',
            nombre='Pedro',
            apellido='Gómez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-05-20', '%Y-%m-%d')),
            correo='pedro.gómez@gmail.com',
            tutor=tutor_170,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_170, id_curso=curso_3ro_C)
        tutor_171 = Usuario.objects.create_user(
            username='9000171',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000171',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            is_active=True
        )
        alumno_171 = Usuario.objects.create_user(
            username='8000171',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000171',
            nombre='María',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='66912751' if '66912751' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-07', '%Y-%m-%d')),
            correo='maría.rojas@gmail.com',
            tutor=tutor_171,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_171, id_curso=curso_3ro_C)
        tutor_172 = Usuario.objects.create_user(
            username='9000172',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000172',
            nombre='Marco',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='69945029' if '69945029' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-09-30', '%Y-%m-%d')),
            correo='marco.quispe@gmail.com',
            is_active=True
        )
        alumno_172 = Usuario.objects.create_user(
            username='8000172',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000172',
            nombre='Lucía',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-01-21', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            tutor=tutor_172,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_172, id_curso=curso_3ro_C)
        tutor_173 = Usuario.objects.create_user(
            username='9000173',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000173',
            nombre='Marco',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='72420478' if '72420478' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1993-12-22', '%Y-%m-%d')),
            correo='marco.flores@gmail.com',
            is_active=True
        )
        alumno_173 = Usuario.objects.create_user(
            username='8000173',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000173',
            nombre='Pedro',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='69732186' if '69732186' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-09', '%Y-%m-%d')),
            correo='pedro.rojas@gmail.com',
            tutor=tutor_173,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_173, id_curso=curso_3ro_C)
        tutor_174 = Usuario.objects.create_user(
            username='9000174',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000174',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='67877721' if '67877721' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-11-21', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            is_active=True
        )
        alumno_174 = Usuario.objects.create_user(
            username='8000174',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000174',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Virgen de Cotoca',
            telefono='63526905' if '63526905' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-06', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_174,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_174, id_curso=curso_3ro_C)
        tutor_175 = Usuario.objects.create_user(
            username='9000175',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000175',
            nombre='Ana',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-05-02', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_175 = Usuario.objects.create_user(
            username='8000175',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000175',
            nombre='Marco',
            apellido='Pérez',
            direccion='Barrio Equipetrol',
            telefono='67476465' if '67476465' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-03-21', '%Y-%m-%d')),
            correo='marco.pérez@gmail.com',
            tutor=tutor_175,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_175, id_curso=curso_3ro_C)
        tutor_176 = Usuario.objects.create_user(
            username='9000176',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000176',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-10-14', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            is_active=True
        )
        alumno_176 = Usuario.objects.create_user(
            username='8000176',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000176',
            nombre='Ana',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='76071191' if '76071191' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-10-06', '%Y-%m-%d')),
            correo='ana.vargas@gmail.com',
            tutor=tutor_176,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_176, id_curso=curso_3ro_C)
        tutor_177 = Usuario.objects.create_user(
            username='9000177',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000177',
            nombre='Marco',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='67388847' if '67388847' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-02-23', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_177 = Usuario.objects.create_user(
            username='8000177',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000177',
            nombre='Luis',
            apellido='Gómez',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-13', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            tutor=tutor_177,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_177, id_curso=curso_3ro_C)
        tutor_178 = Usuario.objects.create_user(
            username='9000178',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000178',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Zona El Trompillo',
            telefono='61748434' if '61748434' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-10-01', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_178 = Usuario.objects.create_user(
            username='8000178',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000178',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-08-08', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            tutor=tutor_178,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_178, id_curso=curso_3ro_C)
        tutor_179 = Usuario.objects.create_user(
            username='9000179',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000179',
            nombre='Elena',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='74166864' if '74166864' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-29', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            is_active=True
        )
        alumno_179 = Usuario.objects.create_user(
            username='8000179',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000179',
            nombre='Lucía',
            apellido='Flores',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-02-24', '%Y-%m-%d')),
            correo='lucía.flores@gmail.com',
            tutor=tutor_179,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_179, id_curso=curso_3ro_C)
        tutor_180 = Usuario.objects.create_user(
            username='9000180',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000180',
            nombre='Laura',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='71224148' if '71224148' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-14', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_180 = Usuario.objects.create_user(
            username='8000180',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000180',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2008-04-25', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            tutor=tutor_180,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_180, id_curso=curso_3ro_C)
        tutor_181 = Usuario.objects.create_user(
            username='9000181',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000181',
            nombre='Ana',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-04-11', '%Y-%m-%d')),
            correo='ana.rojas@gmail.com',
            is_active=True
        )
        alumno_181 = Usuario.objects.create_user(
            username='8000181',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000181',
            nombre='Ana',
            apellido='Flores',
            direccion='Barrio Los Chacos',
            telefono='69987888' if '69987888' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-03-30', '%Y-%m-%d')),
            correo='ana.flores@gmail.com',
            tutor=tutor_181,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_181, id_curso=curso_4to_A)
        tutor_182 = Usuario.objects.create_user(
            username='9000182',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000182',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='75766041' if '75766041' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-12-28', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            is_active=True
        )
        alumno_182 = Usuario.objects.create_user(
            username='8000182',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000182',
            nombre='Carlos',
            apellido='García',
            direccion='Av. Cristo Redentor',
            telefono='64186578' if '64186578' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-12-05', '%Y-%m-%d')),
            correo='carlos.garcía@gmail.com',
            tutor=tutor_182,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_182, id_curso=curso_4to_A)
        tutor_183 = Usuario.objects.create_user(
            username='9000183',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000183',
            nombre='Ana',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1983-03-10', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_183 = Usuario.objects.create_user(
            username='8000183',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000183',
            nombre='Luis',
            apellido='Soto',
            direccion='Barrio Urbarí',
            telefono='66654897' if '66654897' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-23', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_183,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_183, id_curso=curso_4to_A)
        tutor_184 = Usuario.objects.create_user(
            username='9000184',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000184',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='72544402' if '72544402' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1972-11-14', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_184 = Usuario.objects.create_user(
            username='8000184',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000184',
            nombre='Marco',
            apellido='Mamani',
            direccion='Zona Centro',
            telefono='68438392' if '68438392' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-19', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_184,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_184, id_curso=curso_4to_A)
        tutor_185 = Usuario.objects.create_user(
            username='9000185',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000185',
            nombre='María',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-06-15', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_185 = Usuario.objects.create_user(
            username='8000185',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000185',
            nombre='Carlos',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='74910879' if '74910879' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-14', '%Y-%m-%d')),
            correo='carlos.pérez@gmail.com',
            tutor=tutor_185,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_185, id_curso=curso_4to_A)
        tutor_186 = Usuario.objects.create_user(
            username='9000186',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000186',
            nombre='Pedro',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='62394728' if '62394728' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-27', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            is_active=True
        )
        alumno_186 = Usuario.objects.create_user(
            username='8000186',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000186',
            nombre='Lucía',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-07-16', '%Y-%m-%d')),
            correo='lucía.garcía@gmail.com',
            tutor=tutor_186,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_186, id_curso=curso_4to_A)
        tutor_187 = Usuario.objects.create_user(
            username='9000187',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000187',
            nombre='Marco',
            apellido='Torres',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1995-03-29', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_187 = Usuario.objects.create_user(
            username='8000187',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000187',
            nombre='Carlos',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-08-23', '%Y-%m-%d')),
            correo='carlos.mamani@gmail.com',
            tutor=tutor_187,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_187, id_curso=curso_4to_A)
        tutor_188 = Usuario.objects.create_user(
            username='9000188',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000188',
            nombre='María',
            apellido='Soto',
            direccion='Zona Centro',
            telefono='74301771' if '74301771' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1979-10-22', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            is_active=True
        )
        alumno_188 = Usuario.objects.create_user(
            username='8000188',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000188',
            nombre='María',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='61067966' if '61067966' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-01', '%Y-%m-%d')),
            correo='maría.pérez@gmail.com',
            tutor=tutor_188,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_188, id_curso=curso_4to_A)
        tutor_189 = Usuario.objects.create_user(
            username='9000189',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000189',
            nombre='Lucía',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='64534614' if '64534614' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-11-15', '%Y-%m-%d')),
            correo='lucía.mamani@gmail.com',
            is_active=True
        )
        alumno_189 = Usuario.objects.create_user(
            username='8000189',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000189',
            nombre='Jorge',
            apellido='Flores',
            direccion='Barrio Los Chacos',
            telefono='77934199' if '77934199' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-05-04', '%Y-%m-%d')),
            correo='jorge.flores@gmail.com',
            tutor=tutor_189,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_189, id_curso=curso_4to_A)
        tutor_190 = Usuario.objects.create_user(
            username='9000190',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000190',
            nombre='Lucía',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='77998363' if '77998363' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1996-04-08', '%Y-%m-%d')),
            correo='lucía.vargas@gmail.com',
            is_active=True
        )
        alumno_190 = Usuario.objects.create_user(
            username='8000190',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000190',
            nombre='Pedro',
            apellido='García',
            direccion='Av. Banzer',
            telefono='65133321' if '65133321' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-10-02', '%Y-%m-%d')),
            correo='pedro.garcía@gmail.com',
            tutor=tutor_190,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_190, id_curso=curso_4to_A)
        tutor_191 = Usuario.objects.create_user(
            username='9000191',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000191',
            nombre='Carlos',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-07-05', '%Y-%m-%d')),
            correo='carlos.gómez@gmail.com',
            is_active=True
        )
        alumno_191 = Usuario.objects.create_user(
            username='8000191',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000191',
            nombre='Jorge',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2006-12-15', '%Y-%m-%d')),
            correo='jorge.rojas@gmail.com',
            tutor=tutor_191,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_191, id_curso=curso_4to_A)
        tutor_192 = Usuario.objects.create_user(
            username='9000192',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000192',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='66958746' if '66958746' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-05', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            is_active=True
        )
        alumno_192 = Usuario.objects.create_user(
            username='8000192',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000192',
            nombre='Laura',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-07-26', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            tutor=tutor_192,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_192, id_curso=curso_4to_A)
        tutor_193 = Usuario.objects.create_user(
            username='9000193',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000193',
            nombre='Jorge',
            apellido='Soto',
            direccion='Av. Cristo Redentor',
            telefono='71446348' if '71446348' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-12-03', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            is_active=True
        )
        alumno_193 = Usuario.objects.create_user(
            username='8000193',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000193',
            nombre='Elena',
            apellido='Rojas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-30', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            tutor=tutor_193,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_193, id_curso=curso_4to_A)
        tutor_194 = Usuario.objects.create_user(
            username='9000194',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000194',
            nombre='Laura',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-10-10', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_194 = Usuario.objects.create_user(
            username='8000194',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000194',
            nombre='María',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='75698108' if '75698108' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-08-01', '%Y-%m-%d')),
            correo='maría.rojas@gmail.com',
            tutor=tutor_194,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_194, id_curso=curso_4to_A)
        tutor_195 = Usuario.objects.create_user(
            username='9000195',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000195',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='63426945' if '63426945' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-08-20', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_195 = Usuario.objects.create_user(
            username='8000195',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000195',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-11-03', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            tutor=tutor_195,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_195, id_curso=curso_4to_A)
        tutor_196 = Usuario.objects.create_user(
            username='9000196',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000196',
            nombre='Elena',
            apellido='Mamani',
            direccion='Barrio Los Chacos',
            telefono='75989064' if '75989064' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-11-30', '%Y-%m-%d')),
            correo='elena.mamani@gmail.com',
            is_active=True
        )
        alumno_196 = Usuario.objects.create_user(
            username='8000196',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000196',
            nombre='Jorge',
            apellido='Soto',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-13', '%Y-%m-%d')),
            correo='jorge.soto@gmail.com',
            tutor=tutor_196,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_196, id_curso=curso_4to_A)
        tutor_197 = Usuario.objects.create_user(
            username='9000197',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000197',
            nombre='Carlos',
            apellido='Flores',
            direccion='Av. Cristo Redentor',
            telefono='63663050' if '63663050' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-08-01', '%Y-%m-%d')),
            correo='carlos.flores@gmail.com',
            is_active=True
        )
        alumno_197 = Usuario.objects.create_user(
            username='8000197',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000197',
            nombre='Marco',
            apellido='Flores',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-23', '%Y-%m-%d')),
            correo='marco.flores@gmail.com',
            tutor=tutor_197,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_197, id_curso=curso_4to_A)
        tutor_198 = Usuario.objects.create_user(
            username='9000198',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000198',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-07-14', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            is_active=True
        )
        alumno_198 = Usuario.objects.create_user(
            username='8000198',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000198',
            nombre='Carlos',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='72962202' if '72962202' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-25', '%Y-%m-%d')),
            correo='carlos.quispe@gmail.com',
            tutor=tutor_198,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_198, id_curso=curso_4to_A)
        tutor_199 = Usuario.objects.create_user(
            username='9000199',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000199',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-08-12', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_199 = Usuario.objects.create_user(
            username='8000199',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000199',
            nombre='Marco',
            apellido='García',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-07-15', '%Y-%m-%d')),
            correo='marco.garcía@gmail.com',
            tutor=tutor_199,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_199, id_curso=curso_4to_A)
        tutor_200 = Usuario.objects.create_user(
            username='9000200',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000200',
            nombre='Luis',
            apellido='García',
            direccion='Zona Centro',
            telefono='63376286' if '63376286' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-07-17', '%Y-%m-%d')),
            correo='luis.garcía@gmail.com',
            is_active=True
        )
        alumno_200 = Usuario.objects.create_user(
            username='8000200',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000200',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-05-23', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            tutor=tutor_200,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_200, id_curso=curso_4to_A)
        tutor_201 = Usuario.objects.create_user(
            username='9000201',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000201',
            nombre='Elena',
            apellido='Gómez',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-11', '%Y-%m-%d')),
            correo='elena.gómez@gmail.com',
            is_active=True
        )
        alumno_201 = Usuario.objects.create_user(
            username='8000201',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000201',
            nombre='Luis',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='74998021' if '74998021' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-07-08', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            tutor=tutor_201,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_201, id_curso=curso_4to_B)
        tutor_202 = Usuario.objects.create_user(
            username='9000202',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000202',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='77187077' if '77187077' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_202 = Usuario.objects.create_user(
            username='8000202',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000202',
            nombre='Laura',
            apellido='Torres',
            direccion='Av. Virgen de Cotoca',
            telefono='61402965' if '61402965' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-12-02', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            tutor=tutor_202,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_202, id_curso=curso_4to_B)
        tutor_203 = Usuario.objects.create_user(
            username='9000203',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000203',
            nombre='Luis',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='73436319' if '73436319' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1970-08-11', '%Y-%m-%d')),
            correo='luis.quispe@gmail.com',
            is_active=True
        )
        alumno_203 = Usuario.objects.create_user(
            username='8000203',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000203',
            nombre='Luis',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='62636107' if '62636107' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-21', '%Y-%m-%d')),
            correo='luis.torres@gmail.com',
            tutor=tutor_203,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_203, id_curso=curso_4to_B)
        tutor_204 = Usuario.objects.create_user(
            username='9000204',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000204',
            nombre='Ana',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-06', '%Y-%m-%d')),
            correo='ana.gómez@gmail.com',
            is_active=True
        )
        alumno_204 = Usuario.objects.create_user(
            username='8000204',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000204',
            nombre='Laura',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-11-25', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            tutor=tutor_204,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_204, id_curso=curso_4to_B)
        tutor_205 = Usuario.objects.create_user(
            username='9000205',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000205',
            nombre='Marco',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='61618380' if '61618380' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-10-02', '%Y-%m-%d')),
            correo='marco.soto@gmail.com',
            is_active=True
        )
        alumno_205 = Usuario.objects.create_user(
            username='8000205',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000205',
            nombre='Jorge',
            apellido='Vargas',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-10-03', '%Y-%m-%d')),
            correo='jorge.vargas@gmail.com',
            tutor=tutor_205,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_205, id_curso=curso_4to_B)
        tutor_206 = Usuario.objects.create_user(
            username='9000206',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000206',
            nombre='Carlos',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-01-22', '%Y-%m-%d')),
            correo='carlos.vargas@gmail.com',
            is_active=True
        )
        alumno_206 = Usuario.objects.create_user(
            username='8000206',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000206',
            nombre='Pedro',
            apellido='Flores',
            direccion='Barrio Equipetrol',
            telefono='76483959' if '76483959' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-11-03', '%Y-%m-%d')),
            correo='pedro.flores@gmail.com',
            tutor=tutor_206,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_206, id_curso=curso_4to_B)
        tutor_207 = Usuario.objects.create_user(
            username='9000207',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000207',
            nombre='Luis',
            apellido='Vargas',
            direccion='Zona El Trompillo',
            telefono='65242022' if '65242022' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-03-10', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            is_active=True
        )
        alumno_207 = Usuario.objects.create_user(
            username='8000207',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000207',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-09', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            tutor=tutor_207,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_207, id_curso=curso_4to_B)
        tutor_208 = Usuario.objects.create_user(
            username='9000208',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000208',
            nombre='Jorge',
            apellido='Torres',
            direccion='Zona Centro',
            telefono='61832169' if '61832169' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1987-09-29', '%Y-%m-%d')),
            correo='jorge.torres@gmail.com',
            is_active=True
        )
        alumno_208 = Usuario.objects.create_user(
            username='8000208',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000208',
            nombre='Elena',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='70533066' if '70533066' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2006-12-26', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            tutor=tutor_208,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_208, id_curso=curso_4to_B)
        tutor_209 = Usuario.objects.create_user(
            username='9000209',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000209',
            nombre='Luis',
            apellido='Flores',
            direccion='Zona El Trompillo',
            telefono='60244304' if '60244304' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-08-26', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            is_active=True
        )
        alumno_209 = Usuario.objects.create_user(
            username='8000209',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000209',
            nombre='María',
            apellido='Soto',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-25', '%Y-%m-%d')),
            correo='maría.soto@gmail.com',
            tutor=tutor_209,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_209, id_curso=curso_4to_B)
        tutor_210 = Usuario.objects.create_user(
            username='9000210',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000210',
            nombre='Luis',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='74103407' if '74103407' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-05-11', '%Y-%m-%d')),
            correo='luis.mamani@gmail.com',
            is_active=True
        )
        alumno_210 = Usuario.objects.create_user(
            username='8000210',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000210',
            nombre='Laura',
            apellido='Rojas',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-15', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            tutor=tutor_210,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_210, id_curso=curso_4to_B)
        tutor_211 = Usuario.objects.create_user(
            username='9000211',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000211',
            nombre='Laura',
            apellido='Soto',
            direccion='Barrio Equipetrol',
            telefono='75904215' if '75904215' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-12-14', '%Y-%m-%d')),
            correo='laura.soto@gmail.com',
            is_active=True
        )
        alumno_211 = Usuario.objects.create_user(
            username='8000211',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000211',
            nombre='Pedro',
            apellido='Torres',
            direccion='Barrio 4 de Noviembre',
            telefono='76048286' if '76048286' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-14', '%Y-%m-%d')),
            correo='pedro.torres@gmail.com',
            tutor=tutor_211,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_211, id_curso=curso_4to_B)
        tutor_212 = Usuario.objects.create_user(
            username='9000212',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000212',
            nombre='Laura',
            apellido='Flores',
            direccion='Av. Roca y Coronado',
            telefono='63497745' if '63497745' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-09-01', '%Y-%m-%d')),
            correo='laura.flores@gmail.com',
            is_active=True
        )
        alumno_212 = Usuario.objects.create_user(
            username='8000212',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000212',
            nombre='Marco',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='61784250' if '61784250' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-07-28', '%Y-%m-%d')),
            correo='marco.quispe@gmail.com',
            tutor=tutor_212,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_212, id_curso=curso_4to_B)
        tutor_213 = Usuario.objects.create_user(
            username='9000213',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000213',
            nombre='Laura',
            apellido='García',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1973-07-18', '%Y-%m-%d')),
            correo='laura.garcía@gmail.com',
            is_active=True
        )
        alumno_213 = Usuario.objects.create_user(
            username='8000213',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000213',
            nombre='Marco',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='74958977' if '74958977' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-08-15', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_213,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_213, id_curso=curso_4to_B)
        tutor_214 = Usuario.objects.create_user(
            username='9000214',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000214',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-12-18', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_214 = Usuario.objects.create_user(
            username='8000214',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000214',
            nombre='Luis',
            apellido='Rojas',
            direccion='Av. Banzer',
            telefono='69363028' if '69363028' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-11', '%Y-%m-%d')),
            correo='luis.rojas@gmail.com',
            tutor=tutor_214,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_214, id_curso=curso_4to_B)
        tutor_215 = Usuario.objects.create_user(
            username='9000215',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000215',
            nombre='Laura',
            apellido='Mamani',
            direccion='Barrio Urbarí',
            telefono='66177430' if '66177430' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1969-06-18', '%Y-%m-%d')),
            correo='laura.mamani@gmail.com',
            is_active=True
        )
        alumno_215 = Usuario.objects.create_user(
            username='8000215',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000215',
            nombre='Luis',
            apellido='Soto',
            direccion='Zona Centro',
            telefono='75083161' if '75083161' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-11-17', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_215,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_215, id_curso=curso_4to_B)
        tutor_216 = Usuario.objects.create_user(
            username='9000216',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000216',
            nombre='Luis',
            apellido='Torres',
            direccion='Av. Roca y Coronado',
            telefono='66942628' if '66942628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1997-01-03', '%Y-%m-%d')),
            correo='luis.torres@gmail.com',
            is_active=True
        )
        alumno_216 = Usuario.objects.create_user(
            username='8000216',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000216',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-18', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            tutor=tutor_216,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_216, id_curso=curso_4to_B)
        tutor_217 = Usuario.objects.create_user(
            username='9000217',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000217',
            nombre='Pedro',
            apellido='Vargas',
            direccion='Zona Centro',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1980-09-15', '%Y-%m-%d')),
            correo='pedro.vargas@gmail.com',
            is_active=True
        )
        alumno_217 = Usuario.objects.create_user(
            username='8000217',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000217',
            nombre='Carlos',
            apellido='Pérez',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-03-21', '%Y-%m-%d')),
            correo='carlos.pérez@gmail.com',
            tutor=tutor_217,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_217, id_curso=curso_4to_B)
        tutor_218 = Usuario.objects.create_user(
            username='9000218',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000218',
            nombre='Pedro',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='70061577' if '70061577' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-08-12', '%Y-%m-%d')),
            correo='pedro.pérez@gmail.com',
            is_active=True
        )
        alumno_218 = Usuario.objects.create_user(
            username='8000218',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000218',
            nombre='María',
            apellido='Gómez',
            direccion='Av. Cristo Redentor',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-11-20', '%Y-%m-%d')),
            correo='maría.gómez@gmail.com',
            tutor=tutor_218,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_218, id_curso=curso_4to_B)
        tutor_219 = Usuario.objects.create_user(
            username='9000219',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000219',
            nombre='María',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='69278628' if '69278628' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-04-08', '%Y-%m-%d')),
            correo='maría.torres@gmail.com',
            is_active=True
        )
        alumno_219 = Usuario.objects.create_user(
            username='8000219',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000219',
            nombre='Marco',
            apellido='Pérez',
            direccion='Barrio 4 de Noviembre',
            telefono='73279951' if '73279951' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-05-04', '%Y-%m-%d')),
            correo='marco.pérez@gmail.com',
            tutor=tutor_219,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_219, id_curso=curso_4to_B)
        tutor_220 = Usuario.objects.create_user(
            username='9000220',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000220',
            nombre='Laura',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='62142118' if '62142118' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1988-05-30', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_220 = Usuario.objects.create_user(
            username='8000220',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000220',
            nombre='Luis',
            apellido='Mamani',
            direccion='Zona El Trompillo',
            telefono='76470865' if '76470865' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-08-26', '%Y-%m-%d')),
            correo='luis.mamani@gmail.com',
            tutor=tutor_220,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_220, id_curso=curso_4to_B)
        tutor_221 = Usuario.objects.create_user(
            username='9000221',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000221',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Av. Virgen de Cotoca',
            telefono='78074961' if '78074961' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1976-06-23', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_221 = Usuario.objects.create_user(
            username='8000221',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000221',
            nombre='Elena',
            apellido='García',
            direccion='Barrio Los Chacos',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-29', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            tutor=tutor_221,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_221, id_curso=curso_4to_C)
        tutor_222 = Usuario.objects.create_user(
            username='9000222',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000222',
            nombre='Luis',
            apellido='Gómez',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1989-07-20', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            is_active=True
        )
        alumno_222 = Usuario.objects.create_user(
            username='8000222',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000222',
            nombre='Jorge',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='65900089' if '65900089' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-01-18', '%Y-%m-%d')),
            correo='jorge.rojas@gmail.com',
            tutor=tutor_222,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_222, id_curso=curso_4to_C)
        tutor_223 = Usuario.objects.create_user(
            username='9000223',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000223',
            nombre='Elena',
            apellido='Torres',
            direccion='Av. Banzer',
            telefono='70508550' if '70508550' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-08-08', '%Y-%m-%d')),
            correo='elena.torres@gmail.com',
            is_active=True
        )
        alumno_223 = Usuario.objects.create_user(
            username='8000223',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000223',
            nombre='Carlos',
            apellido='García',
            direccion='Av. Cristo Redentor',
            telefono='64891353' if '64891353' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-03-27', '%Y-%m-%d')),
            correo='carlos.garcía@gmail.com',
            tutor=tutor_223,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_223, id_curso=curso_4to_C)
        tutor_224 = Usuario.objects.create_user(
            username='9000224',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000224',
            nombre='Laura',
            apellido='Gómez',
            direccion='Barrio Urbarí',
            telefono='68713474' if '68713474' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1971-11-03', '%Y-%m-%d')),
            correo='laura.gómez@gmail.com',
            is_active=True
        )
        alumno_224 = Usuario.objects.create_user(
            username='8000224',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000224',
            nombre='Luis',
            apellido='Soto',
            direccion='Av. Banzer',
            telefono='61813567' if '61813567' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-01-27', '%Y-%m-%d')),
            correo='luis.soto@gmail.com',
            tutor=tutor_224,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_224, id_curso=curso_4to_C)
        tutor_225 = Usuario.objects.create_user(
            username='9000225',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000225',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Virgen de Cotoca',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1967-05-15', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            is_active=True
        )
        alumno_225 = Usuario.objects.create_user(
            username='8000225',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000225',
            nombre='María',
            apellido='Vargas',
            direccion='Av. Banzer',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-10-21', '%Y-%m-%d')),
            correo='maría.vargas@gmail.com',
            tutor=tutor_225,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_225, id_curso=curso_4to_C)
        tutor_226 = Usuario.objects.create_user(
            username='9000226',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000226',
            nombre='Laura',
            apellido='Rojas',
            direccion='Barrio Equipetrol',
            telefono='66635150' if '66635150' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-06-06', '%Y-%m-%d')),
            correo='laura.rojas@gmail.com',
            is_active=True
        )
        alumno_226 = Usuario.objects.create_user(
            username='8000226',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000226',
            nombre='María',
            apellido='Vargas',
            direccion='Barrio Equipetrol',
            telefono='61456221' if '61456221' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-06', '%Y-%m-%d')),
            correo='maría.vargas@gmail.com',
            tutor=tutor_226,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_226, id_curso=curso_4to_C)
        tutor_227 = Usuario.objects.create_user(
            username='9000227',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000227',
            nombre='Elena',
            apellido='García',
            direccion='Zona El Trompillo',
            telefono='79850106' if '79850106' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-08', '%Y-%m-%d')),
            correo='elena.garcía@gmail.com',
            is_active=True
        )
        alumno_227 = Usuario.objects.create_user(
            username='8000227',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000227',
            nombre='Pedro',
            apellido='Gómez',
            direccion='Av. Roca y Coronado',
            telefono='61878393' if '61878393' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-26', '%Y-%m-%d')),
            correo='pedro.gómez@gmail.com',
            tutor=tutor_227,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_227, id_curso=curso_4to_C)
        tutor_228 = Usuario.objects.create_user(
            username='9000228',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000228',
            nombre='Carlos',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='73036060' if '73036060' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1966-12-30', '%Y-%m-%d')),
            correo='carlos.soto@gmail.com',
            is_active=True
        )
        alumno_228 = Usuario.objects.create_user(
            username='8000228',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000228',
            nombre='Pedro',
            apellido='Quispe',
            direccion='Av. Roca y Coronado',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-16', '%Y-%m-%d')),
            correo='pedro.quispe@gmail.com',
            tutor=tutor_228,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_228, id_curso=curso_4to_C)
        tutor_229 = Usuario.objects.create_user(
            username='9000229',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000229',
            nombre='Marco',
            apellido='Torres',
            direccion='Barrio Urbarí',
            telefono='71097732' if '71097732' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1968-11-14', '%Y-%m-%d')),
            correo='marco.torres@gmail.com',
            is_active=True
        )
        alumno_229 = Usuario.objects.create_user(
            username='8000229',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000229',
            nombre='Luis',
            apellido='Vargas',
            direccion='Barrio Urbarí',
            telefono='67420691' if '67420691' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-26', '%Y-%m-%d')),
            correo='luis.vargas@gmail.com',
            tutor=tutor_229,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_229, id_curso=curso_4to_C)
        tutor_230 = Usuario.objects.create_user(
            username='9000230',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000230',
            nombre='María',
            apellido='Quispe',
            direccion='Barrio Urbarí',
            telefono='64804300' if '64804300' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-08-06', '%Y-%m-%d')),
            correo='maría.quispe@gmail.com',
            is_active=True
        )
        alumno_230 = Usuario.objects.create_user(
            username='8000230',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000230',
            nombre='Elena',
            apellido='Vargas',
            direccion='Barrio Equipetrol',
            telefono='78459469' if '78459469' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-02-04', '%Y-%m-%d')),
            correo='elena.vargas@gmail.com',
            tutor=tutor_230,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_230, id_curso=curso_4to_C)
        tutor_231 = Usuario.objects.create_user(
            username='9000231',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000231',
            nombre='Lucía',
            apellido='Quispe',
            direccion='Barrio 4 de Noviembre',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1994-04-17', '%Y-%m-%d')),
            correo='lucía.quispe@gmail.com',
            is_active=True
        )
        alumno_231 = Usuario.objects.create_user(
            username='8000231',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000231',
            nombre='Lucía',
            apellido='Torres',
            direccion='Barrio Equipetrol',
            telefono='70440483' if '70440483' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-01-06', '%Y-%m-%d')),
            correo='lucía.torres@gmail.com',
            tutor=tutor_231,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_231, id_curso=curso_4to_C)
        tutor_232 = Usuario.objects.create_user(
            username='9000232',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000232',
            nombre='Marco',
            apellido='Quispe',
            direccion='Av. Cristo Redentor',
            telefono='69945029' if '69945029' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-09-30', '%Y-%m-%d')),
            correo='marco.quispe@gmail.com',
            is_active=True
        )
        alumno_232 = Usuario.objects.create_user(
            username='8000232',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000232',
            nombre='Luis',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='78405786' if '78405786' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-05-05', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            tutor=tutor_232,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_232, id_curso=curso_4to_C)
        tutor_233 = Usuario.objects.create_user(
            username='9000233',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000233',
            nombre='Marco',
            apellido='Flores',
            direccion='Av. Virgen de Cotoca',
            telefono='72420478' if '72420478' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1993-12-22', '%Y-%m-%d')),
            correo='marco.flores@gmail.com',
            is_active=True
        )
        alumno_233 = Usuario.objects.create_user(
            username='8000233',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000233',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Roca y Coronado',
            telefono='62747661' if '62747661' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-13', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            tutor=tutor_233,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_233, id_curso=curso_4to_C)
        tutor_234 = Usuario.objects.create_user(
            username='9000234',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000234',
            nombre='Jorge',
            apellido='Gómez',
            direccion='Av. Banzer',
            telefono='67877721' if '67877721' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1992-11-21', '%Y-%m-%d')),
            correo='jorge.gómez@gmail.com',
            is_active=True
        )
        alumno_234 = Usuario.objects.create_user(
            username='8000234',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000234',
            nombre='Luis',
            apellido='Gómez',
            direccion='Zona Centro',
            telefono='79733935' if '79733935' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-10-07', '%Y-%m-%d')),
            correo='luis.gómez@gmail.com',
            tutor=tutor_234,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_234, id_curso=curso_4to_C)
        tutor_235 = Usuario.objects.create_user(
            username='9000235',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000235',
            nombre='Ana',
            apellido='Quispe',
            direccion='Barrio Equipetrol',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1977-05-02', '%Y-%m-%d')),
            correo='ana.quispe@gmail.com',
            is_active=True
        )
        alumno_235 = Usuario.objects.create_user(
            username='8000235',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000235',
            nombre='Laura',
            apellido='García',
            direccion='Av. Banzer',
            telefono='72517076' if '72517076' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-04-01', '%Y-%m-%d')),
            correo='laura.garcía@gmail.com',
            tutor=tutor_235,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_235, id_curso=curso_4to_C)
        tutor_236 = Usuario.objects.create_user(
            username='9000236',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000236',
            nombre='Laura',
            apellido='Pérez',
            direccion='Zona El Trompillo',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1984-10-14', '%Y-%m-%d')),
            correo='laura.pérez@gmail.com',
            is_active=True
        )
        alumno_236 = Usuario.objects.create_user(
            username='8000236',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000236',
            nombre='Marco',
            apellido='Rojas',
            direccion='Av. Cristo Redentor',
            telefono='68841177' if '68841177' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-04', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            tutor=tutor_236,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_236, id_curso=curso_4to_C)
        tutor_237 = Usuario.objects.create_user(
            username='9000237',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000237',
            nombre='Marco',
            apellido='Rojas',
            direccion='Barrio 4 de Noviembre',
            telefono='67388847' if '67388847' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1985-02-23', '%Y-%m-%d')),
            correo='marco.rojas@gmail.com',
            is_active=True
        )
        alumno_237 = Usuario.objects.create_user(
            username='8000237',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000237',
            nombre='Luis',
            apellido='Flores',
            direccion='Barrio Urbarí',
            telefono='' if '' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-08-21', '%Y-%m-%d')),
            correo='luis.flores@gmail.com',
            tutor=tutor_237,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_237, id_curso=curso_4to_C)
        tutor_238 = Usuario.objects.create_user(
            username='9000238',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000238',
            nombre='Carlos',
            apellido='Rojas',
            direccion='Zona El Trompillo',
            telefono='61748434' if '61748434' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1978-10-01', '%Y-%m-%d')),
            correo='carlos.rojas@gmail.com',
            is_active=True
        )
        alumno_238 = Usuario.objects.create_user(
            username='8000238',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000238',
            nombre='Marco',
            apellido='Mamani',
            direccion='Av. Banzer',
            telefono='66756143' if '66756143' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-26', '%Y-%m-%d')),
            correo='marco.mamani@gmail.com',
            tutor=tutor_238,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_238, id_curso=curso_4to_C)
        tutor_239 = Usuario.objects.create_user(
            username='9000239',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000239',
            nombre='Elena',
            apellido='Rojas',
            direccion='Barrio Urbarí',
            telefono='74166864' if '74166864' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1981-09-29', '%Y-%m-%d')),
            correo='elena.rojas@gmail.com',
            is_active=True
        )
        alumno_239 = Usuario.objects.create_user(
            username='8000239',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000239',
            nombre='María',
            apellido='Mamani',
            direccion='Av. Roca y Coronado',
            telefono='62764346' if '62764346' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2007-09-03', '%Y-%m-%d')),
            correo='maría.mamani@gmail.com',
            tutor=tutor_239,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_239, id_curso=curso_4to_C)
        tutor_240 = Usuario.objects.create_user(
            username='9000240',
            password='Tutor123',
            rol='TUTOR/A',
            ci='9000240',
            nombre='Laura',
            apellido='Torres',
            direccion='Zona El Trompillo',
            telefono='71224148' if '71224148' else None,
            fecha_nacimiento=make_aware(datetime.strptime('1990-11-14', '%Y-%m-%d')),
            correo='laura.torres@gmail.com',
            is_active=True
        )
        alumno_240 = Usuario.objects.create_user(
            username='8000240',
            password='Alumno123',
            rol='ALUMNO/A',
            ci='8000240',
            nombre='Elena',
            apellido='Soto',
            direccion='Av. Roca y Coronado',
            telefono='75975699' if '75975699' else None,
            fecha_nacimiento=make_aware(datetime.strptime('2006-12-27', '%Y-%m-%d')),
            correo='elena.soto@gmail.com',
            tutor=tutor_240,
            is_active=True
        )
        AlumnoCurso.objects.create(gestion=2022, id_alumno=alumno_240, id_curso=curso_4to_C)