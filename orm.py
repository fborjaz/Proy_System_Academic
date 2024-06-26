import os
import django
import random
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.db.models import Q, Avg, Count, F, Value, CharField, Max, Min, Sum
from django.http import Http404
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.shortcuts import get_object_or_404
from core.models import Periodo, Asignatura, Profesor, Estudiante, Nota, DetalleNota
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from tabulate import tabulate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_academy.settings')
django.setup()

from django.contrib.auth.models import User

def create_user(create=True):
    if create:
        User.objects.create_user(username='Frank_', password='1234', email='frankBorja@gmail.com')
        print("Usuario creado.")
    else:
        print("No se creó el usuario.")

def insertar_periodos(user):
    periodos = [
        Periodo(user=user, nombre='Periodo 1', fecha_inicio=date(2023, 1, 1), fecha_fin=date(2023, 6, 30), año=2023),
        Periodo(user=user, nombre='Periodo 2', fecha_inicio=date(2023, 7, 1), fecha_fin=date(2023, 12, 31), año=2023),
        Periodo(user=user, nombre='Periodo 3', fecha_inicio=date(2024, 1, 1), fecha_fin=date(2024, 6, 30), año=2024),
        Periodo(user=user, nombre='Periodo 4', fecha_inicio=date(2024, 7, 1), fecha_fin=date(2024, 12, 31), año=2024),
        Periodo(user=user, nombre='Periodo 5', fecha_inicio=date(2025, 1, 1), fecha_fin=date(2025, 6, 30), año=2025),
        Periodo(user=user, nombre='Periodo 6', fecha_inicio=date(2025, 7, 1), fecha_fin=date(2025, 12, 31), año=2025),
        Periodo(user=user, nombre='Periodo 7', fecha_inicio=date(2026, 1, 1), fecha_fin=date(2026, 6, 30), año=2026),
        Periodo(user=user, nombre='Periodo 8', fecha_inicio=date(2026, 7, 1), fecha_fin=date(2026, 12, 31), año=2026),
        Periodo(user=user, nombre='Periodo 9', fecha_inicio=date(2027, 1, 1), fecha_fin=date(2027, 6, 30), año=2027),
        Periodo(user=user, nombre='Periodo 10', fecha_inicio=date(2027, 7, 1), fecha_fin=date(2027, 12, 31), año=2027),
    ]
    Periodo.objects.bulk_create(periodos)
    print(f'Se han creado {len(periodos)} periodos académicos.')

def insertar_asignaturas(user):
    asignaturas = [
        Asignatura(user=user, nombre='Matemáticas', descripcion='Curso de matemáticas', creditos=4),
        Asignatura(user=user, nombre='Física', descripcion='Curso de física', creditos=3),
        Asignatura(user=user, nombre='Programación', descripcion='Curso de programación', creditos=5),
        Asignatura(user=user, nombre='Literatura', descripcion='Curso de literatura', creditos=3),
        Asignatura(user=user, nombre='Historia', descripcion='Curso de historia', creditos=3),
        Asignatura(user=user, nombre='Biología', descripcion='Curso de biología', creditos=4),
        Asignatura(user=user, nombre='Química', descripcion='Curso de química', creditos=4),
        Asignatura(user=user, nombre='Geografía', descripcion='Curso de geografía', creditos=3),
        Asignatura(user=user, nombre='Arte', descripcion='Curso de arte', creditos=3),
        Asignatura(user=user, nombre='Música', descripcion='Curso de música', creditos=3),
    ]
    Asignatura.objects.bulk_create(asignaturas)
    print(f'Se han creado {len(asignaturas)} asignaturas.')

def insertar_profesores(user):
    profesores = [
        Profesor(user=user, nombre='Juan', apellido='Pérez', cedula='6758901234', titulo='Ing.', especialidad='Software'),
        Profesor(user=user, nombre='María', apellido='González', cedula='2987654321', titulo='Dra.', especialidad='Matemáticas'),
        Profesor(user=user, nombre='Ana', apellido='Martínez', cedula='9012345678', titulo='Lic.', especialidad='Física'),
        Profesor(user=user, nombre='Luis', apellido='Ramírez', cedula='5554443332', titulo='Mg.', especialidad='Historia'),
        Profesor(user=user, nombre='Carlos', apellido='Sánchez', cedula='1112223334', titulo='Dr.', especialidad='Biología'),
        Profesor(user=user, nombre='Laura', apellido='Gómez', cedula='7778889990', titulo='Ing.', especialidad='Química'),
        Profesor(user=user, nombre='Pedro', apellido='Castro', cedula='4321098765', titulo='Lic.', especialidad='Geografía'),
        Profesor(user=user, nombre='Lucía', apellido='Herrera', cedula='8887776665', titulo='Mg.', especialidad='Arte'),
        Profesor(user=user, nombre='Miguel', apellido='Ruiz', cedula='3141592653', titulo='Dr.', especialidad='Música'),
        Profesor(user=user, nombre='Sofía', apellido='López', cedula='5820852941', titulo='Ing.', especialidad='Literatura'),
    ]
    try:
        Profesor.objects.bulk_create(profesores)
        print(f'Se han creado {len(profesores)} profesores.')
    except IntegrityError:
        print("Error: No se pudieron crear los profesores. Verifica que las cédulas sean únicas.")

