
from django.core.management.base import BaseCommand
from django.db.models import Avg, Count
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from apps.alumno_curso.models import AlumnoCurso
from apps.asistencia.models import Asistencia
from apps.alumno_actividad.models import AlumnoActividad
from apps.dimension_evaluada.models import DimensionEvaluada
from apps.materia.models import Materia
from apps.resumen_nota.utils import calcular_promedio_por_dimension, calcular_nota_trimestral

class Command(BaseCommand):
    help = 'Entrena un modelo de IA para predecir si un estudiante aprobará un trimestre usando datos reales'

    def handle(self, *args, **kwargs):
        trimestre = 1
        gestion = 2022
        registros = []

        for alumno_curso in AlumnoCurso.objects.filter(gestion=gestion):
            materias = Materia.objects.filter(
                actividades__id_curso=alumno_curso.id_curso,
                actividades__trimestre=trimestre,
                actividades__gestion=gestion
            ).distinct()

            for materia in materias:
                promedios = calcular_promedio_por_dimension(alumno_curso, materia, trimestre, gestion)
                nota_final = calcular_nota_trimestral(promedios)

                asistencias = Asistencia.objects.filter(id_alumno_curso=alumno_curso, id_materia=materia)
                total = asistencias.count()
                presentes = asistencias.filter(presente=True).count()
                porcentaje_asistencia = presentes / total if total else 0

                registros.append({
                    "asistencia_pct": round(porcentaje_asistencia, 2),
                    **{f"promedio_{dim.lower()}": promedios.get(dim, 0) for dim, _ in DimensionEvaluada.DIMENSIONES},
                    "nota_final": nota_final,
                    "aprobado": 1 if nota_final >= 51 else 0
                })

        df = pd.DataFrame(registros)
        if df.empty:
            self.stdout.write(self.style.WARNING("No hay suficientes datos para entrenar."))
            return

        X = df.drop(columns=["nota_final", "aprobado"]).astype("float32")
        y = df["aprobado"].astype("float32")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(32, activation='relu', input_shape=(X.shape[1],)),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        model.fit(X_train, y_train, epochs=30, batch_size=16, validation_split=0.1, verbose=0)

        y_pred = model.predict(X_test).round().astype(int)
        acc = accuracy_score(y_test, y_pred)
        self.stdout.write(self.style.SUCCESS(f'Modelo entrenado correctamente. Precisión: {acc:.2f}'))

        model.save("modelo_aprobacion_trimestre.keras")
        self.stdout.write(self.style.SUCCESS("Modelo guardado como modelo_aprobacion_trimestre.keras"))
