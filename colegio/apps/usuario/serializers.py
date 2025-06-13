import random
import string
from datetime import date

from rest_framework import serializers
from .models import Usuario

def generar_password_aleatorio(longitud=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    fecha_registro = serializers.DateField(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'fecha_registro', 'rol', 'nombre', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.set_password(password)
        instance.save()
        return instance

# Super clase para los perfiles serializers
class PerfilSerializer(serializers.ModelSerializer):
    edad = serializers.ReadOnlyField()

    class Meta:
        model = Usuario
        fields = ['id', 'ci', 'nombre', 'apellido', 'fecha_nacimiento', 'edad',
                  'direccion', 'telefono', 'correo']

    def create(self, validated_data):
        # Asignar username igual al ci
        validated_data['username'] = validated_data['ci']

        # Generar contraseña aleatoria
        password_aleatoria = generar_password_aleatorio()

        # Crear usuario sin password aún
        user = Usuario(**validated_data)

        # Asignar contraseña encriptada
        user.set_password(password_aleatoria)
        user.save()

        # Imprimir en consola username y password sin codificar
        print(f"Usuario creado: username={user.username}, password={password_aleatoria}")

        # Si querés, podés agregar el password generado para devolverlo o enviarlo
        user.generated_password = password_aleatoria

        return user

class AlumnoSerializer(PerfilSerializer):
    nombre_completo_tutor = serializers.SerializerMethodField()
    tutor = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(rol=Usuario.TUTOR),
        required=True
    )

    class Meta(PerfilSerializer.Meta):
        fields = PerfilSerializer.Meta.fields + ['nombre_completo_tutor', 'tutor']

    def get_nombre_completo_tutor(self, obj):
        return obj.tutor.get_nombre_completo

    def create(self, validated_data):
        validated_data['rol'] = Usuario.ALUMNO
        return super().create(validated_data)

class ProfesorSerializer(PerfilSerializer):
    class Meta(PerfilSerializer.Meta):
        model = PerfilSerializer.Meta.model
        fields = PerfilSerializer.Meta.fields

    def create(self, validated_data):
        validated_data['rol'] = Usuario.PROFESOR
        return super().create(validated_data)

class DetalleAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'ci', 'nombre', 'apellido']

class TutorSerializer(PerfilSerializer):
    alumnos = DetalleAlumnoSerializer(many=True, read_only=True)

    class Meta(PerfilSerializer.Meta):
        model = PerfilSerializer.Meta.model
        fields = PerfilSerializer.Meta.fields + ['alumnos']

    def create(self, validated_data):
        validated_data['rol'] = Usuario.TUTOR
        return super().create(validated_data)

class SecretarioSerializer(PerfilSerializer):
    class Meta(PerfilSerializer.Meta):
        model = PerfilSerializer.Meta.model
        fields = PerfilSerializer.Meta.fields

    def create(self, validated_data):
        validated_data['rol'] = Usuario.SECRETARIO
        return super().create(validated_data)

class DirectorSerializer(PerfilSerializer):
    class Meta(PerfilSerializer.Meta):
        model = PerfilSerializer.Meta.model
        fields = PerfilSerializer.Meta.fields

    def create(self, validated_data):
        validated_data['rol'] = Usuario.DIRECTOR
        return super().create(validated_data)