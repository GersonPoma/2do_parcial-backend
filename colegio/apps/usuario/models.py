from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# Custom manager
class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El nombre de usuario es obligatorio")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

# Modelo Usuario personalizado
class Usuario(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'ADMIN'
    ALUMNO = 'ALUMNO/A'
    PROFESOR = 'PROFESOR/A'
    DIRECTOR = 'DIRECTOR/A'
    SECRETARIO = 'SECRETARIO/A'
    TUTOR = 'TUTOR/A'

    ROL_CHOICES = (
        (ADMIN, 'Administrador'),
        (ALUMNO, 'Alumno/a'),
        (PROFESOR, 'Profesor/a'),
        (DIRECTOR, 'Director/a'),
        (SECRETARIO, 'Secretario/a'),
        (TUTOR, 'Tutor/a'),
    )

    username = models.CharField(max_length=150, unique=True)
    #password = models.CharField(max_length=128)  # lo maneja AbstractBaseUser
    fecha_registro = models.DateField(auto_now_add=True)
    rol = models.CharField(max_length=12, choices=ROL_CHOICES)
    ci = models.CharField(max_length=12, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    tutor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,  # Puede no tener tutor (opcional)
        blank=True,
        related_name='alumnos'  # Permite acceder a todos los alumnos de un tutor con tutor.alumnos.all()
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Necesario para usar el admin

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol']

    @property
    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def get_edad(self):
        if self.fecha_nacimiento:
            hoy = date.today()
            edad = hoy.year - self.fecha_nacimiento.year

            if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
                edad -= 1

            return edad
        else:
            return None

    def __str__(self):
        return self.username