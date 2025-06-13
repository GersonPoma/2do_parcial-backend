from django_filters import FilterSet, NumberFilter

from apps.resumen_nota.models import ResumenNota


class ResumenNotaFilter(FilterSet):
    id_curso = NumberFilter(field_name='id_alumno_curso__id_curso')
    id_alumno = NumberFilter(field_name='id_alumno_curso__id_alumno')
    gestion = NumberFilter(field_name='id_alumno_curso__gestion')

    class Meta:
        model = ResumenNota
        fields = ['id_curso', 'id_alumno', 'gestion']