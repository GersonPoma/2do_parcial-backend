from django_filters.rest_framework import FilterSet, NumberFilter

from ..asistencia.models import Asistencia


class AsistenciaFilter(FilterSet):
    id_curso = NumberFilter(field_name='id_alumno_curso__id_curso')
    gestion = NumberFilter(field_name='id_alumno_curso__gestion')
    id_alumno = NumberFilter(field_name='id_alumno_curso__id_alumno')
    class Meta:
        model = Asistencia
        fields = ['fecha', 'id_materia', 'id_curso', 'gestion', 'id_alumno']