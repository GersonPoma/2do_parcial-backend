import django_filters
from apps.alumno_actividad.models import AlumnoActividad

class AlumnoActividadFilter(django_filters.FilterSet):
    id_curso = django_filters.NumberFilter(field_name='id_actividad__id_curso')
    id_materia = django_filters.NumberFilter(field_name='id_actividad__id_materia')
    gestion = django_filters.NumberFilter(field_name='id_actividad__gestion')
    trimestre = django_filters.NumberFilter(field_name='id_actividad__trimestre')
    id_alumno = django_filters.NumberFilter(field_name='id_alumno_curso__id_alumno')

    class Meta:
        model = AlumnoActividad
        fields = ['id_curso', 'id_materia', 'gestion', 'trimestre', 'id_alumno']
