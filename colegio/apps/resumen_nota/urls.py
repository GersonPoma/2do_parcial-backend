from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.resumen_nota.views import ResumenNotaView, generar_boletin_pdf

router = DefaultRouter()
router.register(r'resumen-notas', ResumenNotaView, basename='resumen-notas')

urlpatterns = router.urls + [
    path('boletin/<int:alumno_id>/', generar_boletin_pdf, name='boletin-pdf'),
    path('boletin/<int:alumno_id>/<int:gestion>/', generar_boletin_pdf, name='boletin-pdf-gestion'),
]