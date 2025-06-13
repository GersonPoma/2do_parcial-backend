from rest_framework.permissions import BasePermission

from apps.usuario.models import Usuario

class HasRolPermission(BasePermission):
    rol_requerido = None

    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.rol == self.rol_requerido
        )

class IsAdmin(HasRolPermission):
    rol_requerido = Usuario.ADMIN

class IsAlumno(HasRolPermission):
    rol_requerido = Usuario.ALUMNO

class IsProfesor(HasRolPermission):
    rol_requerido = Usuario.PROFESOR

class IsDirector(HasRolPermission):
    rol_requerido = Usuario.DIRECTOR

class IsSecretario(HasRolPermission):
    rol_requerido = Usuario.SECRETARIO

class IsTutor(HasRolPermission):
    rol_requerido = Usuario.TUTOR

class OrPermissions(BasePermission):
    def __init__(self, *perms):
        self.perms = [perm() for perm in perms]

    def has_permission(self, request, view):
        return any(perm.has_permission(request, view) for perm in self.perms)
