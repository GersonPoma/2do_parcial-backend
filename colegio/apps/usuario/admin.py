# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Form para creación de usuario en admin
class UsuarioCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'rol')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Form para cambio de usuario en admin
class UsuarioChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = '__all__'

# Admin personalizado
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario

    list_display = ('id', 'username', 'rol', 'nombre', 'apellido', 'is_active', 'is_staff', 'fecha_registro')
    list_filter = ('rol', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {
            'fields': (
                'rol', 'ci', 'nombre', 'apellido', 'direccion',
                'telefono', 'fecha_nacimiento', 'correo', 'tutor'
            )
        }),
        ('Permisos y estado', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        # ('Fechas', {'fields': ('fecha_registro',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'rol', 'password1', 'password2',
                'ci', 'nombre', 'apellido', 'direccion',
                'telefono', 'fecha_nacimiento', 'correo', 'tutor',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

    search_fields = ('username', 'ci', 'nombre', 'apellido')
    ordering = ('id',)

# Registrar el modelo
admin.site.register(Usuario, UsuarioAdmin)