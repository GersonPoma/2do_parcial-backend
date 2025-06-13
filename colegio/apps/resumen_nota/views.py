from datetime import datetime
from io import BytesIO

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from apps.alumno_curso.models import AlumnoCurso
from apps.resumen_nota.filters import ResumenNotaFilter
from apps.resumen_nota.models import ResumenNota
from common.permissions import OrPermissions, IsAdmin, IsSecretario, IsDirector


# Create your views here.

class ResumenNotaView(viewsets.ModelViewSet):
    serializer_class = ResumenNota
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ResumenNotaFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [OrPermissions(IsAdmin, IsSecretario, IsDirector)]

        return [IsAdmin()]

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def generar_boletin_pdf(request, alumno_id, gestion=None):
    if gestion is None:
        gestion = datetime.now().year

    alumno_curso_qs = AlumnoCurso.objects.filter(id_alumno__id=alumno_id, gestion=gestion)
    if not alumno_curso_qs.exists():
        return HttpResponse("No se encontró información del alumno en esa gestión.", status=404)

    alumno = alumno_curso_qs.first().id_alumno
    curso = alumno_curso_qs.first().id_curso
    resumenes = ResumenNota.objects.filter(id_alumno_curso__in=alumno_curso_qs).select_related('id_materia')

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=landscape(letter))
    width, height = landscape(letter)
    x_center = width / 2
    y = height - 50

    # Título centrado
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(x_center, y, "Libreta Escolar")
    y -= 30

    # Encabezado institucional (ajustado horizontalmente)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(70, y, "Unidad Educativa:")
    p.setFont("Helvetica", 10)
    p.drawString(180, y, "NACIONAL SAN JOSE")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(70, y - 15, "Distrito:")
    p.setFont("Helvetica", 10)
    p.drawString(180, y - 15, "LA GUARDIA")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(70, y - 30, "Turno:")
    p.setFont("Helvetica", 10)
    p.drawString(180, y - 30, "MAÑANA")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 250, y, "Departamento:")
    p.setFont("Helvetica", 10)
    p.drawString(width - 150, y, "SANTA CRUZ")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(width - 250, y - 30, "Gestión:")
    p.setFont("Helvetica", 10)
    p.drawString(width - 150, y - 30, str(gestion))

    # Celda superior con nombre y curso
    y -= 60
    x_start = (width - 640) / 2
    table_width = 640
    row_height = 18
    p.rect(x_start, y - row_height, table_width, row_height)

    p.setFont("Helvetica-Bold", 10)
    p.drawString(x_start + 6, y - 13, "Nombres y Apellidos:")
    p.setFont("Helvetica", 10)
    p.drawString(x_start + 150, y - 13, alumno.get_nombre_completo)

    p.setFont("Helvetica-Bold", 10)
    p.drawString(x_start + 350, y - 13, "Año de Escolaridad:")
    p.setFont("Helvetica", 10)
    p.drawString(x_start + 500, y - 13, curso.get_detalle_curso)

    y -= row_height

    # Encabezado tabla de notas
    headers = ["Materia", "1er Trimestre", "2do Trimestre", "3er Trimestre", "Nota Anual"]
    col_widths = [200, 110, 110, 110, 110]

    def draw_table_row(values, y_pos, is_header=False):
        x = x_start
        p.setFont("Helvetica-Bold" if is_header else "Helvetica", 10)
        for i, val in enumerate(values):
            p.rect(x, y_pos - row_height, col_widths[i], row_height, stroke=1, fill=0)
            p.drawString(x + 4, y_pos - 13, str(val))
            x += col_widths[i]

    draw_table_row(headers, y, is_header=True)
    y -= row_height

    for resumen in resumenes:
        if y < 130:
            p.showPage()
            y = height - 50
            draw_table_row(headers, y, is_header=True)
            y -= row_height

        draw_table_row([
            resumen.id_materia.nombre,
            resumen.nota_1erT or '-',
            resumen.nota_2doT or '-',
            resumen.nota_3erT or '-',
            resumen.nota_anual or '-'
        ], y)
        y -= row_height

    # Firmas
    footer_y = 40
    label_font = 9
    sub_font = 8

    p.setFont("Helvetica-Bold", label_font)
    p.drawCentredString(100, footer_y + 25, "Maestro/Maestra")
    p.setFont("Helvetica-Bold", sub_font)
    p.drawCentredString(100, footer_y + 12, "firma")

    p.setFont("Helvetica-Bold", label_font)
    p.drawCentredString(x_center - 40, footer_y + 25, "Unidad Educativa")
    p.setFont("Helvetica-Bold", sub_font)
    p.drawCentredString(x_center - 40, footer_y + 12, "Sello")

    p.setFont("Helvetica-Bold", label_font)
    p.drawCentredString(width - 150, footer_y + 25, "Director/Directora Unidad Educativa")
    p.setFont("Helvetica-Bold", sub_font)
    p.drawCentredString(width - 150, footer_y + 12, "firma")

    p.save()
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="boletin_{alumno.get_nombre_completo.replace(" ", "_")}_{gestion}.pdf"'
    return response