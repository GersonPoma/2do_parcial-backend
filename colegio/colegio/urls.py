"""
URL configuration for colegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # Ruta para el esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Documentación Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Documentación Redoc (otra UI alternativa)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('api/', include('apps.usuario.urls')), #Usuarios
    path('api/', include('security.urls')),
    path('api/materias/', include('apps.materia.urls')),
    path('api/cursos/', include('apps.curso.urls')),
    path('api/alumnos-cursos/', include('apps.alumno_curso.urls')),
    path('api/asistencias/', include('apps.asistencia.urls')),
    path('api/horarios/', include('apps.horario.urls')),
    path('api/actividades/', include('apps.actividad.urls')),
    path('api/alumnos-actividades/', include('apps.alumno_actividad.urls')),
    path('api/dimesiones-evaluativas/', include('apps.dimension_evaluada.urls')),
    path('api/', include('apps.resumen_nota.urls')),
    path('api/', include('apps.notificacion.urls')),
    path("api/ia/", include("apps.ia.urls")),
]