def insertar_estudiantes(user):
    estudiantes = [
        Estudiante(user=user, nombre='Est 1', apellido='Apellido1', cedula='1234567891', fecha_nacimiento=date(2000, 1, 1), email='est1@example.com'),
        Estudiante(user=user, nombre='Est 2', apellido='Apellido2', cedula='0987654322', fecha_nacimiento=date(2001, 2, 2), email='est2@example.com'),
        Estudiante(user=user, nombre='Est 3', apellido='Apellido3', cedula='5432167893', fecha_nacimiento=date(2002, 3, 3), email='est3@example.com'),
        Estudiante(user=user, nombre='Est 4', apellido='Apellido4', cedula='0987654324', fecha_nacimiento=date(2003, 4, 4), email='est4@example.com'),
        Estudiante(user=user, nombre='Est 5', apellido='Apellido5', cedula='1234509875', fecha_nacimiento=date(2004, 5, 5), email='est5@example.com'),
        Estudiante(user=user, nombre='Est 6', apellido='Apellido6', cedula='6789054326', fecha_nacimiento=date(2005, 6, 6), email='est6@example.com'),
        Estudiante(user=user, nombre='Est 7', apellido='Apellido7', cedula='5432109877', fecha_nacimiento=date(2006, 7, 7), email='est7@example.com'),
        Estudiante(user=user, nombre='Est 8', apellido='Apellido8', cedula='0987654328', fecha_nacimiento=date(2007, 8, 8), email='est8@example.com'),
        Estudiante(user=user, nombre='Est 9', apellido='Apellido9', cedula='1234567899', fecha_nacimiento=date(2008, 9, 9), email='est9@example.com'),
        Estudiante(user=user, nombre='Est 10', apellido='Apellido10', cedula='5678901230', fecha_nacimiento=date(2009, 10, 10), email='est10@example.com'),
    ]
    Estudiante.objects.bulk_create(estudiantes)
    print(f'Se han creado {len(estudiantes)} estudiantes.')

def insertar_notas(user, estudiantes, periodos, asignaturas, profesores):
    for periodo in periodos:
        for asignatura in asignaturas:
            profesor = random.choice(profesores)
            estudiante = random.choice(estudiantes)

            try:
                nota = Nota.objects.create(
                    user=user,
                    periodo=periodo,
                    asignatura=asignatura,
                    profesor=profesor,
                    estudiante=estudiante,
                    nota1=round(random.uniform(0, 20), 2),
                    nota2=round(random.uniform(0, 20), 2),
                    recuperacion=round(random.uniform(0, 20), 2) if random.random() < 0.3 else None,
                    estado=random.choice(['Aprobado', 'Reprobado']),
                )
                DetalleNota.objects.create(
                    user=user,
                    nota=nota,
                    descripcion=random.choice(['Examen', 'Tarea', 'Proyecto']),
                    porcentaje=random.randint(10, 50),
                )
            except ObjectDoesNotExist:
                print(f"Error: No se pudo crear la nota para el estudiante {estudiante} en {asignatura} del periodo {periodo}.")
    print(f'Se han creado notas y sus detalles.')

# Consultas ORM

# Consultas Básicas: 1 - 6
def consulta_1(user_id=None):
    estudiantes_est = Estudiante.objects.filter(nombre__startswith='Est', user_id=user_id)
    print("\nConsulta 1: Estudiantes cuyo nombre empieza con 'Est':")
    for estudiante in estudiantes_est:
        print(f"  - {estudiante.nombre} {estudiante.apellido} (ID: {estudiante.id})")

def consulta_2(user_id=None):
    profesores_or = Profesor.objects.filter(nombre__icontains='or', user_id=user_id)
    print("\nConsulta 2: Profesores cuyo nombre contiene 'or':")
    for profesor in profesores_or:
        print(f"  - {profesor.nombre} {profesor.apellido}")

def consulta_3(user_id=None):
    asignaturas_a = Asignatura.objects.filter(descripcion__endswith='a', user_id=user_id)
    print("\nConsulta 3: Asignaturas cuya descripción termina en 'a':")
    for asignatura in asignaturas_a:
        print(f"  - {asignatura.nombre}")

