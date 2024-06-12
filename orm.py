import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_academy.settings')
import django
django.setup()

from django.db.models import Q, Avg, Count, Max, Min, Sum, F
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from datetime import date, datetime, timedelta
from decimal import Decimal

from core.models import (
    Periodo, Asignatura, Profesor, Estudiante, Nota, DetalleNota
)

# ------------------------------------------------------------------------------
# CONSULTAS
# ------------------------------------------------------------------------------

def estudiantes_empiezan_con_Est():
    return Estudiante.objects.filter(nombre__startswith="Est")

def profesores_contienen_or():
    return Profesor.objects.filter(nombre__icontains="or")

def asignaturas_terminan_en_10():
    return Asignatura.objects.filter(descripcion__endswith="10")

def estudiantes_empiezan_con_Est_terminan_en_1():
    return Estudiante.objects.filter(Q(nombre__startswith="Est") & Q(cedula__endswith="1"))

def asignaturas_contienen_Asig_o_terminan_en_5():
    return Asignatura.objects.filter(Q(descripcion__icontains="Asig") | Q(descripcion__endswith="5"))

def profesores_no_contienen_or():
    return Profesor.objects.exclude(nombre__icontains="or")

def notas_entre_7_y_9():
    return Nota.objects.filter(nota1__range=(7, 9))

def notas_no_entre_6_y_8():
    return Nota.objects.exclude(nota2__range=(6, 8))

def notas_ultimo_año():
    return Nota.objects.filter(created__gte=datetime.now() - timedelta(days=365))

def estudiantes_nombre_10_caracteres():
    return Estudiante.objects.filter(nombre__exact=10)

def notas_ambas_mayores_a_7_5():
    return Nota.objects.filter(nota1__gt=7.5, nota2__gt=7.5)

def estudiantes_con_recuperacion():
    return Estudiante.objects.filter(nota__recuperacion__isnull=False).distinct()

def profesores_de_matematicas_1():
    return Profesor.objects.filter(nota__asignatura__nombre="Matemáticas I").distinct()

def asignaturas_con_notas():
    return Asignatura.objects.annotate(num_notas=Count('nota')).filter(num_notas__gt=0)

def notas_de_estudiante(cedula_estudiante):
    estudiante = get_object_or_404(Estudiante, cedula=cedula_estudiante)
    return estudiante.nota_set.all()

def notas_de_periodo(nombre_periodo):
    periodo = get_object_or_404(Periodo, nombre=nombre_periodo)
    return periodo.nota_set.all()

def suma_notas_estudiante(cedula_estudiante):
    estudiante = get_object_or_404(Estudiante, cedula=cedula_estudiante)
    return Nota.objects.filter(estudiante=estudiante).aggregate(suma=Sum('promedio'))['suma']

def nota_maxima_estudiante(cedula_estudiante):
    estudiante = get_object_or_404(Estudiante, cedula=cedula_estudiante)
    return Nota.objects.filter(estudiante=estudiante).aggregate(Max('promedio'))['promedio__max']

def nota_minima_estudiante(cedula_estudiante):
    estudiante = get_object_or_404(Estudiante, cedula=cedula_estudiante)
    return Nota.objects.filter(estudiante=estudiante).aggregate(Min('promedio'))['promedio__min']

def promedio_notas_estudiante(cedula_estudiante):
    estudiante = get_object_or_404(Estudiante, cedula=cedula_estudiante)
    return Nota.objects.filter(estudiante=estudiante).aggregate(Avg('promedio'))['promedio__avg']

# ------------------------------------------------------------------------------
# ACTUALIZACIONES
# ------------------------------------------------------------------------------

def actualizar_nota1_menor_20():
    return Nota.objects.filter(nota1__lt=20).update(nota1=20)

# ------------------------------------------------------------------------------
# ELIMINACIONES
# ------------------------------------------------------------------------------

def eliminar_galleta_maria():
    try:
        brand = Brand.objects.get(description='Galleta Maria')
        brand.delete()
        return True
    except Brand.DoesNotExist:
        return False

# ------------------------------------------------------------------------------
# EJECUCIÓN
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    # Llama a las funciones que deseas probar aquí
    print(estudiantes_empiezan_con_Est())
    print(profesores_contienen_or())
    print(asignaturas_terminan_en_10())
    print(estudiantes_empiezan_con_Est_terminan_en_1())
    print(asignaturas_contienen_Asig_o_terminan_en_5())
    print(profesores_no_contienen_or())
    print(notas_entre_7_y_9())
    print(notas_no_entre_6_y_8())
    print(notas_ultimo_año())
    print(estudiantes_nombre_10_caracteres())
    print(notas_ambas_mayores_a_7_5())
    print(estudiantes_con_recuperacion())
    print(profesores_de_matematicas_1())
    print(asignaturas_con_notas())
    print(notas_de_estudiante('2000000001'))
    print(notas_de_periodo('Periodo 1-2023'))
    print(suma_notas_estudiante('2000000001'))
    print(nota_maxima_estudiante('2000000001'))
    print(nota_minima_estudiante('2000000001'))
    print(promedio_notas_estudiante('2000000001'))
    print(actualizar_nota1_menor_20())
    print(eliminar_galleta_maria())
