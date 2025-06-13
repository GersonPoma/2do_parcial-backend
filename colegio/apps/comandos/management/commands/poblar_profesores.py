from django.core.management.base import BaseCommand
from datetime import date

from apps.usuario.models import Usuario


class Command(BaseCommand):
    help = 'Pobla el sistema con los docentes únicos con datos adicionales.'

    def handle(self, *args, **kwargs):
        profesores = [
            {'ci': '10001', 'nombre': 'Miriam Judit', 'apellido': 'Rojas Mamani'},
            {'ci': '10002', 'nombre': 'Royer', 'apellido': 'Lopez Quispe'},
            {'ci': '10003', 'nombre': 'Maria Elena', 'apellido': 'Gonzales Perez'},
            {'ci': '10004', 'nombre': 'Maria Ester', 'apellido': 'Fernandez Cortez'},
            {'ci': '10005', 'nombre': 'Marioly', 'apellido': 'Salazar Vargas'},
            {'ci': '10006', 'nombre': 'Ana Paola', 'apellido': 'Castro Torrez'},
            {'ci': '10007', 'nombre': 'Jose Daniel', 'apellido': 'Ortega Sanchez'},
            {'ci': '10008', 'nombre': 'Juan Limber', 'apellido': 'Navarro Salazar'},
            {'ci': '10009', 'nombre': 'Ángel Horacio', 'apellido': 'Cortez Lopez'},
            {'ci': '10010', 'nombre': 'Ramón', 'apellido': 'Perez Flores'},
            {'ci': '10011', 'nombre': 'Alicia', 'apellido': 'Mamani Gonzales'},
            {'ci': '10012', 'nombre': 'Roma', 'apellido': 'Sanchez Rojas'},
            {'ci': '10013', 'nombre': 'Juana Elizabeth', 'apellido': 'Vargas Castro'},
            {'ci': '10014', 'nombre': 'Roberto', 'apellido': 'Quispe Salazar'},
            {'ci': '10015', 'nombre': 'Jose', 'apellido': 'Torrez Mamani'},
            {'ci': '10016', 'nombre': 'Fernando', 'apellido': 'Gonzales Rojas'},
            {'ci': '10017', 'nombre': 'David', 'apellido': 'Lopez Fernandez'},
            {'ci': '10018', 'nombre': 'Willy', 'apellido': 'Castro Quispe'},
            {'ci': '10019', 'nombre': 'Esau Franco', 'apellido': 'Vargas Cortez'},
            {'ci': '10020', 'nombre': 'Maria Isabel', 'apellido': 'Perez Mamani'},
            # {'ci': '10021', 'nombre': 'Jimena', 'apellido': 'Salazar Ortega'},
            # {'ci': '10022', 'nombre': 'Rolando', 'apellido': 'Navarro Gonzales'},
            # {'ci': '10023', 'nombre': 'Josefa', 'apellido': 'Rojas Castro'},
            # {'ci': '10024', 'nombre': 'Rosa Amanda', 'apellido': 'Sanchez Flores'},
        ]

        password_fija = "Prof12345"
        total = 0

        for i, profe in enumerate(profesores, start=1):
            usuario, created = Usuario.objects.get_or_create(
                username=profe['ci'],
                defaults={
                    'ci': profe['ci'],
                    'nombre': profe['nombre'],
                    'apellido': profe['apellido'],
                    'rol': Usuario.PROFESOR,
                    'is_active': True,
                }
            )

            if created:
                usuario.set_password(password_fija)

            # Solo agregar datos adicionales a los primeros 20
            if int(profe['ci']) <= 10020:
                usuario.telefono = f'72000{i:03}'
                usuario.direccion = f'Calle Ficticia #{i}'
                usuario.fecha_nacimiento = date(1980 + (i % 10), (i % 12) + 1, ((i % 28) + 1))
                # Construye correo en formato nombre.apellido@gmail.com
                nombre = profe['nombre'].split()[0].lower()
                apellido = profe['apellido'].split()[0].lower()
                usuario.correo = f"{nombre}.{apellido}@gmail.com"

            usuario.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"Profesor creado: {usuario.get_nombre_completo}"))
                total += 1
            else:
                self.stdout.write(f"Ya existía: {usuario.get_nombre_completo}")

        self.stdout.write(self.style.SUCCESS(f"Total profesores creados: {total}"))