def consulta_4(user_id=None):
    notas_mayores_8 = Nota.objects.filter(nota1__gt=8.0, user_id=user_id)
    print("\nConsulta 4: Notas con nota1 mayor que 8.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1) for nota in notas_mayores_8], headers=["ID", "Estudiante", "Nota 1"]))

def consulta_5(user_id=None):
    notas_menores_9 = Nota.objects.filter(nota2__lt=9.0, user_id=user_id)
    print("\nConsulta 5: Notas con nota2 menor que 9.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota2) for nota in notas_menores_9], headers=["ID", "Estudiante", "Nota 2"]))

def consulta_6(user_id=None):
    notas_recuperacion_9_5 = Nota.objects.filter(recuperacion=9.5, user_id=user_id)
    print("\nConsulta 6: Notas con recuperación igual a 9.5:")
    print(tabulate([(nota.id, nota.estudiante, nota.recuperacion) for nota in notas_recuperacion_9_5], headers=["ID", "Estudiante", "Recuperación"]))

# Consultas con Condiciones Lógicas 7 - 11
def consulta_7(user_id=None):
    estudiantes_est_cedula_1 = Estudiante.objects.filter(nombre__startswith='Est', cedula__endswith='1', user_id=user_id)
    print("\nConsulta 7: Estudiantes cuyo nombre empieza con 'Est' y su cédula termina en '1':")
    for estudiante in estudiantes_est_cedula_1:
        print(f"  - {estudiante.nombre} {estudiante.apellido} (Cédula: {estudiante.cedula})")

def consulta_8(user_id=None):
    asignaturas_curso_o_a = Asignatura.objects.filter(Q(descripcion__icontains='Curso') | Q(descripcion__endswith='a'), user_id=user_id)
    print("\nConsulta 8: Asignaturas cuya descripción contiene 'Curso' o termina en 'a':")
    for asignatura in asignaturas_curso_o_a:
        print(f"  - {asignatura.nombre} (Descripción: {asignatura.descripcion})")

def consulta_9(user_id=None):
    profesores_no_or = Profesor.objects.filter(~Q(nombre__icontains='or'), user_id=user_id)
    print("\nConsulta 9: Profesores cuyo nombre NO contiene 'or':")
    for profesor in profesores_no_or:
        print(f"  - {profesor.nombre} {profesor.apellido}")

def consulta_10(user_id=None):
    notas_7_8 = Nota.objects.filter(nota1__gt=7.0, nota2__lt=8.0, user_id=user_id)
    print("\nConsulta 10: Notas con nota1 mayor que 7.0 y nota2 menor que 8.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_7_8], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_11(user_id=None):
    notas_recuperacion_none_o_nota2_mayor_9 = Nota.objects.filter(Q(recuperacion__isnull=True) | Q(nota2__gt=9.0), user_id=user_id)
    print("\nConsulta 11: Notas con recuperación igual a None o nota2 mayor que 9.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota2, nota.recuperacion) for nota in notas_recuperacion_none_o_nota2_mayor_9], headers=["ID", "Estudiante", "Nota 2", "Recuperación"]))

# Consultas con Funciones Numéricas: 12 - 14
def consulta_12(user_id=None):
    notas_nota1_entre_7_y_9 = Nota.objects.filter(nota1__range=(7.0, 9.0), user_id=user_id)
    print("\nConsulta 12: Notas con nota1 entre 7.0 y 9.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1) for nota in notas_nota1_entre_7_y_9], headers=["ID", "Estudiante", "Nota 1"]))

def consulta_13(user_id=None):
    notas_nota2_fuera_de_rango_6_8 = Nota.objects.exclude(nota2__range=(6.0, 8.0), user_id=user_id)
    print("\nConsulta 13: Notas con nota2 fuera del rango 6.0 a 8.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota2) for nota in notas_nota2_fuera_de_rango_6_8], headers=["ID", "Estudiante", "Nota 2"]))

def consulta_14(user_id=None):
    notas_recuperacion_no_null = Nota.objects.filter(recuperacion__isnull=False, user_id=user_id)
    print("\nConsulta 14: Notas cuya recuperación no sea None:")
    print(tabulate([(nota.id, nota.estudiante, nota.recuperacion) for nota in notas_recuperacion_no_null], headers=["ID", "Estudiante", "Recuperación"]))

# Consultas con Funciones de Fecha: 15 - 19
def consulta_15(user_id=None):
    hace_un_anio = timezone.now() - timedelta(days=365)
    notas_ultimo_anio = Nota.objects.filter(created__gte=hace_un_anio, user_id=user_id)
    print("\nConsulta 15: Notas creadas en el último año:")
    print(tabulate([(nota.id, nota.estudiante, nota.created) for nota in notas_ultimo_anio], headers=["ID", "Estudiante", "Fecha Creación"]))

def consulta_16(user_id=None):
    hace_un_mes = timezone.now() - timedelta(days=30)
    notas_ultimo_mes = Nota.objects.filter(created__gte=hace_un_mes, user_id=user_id)
    print("\nConsulta 16: Notas creadas en el último mes:")
    print(tabulate([(nota.id, nota.estudiante, nota.created) for nota in notas_ultimo_mes], headers=["ID", "Estudiante", "Fecha Creación"]))

def consulta_17(user_id=None):
    hace_un_dia = timezone.now() - timedelta(days=1)
    notas_ultimo_dia = Nota.objects.filter(created__gte=hace_un_dia, user_id=user_id)
    print("\nConsulta 17: Notas creadas en el último día:")
    print(tabulate([(nota.id, nota.estudiante, nota.created) for nota in notas_ultimo_dia], headers=["ID", "Estudiante", "Fecha Creación"]))

def consulta_18(user_id=None):
    notas_antes_2023 = Nota.objects.filter(created__year__lt=2023, user_id=user_id)
    print("\nConsulta 18: Notas creadas antes del año 2023:")
    print(tabulate([(nota.id, nota.estudiante, nota.created) for nota in notas_antes_2023], headers=["ID", "Estudiante", "Fecha Creación"]))

def consulta_19(user_id=None):
    notas_marzo = Nota.objects.filter(created__month=3, user_id=user_id)
    print("\nConsulta 19: Notas creadas en marzo de cualquier año:")
    print(tabulate([(nota.id, nota.estudiante, nota.created) for nota in notas_marzo], headers=["ID", "Estudiante", "Fecha Creación"]))

# Consultas Combinadas con Funciones Avanzadas: 20 - 24
def consulta_20(user_id=None):
    estudiantes_10_caracteres = Estudiante.objects.annotate(nombre_length=Length('nombre')).filter(nombre_length__exact=10, user_id=user_id)
    print("\nConsulta 20: Estudiantes cuyo nombre tiene exactamente 10 caracteres:")
    for estudiante in estudiantes_10_caracteres:
        print(f"  - {estudiante.nombre} {estudiante.apellido}")

def consulta_21(user_id=None):
    notas_mayores_7_5 = Nota.objects.filter(nota1__gt=7.5, nota2__gt=7.5, user_id=user_id)
    print("\nConsulta 21: Notas con nota1 y nota2 mayores a 7.5:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_mayores_7_5], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_22(user_id=None):
    notas_recuperacion_y_nota1_mayor_nota2 = Nota.objects.filter(recuperacion__isnull=False, nota1__gt=F('nota2'), user_id=user_id)
    print("\nConsulta 22: Notas con recuperación no nula y nota1 mayor a nota2:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2, nota.recuperacion) for nota in notas_recuperacion_y_nota1_mayor_nota2], headers=["ID", "Estudiante", "Nota 1", "Nota 2", "Recuperación"]))

def consulta_23(user_id=None):
    notas_nota1_mayor_8_o_nota2_igual_7_5 = Nota.objects.filter(Q(nota1__gt=8.0) | Q(nota2=7.5), user_id=user_id)
    print("\nConsulta 23: Notas con nota1 mayor a 8.0 o nota2 igual a 7.5:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_nota1_mayor_8_o_nota2_igual_7_5], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_24(user_id=None):
    notas_recuperacion_mayor_nota1_y_nota2 = Nota.objects.filter(Q(recuperacion__gt=F('nota1')) & Q(recuperacion__gt=F('nota2')), user_id=user_id)
    print("\nConsulta 24: Notas con recuperación mayor a nota1 y nota2:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2, nota.recuperacion) for nota in notas_recuperacion_mayor_nota1_y_nota2], headers=["ID", "Estudiante", "Nota 1", "Nota 2", "Recuperación"]))

# Consultas con Subconsultas y Anotaciones: 25 - 39
def consulta_25(user_id=None):
    estudiantes_con_recuperacion = Estudiante.objects.filter(nota__recuperacion__isnull=False, user_id=user_id).distinct()
    print("\nConsulta 25: Estudiantes con al menos una nota de recuperación:")
    for estudiante in estudiantes_con_recuperacion:
        print(f"  - {estudiante.nombre} {estudiante.apellido}")

def consulta_26(user_id=None):
    try:
        asignatura_especifica = Asignatura.objects.get(descripcion='Matemáticas', user_id=user_id)
        profesores_asignatura_especifica = Profesor.objects.filter(nota__asignatura=asignatura_especifica, user_id=user_id).distinct()
        print("\nConsulta 26: Profesores que han dado 'Matemáticas':")
        for profesor in profesores_asignatura_especifica:
            print(f"  - {profesor.nombre} {profesor.apellido}")
    except Asignatura.DoesNotExist:
        print(f"Error: No se pudo encontrar la asignatura 'Matemáticas' para el usuario {user_id}.")

def consulta_27(user_id=None):
    asignaturas_con_notas = Asignatura.objects.filter(nota__isnull=False, user_id=user_id).distinct()
    print("\nConsulta 27: Asignaturas que tienen al menos una nota registrada:")
    for asignatura in asignaturas_con_notas:
        print(f"  - {asignatura.nombre}")

def consulta_28(user_id=None):
    asignaturas_sin_notas = Asignatura.objects.filter(nota__isnull=True, user_id=user_id)
    print("\nConsulta 28: Asignaturas que NO tienen notas registradas:")
    for asignatura in asignaturas_sin_notas:
        print(f"  - {asignatura.nombre}")

def consulta_29(user_id=None):
    estudiantes_sin_recuperacion = Estudiante.objects.filter(nota__recuperacion__isnull=True, user_id=user_id).distinct()
    print("\nConsulta 29: Estudiantes que NO tienen notas de recuperación:")
    for estudiante in estudiantes_sin_recuperacion:
        print(f"  - {estudiante.nombre} {estudiante.apellido}")

def consulta_30(user_id=None):
    promedio_notas = Nota.objects.filter(user_id=user_id).annotate(
        promedio_notas=Cast(F('nota1') + F('nota2'), FloatField()) / 2
    )
    print("\nConsulta 30: Promedio de nota1 y nota2 de cada nota:")
    print(tabulate([(nota.id, nota.estudiante, nota.promedio_notas) for nota in promedio_notas], headers=["ID", "Estudiante", "Promedio"]))

def consulta_31(user_id=None):
    notas_nota1_menor_6_nota2_mayor_7 = Nota.objects.filter(nota1__lt=6.0, nota2__gt=7.0, user_id=user_id)
    print("\nConsulta 31: Notas con nota1 menor que 6.0 y nota2 mayor que 7.0:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_nota1_menor_6_nota2_mayor_7], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_32(user_id=None):
    notas_nota1_en_lista = Nota.objects.filter(nota1__in=[7.0, 8.0, 9.0], user_id=user_id)
    print("\nConsulta 32: Notas con nota1 en la lista [7.0, 8.0, 9.0]:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1) for nota in notas_nota1_en_lista], headers=["ID", "Estudiante", "Nota 1"]))

def consulta_33(user_id=None):
    notas_rango_id = Nota.objects.filter(id__range=(1, 5), user_id=user_id)
    print("\nConsulta 33: Notas cuyo id está en un rango del 1 al 5:")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_rango_id], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_34(user_id=None):
    notas_recuperacion_no_en_lista = Nota.objects.exclude(recuperacion__in=[8.0, 9.0, 10.0], user_id=user_id)
    print("\nConsulta 34: Notas cuyo recuperacion NO está en la lista [8.0, 9.0, 10.0]:")
    print(tabulate([(nota.id, nota.estudiante, nota.recuperacion) for nota in notas_recuperacion_no_en_lista], headers=["ID", "Estudiante", "Recuperación"]))

def consulta_35(user_id=None):
    while True:
        try:
            estudiante_id = int(input("Ingrese el ID del estudiante para consultar sus notas: "))
            suma_notas_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(suma_notas=Sum('nota1'))['suma_notas']
            if suma_notas_estudiante is not None:
                print(f"\nConsulta 35: Suma de todas las notas del estudiante con ID {estudiante_id}: {suma_notas_estudiante}")
            else:
                print(f"El estudiante con ID {estudiante_id} no tiene notas registradas.")
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
        except Estudiante.DoesNotExist:
            print(f"Error: No se encontró ningún estudiante con el ID {estudiante_id}.")

def consulta_36(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para consultar su nota máxima: "))
    nota_maxima_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(Max('nota1'))['nota1__max']
    print(f"\nConsulta 36: Nota máxima obtenida por el estudiante con ID {estudiante_id}: {nota_maxima_estudiante}")

def consulta_37(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para consultar su nota mínima: "))
    nota_minima_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(Min('nota1'))['nota1__min']
    print(f"\nConsulta 37: Nota mínima obtenida por el estudiante con ID {estudiante_id}: {nota_minima_estudiante}")

def consulta_38(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para contar sus notas: "))
    total_notas_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).count()
    print(f"\nConsulta 38: Número total de notas del estudiante con ID {estudiante_id}: {total_notas_estudiante}")

def consulta_39(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para calcular su promedio (sin recuperación): "))
    promedio_sin_recuperacion = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).exclude(recuperacion__isnull=False).aggregate(Avg('nota1'))['nota1__avg']
    if promedio_sin_recuperacion is not None:
        print(f"\nConsulta 39: Promedio de notas del estudiante con ID {estudiante_id} (sin recuperación): {promedio_sin_recuperacion}")
    else:
        print(f"El estudiante con ID {estudiante_id} no tiene notas registradas (sin recuperación).")

# Consultas con Relaciones Inversas: 40 - 49
def consulta_40(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para ver sus notas y detalles: "))
    notas_estudiante_detalle = Nota.objects.filter(estudiante=estudiante_id).prefetch_related('detallenota_set')
    print(f"\nConsulta 40: Notas del estudiante con ID {estudiante_id} y sus detalles:")
    for nota in notas_estudiante_detalle:
        print(f"  - {nota}:")
        for detalle in nota.detallenota_set.all():
            print(f"    - {detalle}")

def consulta_41(user_id=None):
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    notas_periodo_especifico = Nota.objects.filter(periodo=periodo_especifico, user_id=user_id)
    print(f"\nConsulta 41: Notas del período '{periodo_especifico}':")
    print(tabulate([(nota.id, nota.estudiante, nota.asignatura, nota.nota1, nota.nota2) for nota in notas_periodo_especifico], headers=["ID", "Estudiante", "Asignatura", "Nota 1", "Nota 2"]))

def consulta_42(user_id=None):
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    asignatura_especifica = Asignatura.objects.get(nombre='Matemáticas', user_id=user_id)
    notas_asignatura_periodo = Nota.objects.filter(asignatura=asignatura_especifica, periodo=periodo_especifico, user_id=user_id)
    print(f"\nConsulta 42: Notas de '{asignatura_especifica}' en el periodo '{periodo_especifico}':")
    print(tabulate([(nota.id, nota.estudiante, nota.nota1, nota.nota2) for nota in notas_asignatura_periodo], headers=["ID", "Estudiante", "Nota 1", "Nota 2"]))

def consulta_43(user_id=None):
    profesor_especifico = Profesor.objects.get(cedula='9012345678', user_id=user_id)
    notas_profesor = Nota.objects.filter(profesor=profesor_especifico, user_id=user_id)
    print(f"\nConsulta 43: Notas del profesor '{profesor_especifico.nombre} {profesor_especifico.apellido}':")
    print(tabulate([(nota.id, nota.estudiante, nota.asignatura, nota.nota1, nota.nota2) for nota in notas_profesor], headers=["ID", "Estudiante", "Asignatura", "Nota 1", "Nota 2"]))

def consulta_44(user_id=None):
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891', user_id=user_id)
    notas_estudiante_altas = Nota.objects.filter(estudiante=estudiante_especifico, nota1__gt=15.0, user_id=user_id)
    print(f"\nConsulta 44: Notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' superiores a 15.0:")
    print(tabulate([(nota.id, nota.asignatura, nota.nota1) for nota in notas_estudiante_altas], headers=["ID", "Asignatura", "Nota 1"]))

def consulta_45(user_id=None):
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891', user_id=user_id)
    notas_estudiante_ordenadas = Nota.objects.filter(estudiante=estudiante_especifico, user_id=user_id).order_by('periodo__nombre')
    print(f"\nConsulta 45: Notas de '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' ordenadas por periodo:")
    print(tabulate([(nota.periodo, nota.asignatura, nota.nota1, nota.nota2) for nota in notas_estudiante_ordenadas], headers=["Periodo", "Asignatura", "Nota 1", "Nota 2"]))

def consulta_46(user_id=None):
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891', user_id=user_id)
    total_notas_estudiante = Nota.objects.filter(estudiante=estudiante_especifico, user_id=user_id).count()
    print(f"\nConsulta 46: Total de notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}': {total_notas_estudiante}")

def consulta_47(user_id=None):
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891', user_id=user_id)
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    promedio_notas_estudiante_periodo = Nota.objects.filter(estudiante=estudiante_especifico, periodo=periodo_especifico, user_id=user_id).aggregate(Avg('nota1'))['nota1__avg']
    if promedio_notas_estudiante_periodo is not None:
        print(f"\nConsulta 47: Promedio de notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' en el periodo '{periodo_especifico}': {promedio_notas_estudiante_periodo}")
    else:
        print(f"El estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' no tiene notas en el periodo '{periodo_especifico}'.")

def consulta_48(user_id=None):
    notas_observacion_especifica = Nota.objects.filter(observacion='Reprobado', user_id=user_id)
    print("\nConsulta 48: Notas con observación 'Reprobado':")
    print(tabulate([(nota.id, nota.estudiante, nota.asignatura, nota.observacion) for nota in notas_observacion_especifica], headers=["ID", "Estudiante", "Asignatura", "Observación"]))

def consulta_49(user_id=None):
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891', user_id=user_id)
    notas_estudiante_ordenadas_asignatura = Nota.objects.filter(estudiante=estudiante_especifico, user_id=user_id).order_by('asignatura__nombre')
    print(f"\nConsulta 49: Notas de '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' ordenadas por asignatura:")
    print(tabulate([(nota.asignatura, nota.nota1, nota.nota2, nota.recuperacion) for nota in notas_estudiante_ordenadas_asignatura], headers=["Asignatura", "Nota 1", "Nota 2", "Recuperación"]))

# Sentencias Update: 50 - 54
def operacion_50(user_id=None):
    num_actualizadas = Nota.objects.filter(nota1__lt=20, user_id=user_id).update(nota1=20)
    print(f"\nOperación 50: Se actualizaron {num_actualizadas} notas con nota1 < 20 a 20")

def operacion_51(user_id=None):
    num_actualizadas = Nota.objects.filter(nota2__lt=15, user_id=user_id).update(nota2=15)
    print(f"\nOperación 51: Se actualizaron {num_actualizadas} notas con nota2 < 15 a 15")

def operacion_52(user_id=None):
    num_actualizadas = Nota.objects.filter(recuperacion__lt=10, user_id=user_id).update(recuperacion=10)
    print(f"\nOperación 52: Se actualizaron {num_actualizadas} notas con recuperación < 10 a 10")

def operacion_53(user_id=None):
    num_actualizadas = Nota.objects.filter(nota1__gte=10, nota2__gte=10, user_id=user_id).update(observacion='Aprobado')
    print(f"\nOperación 53: Se actualizaron {num_actualizadas} notas a 'Aprobado' por tener nota1 y nota2 >= 10")

def operacion_54(user_id=None):
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    num_actualizadas = Nota.objects.filter(periodo=periodo_especifico, user_id=user_id).update(nota1=F('nota1') + 1)
    print(f"\nOperación 54: Se incrementó nota1 en 1 para {num_actualizadas} notas del período '{periodo_especifico}'")

# Sentencias Delete: 55 - 59
def operacion_55(user_id=None):
    estudiante_id = int(input("Ingrese el ID del estudiante para eliminar sus notas: "))
    num_eliminadas = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).delete()
    print(f"\nOperación 55: Se eliminaron {num_eliminadas[0]} notas del estudiante con ID {estudiante_id}")

def operacion_56(user_id=None):
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    num_eliminadas = Nota.objects.filter(periodo=periodo_especifico, user_id=user_id).delete()
    print(f"\nOperación 56: Se eliminaron {num_eliminadas[0]} notas del período '{periodo_especifico}'")

def operacion_57(user_id=None):
    num_eliminadas = Nota.objects.filter(nota1__lt=10, user_id=user_id).delete()
    print(f"\nOperación 57: Se eliminaron {num_eliminadas[0]} notas con nota1 menor a 10")

def operacion_58(user_id=None):
    periodo_especifico = Periodo.objects.get(nombre='Periodo 1', user_id=user_id)
    num_actualizadas = Nota.objects.filter(periodo=periodo_especifico, user_id=user_id).update(state=False)
    print(f"\nOperación 58: Se eliminaron lógicamente {num_actualizadas} notas del período '{periodo_especifico}'")

def operacion_59(user_id=None):
    notas_con_nota1_menor_a_10 = Nota.objects.filter(nota1__lt=10, user_id=user_id)
    num_eliminadas = DetalleNota.objects.filter(nota__in=notas_con_nota1_menor_a_10).delete()
    print(f"\nOperación 59: Se eliminaron {num_eliminadas[0]} detalles de notas con nota1 menor a 10")

# Sentencias CRUD:
def consulta_60(user, user_id=None):
    try:
        with transaction.atomic():
            estudiante = Estudiante.objects.get(id=1, user_id=user_id)
            periodo = Periodo.objects.get(id=1, user_id=user_id)
            asignaturas = Asignatura.objects.filter(user_id=user_id).prefetch_related('profesores')

            # Crear la nota sin promedio
            nueva_nota = Nota.objects.create(
                periodo=periodo,
                estudiante=estudiante,
                user=user
            )

            detalles_notas = []
            suma_ponderada_nota1 = 0
            suma_ponderada_nota2 = 0
            total_porcentaje = 0

            # Crear y guardar los detalles de notas
            for asignatura in asignaturas:
                profesores = asignatura.profesores.all()
                if not profesores:
                    raise ValueError(f"No hay profesores asignados a la asignatura '{asignatura}'")
                profesor = random.choice(profesores)

                detalle = DetalleNota(
                    nota=nueva_nota,
                    asignatura=asignatura,
                    profesor=profesor,
                    porcentaje=random.randint(10, 50),
                    user=user,
                    nota1=round(random.uniform(0, 20), 2),
                    nota2=round(random.uniform(0, 20), 2),
                    recuperacion=round(random.uniform(0, 20), 2) if random.random() < 0.3 else None
                )
                detalle.save()
                detalles_notas.append(detalle)

                suma_ponderada_nota1 += detalle.nota1 * detalle.porcentaje
                suma_ponderada_nota2 += detalle.nota2 * detalle.porcentaje
                total_porcentaje += detalle.porcentaje

            # Calcular y guardar el promedio (DESPUÉS de crear y guardar los detalles)
            if total_porcentaje > 0:
                nueva_nota.promedio = (suma_ponderada_nota1 + suma_ponderada_nota2) / (2 * total_porcentaje)
                # Opcional: Actualizar el estado de la nota en función de si aprobó o no
                nueva_nota.estado = "Aprobado" if nueva_nota.promedio >= 10 else "Reprobado"
            else:
                nueva_nota.promedio = None  # Si no hay detalles, el promedio será nulo
                # Opcional: Si no hay notas, puedes asignar un estado como "Sin Calificar"
                nueva_nota.estado = "Sin Calificar"
            nueva_nota.save()

            # Imprimir resultados
            print("\nConsulta 60: Registro de notas creado exitosamente.")
            print(f"  - Estudiante: {estudiante.nombre} {estudiante.apellido}")
            print(f"  - Periodo: {periodo.nombre}")
            print("  - Notas:")
            for detalle in detalles_notas:
                print(
                    f"    - Asignatura: {detalle.asignatura}, Nota 1: {detalle.nota1}, Nota 2: {detalle.nota2}, Recuperación: {detalle.recuperacion if detalle.recuperacion else 'No aplica'}"
                )

    except ObjectDoesNotExist:
        print("Error: No se pudo encontrar el estudiante, periodo, asignatura o profesor.")


# Ejecutar inserciones y consultas
if __name__ == '__main__':
    create_user()  # Crear usuario solo si no existe
    user = User.objects.get(username='Frank_')  # Obtener el usuario creado
    insertar_periodos(user)
    insertar_asignaturas(user)
    insertar_profesores(user)
    insertar_estudiantes(user)
    insertar_notas(user, Estudiante.objects.all(), Periodo.objects.all(), Asignatura.objects.all(), Profesor.objects.all())

    # Llamadas a las consultas y operaciones

    # Consultas Básicas: 1 - 6
    consulta_1(user.id)
    consulta_2(user.id)
    consulta_3(user.id)
    consulta_4(user.id)
    consulta_5(user.id)
    consulta_6(user.id)
    # Consultas con Condiciones Lógicas 7 - 11
    consulta_7(user.id)
    consulta_8(user.id)
    consulta_9(user.id)
    consulta_10(user.id)
    consulta_11(user.id)
    # Consultas con Funciones Numéricas: 12 - 14
    consulta_12(user.id)
    consulta_13(user.id)
    consulta_14(user.id)
    # Consultas con Funciones de Fecha: 15 - 19
    consulta_15(user.id)
    consulta_16(user.id)
    consulta_17(user.id)
    consulta_18(user.id)
    consulta_19(user.id)
    # Consultas Combinadas con Funciones Avanzadas: 20 - 24
    consulta_20(user.id)
    consulta_21(user.id)
    consulta_22(user.id)
    consulta_23(user.id)
    consulta_24(user.id)
    # Consultas con Subconsultas y Anotaciones: 25 - 39
    consulta_25(user.id)
    consulta_26(user.id)
    consulta_27(user.id)
    consulta_28(user.id)
    consulta_29(user.id)
    consulta_30(user.id)
    consulta_31(user.id)
    consulta_32(user.id)
    consulta_33(user.id)
    consulta_34(user.id)
    consulta_35(user.id)
    consulta_36(user.id)
    consulta_37(user.id)
    consulta_38(user.id)
    consulta_39(user.id)
    # Consultas con Relaciones Inversas: 40 - 49
    consulta_40(user.id)
    consulta_41(user.id)
    consulta_42(user.id)
    consulta_43(user.id)
    consulta_44(user.id)
    consulta_45(user.id)
    consulta_46(user.id)
    consulta_47(user.id)
    consulta_48(user.id)
    consulta_49(user.id)
    # Sentencias Update: 50 - 54
    operacion_50(user.id)
    operacion_51(user.id)
    operacion_52(user.id)
    operacion_53(user.id)
    operacion_54(user.id)
    # Sentencias Delete: 55 - 59
    operacion_55(user.id)
    operacion_56(user.id)
    operacion_57(user.id)
    operacion_58(user.id)
    operacion_59(user.id)
    # Sentencias CRUD
    consulta_60(user, user.id)  # Llama a la consulta 60 con el objeto user

