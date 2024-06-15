import os
import django
import random
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.db.models import Q, Avg, Count, F, Value, CharField
from django.http import Http404
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.shortcuts import get_object_or_404

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_academy.settings')
django.setup()

from django.contrib.auth.models import User

def create_user(create=False):
    if create:
        User.objects.create_user(username='poo', password='1234', email='')

def insertar_periodos(user):
    periodos = [
        Periodo(user=user, nombre='Periodo 1', fecha_inicio=date(2023, 1, 1), fecha_fin=date(2023, 6, 30), año=2023),
        Periodo(user=user, nombre='Periodo 2', fecha_inicio=date(2023, 7, 1), fecha_fin=date(2023, 12, 31), año=2023),
        Periodo(user=user, nombre= 'Periodo 3', fecha_inicio=date(2024, 1, 1), fecha_fin=date(2024, 6, 30), año=2024),
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
        Profesor(user=user, nombre='Juan', apellido='Pérez', cedula='1234567890', titulo='Ing.', especialidad='Software'),
        Profesor(user=user, nombre='María', apellido='González', cedula='0987654321', titulo='Dra.', especialidad='Matemáticas'),
        Profesor(user=user, nombre='Ana', apellido='Martínez', cedula='1234509876', titulo='Lic.', especialidad='Física'),
        Profesor(user=user, nombre='Luis', apellido='Ramírez', cedula='5432167890', titulo='Mg.', especialidad='Historia'),
        Profesor(user=user, nombre='Carlos', apellido='Sánchez', cedula='0987654321', titulo='Dr.', especialidad='Biología'),
        Profesor(user=user, nombre='Laura', apellido='Gómez', cedula='6789054321', titulo='Ing.', especialidad='Química'),
        Profesor(user=user, nombre='Pedro', apellido='Castro', cedula='5432109876', titulo='Lic.', especialidad='Geografía'),
        Profesor(user=user, nombre='Lucía', apellido='Herrera', cedula='0987654321', titulo='Mg.', especialidad='Arte'),
        Profesor(user=user, nombre='Miguel', apellido='Ruiz', cedula='1234567890', titulo='Dr.', especialidad='Música'),
        Profesor(user=user, nombre='Sofía', apellido='López', cedula='5678901234', titulo='Ing.', especialidad='Literatura'),
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
            estudiante = random.choice(estudiantes)  # Elegimos un estudiante aleatorio

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

# Consultas (según el caso de estudio)
def consultas_orm(user_id=None):
    # Consulta 1: Estudiantes cuyo nombre empieza con 'Est'
    estudiantes_est = Estudiante.objects.filter(nombre__startswith='Est', user_id=user_id)
    print("Estudiantes cuyo nombre empieza con 'Est':", estudiantes_est)

    # Consulta 2: Profesores cuyo nombre contiene 'or'
    profesores_or = Profesor.objects.filter(nombre__icontains='or', user_id=user_id)
    print("Profesores cuyo nombre contiene 'or':", profesores_or)

    # Consulta 3: Asignaturas cuya descripción termina en 'a'
    asignaturas_a = Asignatura.objects.filter(descripcion__endswith='a', user_id=user_id)
    print("Asignaturas cuya descripción termina en 'a':", asignaturas_a)

    # Consulta 4: Notas con nota1 mayor que 8.0
    notas_mayores_8 = Nota.objects.filter(nota1__gt=8.0, user_id=user_id)
    print("Notas con nota1 mayor que 8.0:", notas_mayores_8)

    # Consulta 5: Notas con nota2 menor que 9.0
    notas_menores_9 = Nota.objects.filter(nota2__lt=9.0, user_id=user_id)
    print("Notas con nota2 menor que 9.0:", notas_menores_9)

    # Consulta 6: Notas con recuperación igual a 9.5
    notas_recuperacion_9_5 = Nota.objects.filter(recuperacion=9.5, user_id=user_id)
    print("Notas con recuperación igual a 9.5:", notas_recuperacion_9_5)

    # Consulta 7: Estudiantes cuyo nombre empieza con 'Est' y su cédula termina en '1'
    estudiantes_est_cedula_1 = Estudiante.objects.filter(nombre__startswith='Est', cedula__endswith='1', user_id=user_id)
    print("Estudiantes cuyo nombre empieza con 'Est' y su cédula termina en '1':", estudiantes_est_cedula_1)

    # Consulta 8: Asignaturas cuya descripción contiene 'Curso' o termina en 'a'
    asignaturas_curso_o_a = Asignatura.objects.filter(
        Q(descripcion__icontains='Curso') | Q(descripcion__endswith='a'), user_id=user_id
    )
    print("Asignaturas cuya descripción contiene 'Curso' o termina en 'a':", asignaturas_curso_o_a)

    # Consulta 9: Profesores cuyo nombre no contiene 'or'
    profesores_no_or = Profesor.objects.filter(~Q(nombre__icontains='or'), user_id=user_id)
    print("Profesores cuyo nombre no contiene 'or':", profesores_no_or)

    # Consulta 10: Notas con nota1 mayor que 7.0 y nota2 menor que 8.0
    notas_7_8 = Nota.objects.filter(nota1__gt=7.0, nota2__lt=8.0, user_id=user_id)
    print("Notas con nota1 mayor que 7.0 y nota2 menor que 8.0:", notas_7_8)

    # Consulta 11: Notas con recuperación igual a None o nota2 mayor que 9.0
    notas_recuperacion_none_o_nota2_mayor_9 = Nota.objects.filter(Q(recuperacion__isnull=True) | Q(nota2__gt=9.0),
                                                                  user_id=user_id)
    print("Notas con recuperación igual a None o nota2 mayor que 9.0:", notas_recuperacion_none_o_nota2_mayor_9)

    # Consulta 12: Notas con nota1 entre 7.0 y 9.0
    notas_nota1_entre_7_y_9 = Nota.objects.filter(nota1__range=(7.0, 9.0), user_id=user_id)
    print("Notas con nota1 entre 7.0 y 9.0:", notas_nota1_entre_7_y_9)

    # Consulta 13: Notas con nota2 fuera del rango 6.0 a 8.0
    notas_nota2_fuera_de_rango_6_8 = Nota.objects.exclude(nota2__range=(6.0, 8.0), user_id=user_id)
    print("Notas con nota2 fuera del rango 6.0 a 8.0:", notas_nota2_fuera_de_rango_6_8)

    # Consulta 14: Notas cuya recuperación no sea None
    notas_recuperacion_no_null = Nota.objects.filter(recuperacion__isnull=False, user_id=user_id)
    print("Notas cuya recuperación no sea None:", notas_recuperacion_no_null)

    # Consulta 15: Notas creadas en el último año
    hace_un_anio = timezone.now() - timedelta(days=365)
    notas_ultimo_anio = Nota.objects.filter(created__gte=hace_un_anio, user_id=user_id)
    print("Notas creadas en el último año:", notas_ultimo_anio)

    # Consulta 16: Notas creadas en el último mes
    hace_un_mes = timezone.now() - timedelta(days=30)
    notas_ultimo_mes = Nota.objects.filter(created__gte=hace_un_mes, user_id=user_id)
    print("Notas creadas en el último mes:", notas_ultimo_mes)

    # Consulta 17: Notas creadas en el último día
    hace_un_dia = timezone.now() - timedelta(days=1)
    notas_ultimo_dia = Nota.objects.filter(created__gte=hace_un_dia, user_id=user_id)
    print("Notas creadas en el último día:", notas_ultimo_dia)

    # Consulta 18: Notas creadas antes del año 2023
    notas_antes_2023 = Nota.objects.filter(created__year__lt=2023, user_id=user_id)
    print("Notas creadas antes del año 2023:", notas_antes_2023)

    # Consulta 19: Notas creadas en marzo de cualquier año
    notas_marzo = Nota.objects.filter(created__month=3, user_id=user_id)
    print("Notas creadas en marzo de cualquier año:", notas_marzo)

    # Consulta 20: Estudiantes cuyo nombre tiene exactamente 10 caracteres (corregida)
    from django.db.models.functions import Length
    estudiantes_10_caracteres = Estudiante.objects.annotate(nombre_length=Length('nombre')).filter(
        nombre_length__exact=10, user_id=user_id)
    print("Estudiantes cuyo nombre tiene exactamente 10 caracteres:", estudiantes_10_caracteres)

    # Consulta 21: Notas con nota1 y nota2 mayores a 7.5
    notas_mayores_7_5 = Nota.objects.filter(nota1__gt=7.5, nota2__gt=7.5, user_id=user_id)
    print("Notas con nota1 y nota2 mayores a 7.5:", notas_mayores_7_5)

    # Consulta 22: Notas con recuperación no nula y nota1 mayor a nota2
    notas_recuperacion_y_nota1_mayor_nota2 = Nota.objects.filter(recuperacion__isnull=False, nota1__gt=F('nota2'),
                                                                 user_id=user_id)
    print("Notas con recuperación no nula y nota1 mayor a nota2:", notas_recuperacion_y_nota1_mayor_nota2)

    # Consulta 23: Notas con nota1 mayor a 8.0 o nota2 igual a 7.5
    notas_nota1_mayor_8_o_nota2_igual_7_5 = Nota.objects.filter(Q(nota1__gt=8.0) | Q(nota2=7.5), user_id=user_id)
    print("Notas con nota1 mayor a 8.0 o nota2 igual a 7.5:", notas_nota1_mayor_8_o_nota2_igual_7_5)

    # Consulta 24: Notas con recuperación mayor a nota1 y nota2 (corregida)
    notas_recuperacion_mayor_nota1_y_nota2 = Nota.objects.filter(
        Q(recuperacion__gt=F('nota1')) & Q(recuperacion__gt=F('nota2')), user_id=user_id
    )
    print("Notas con recuperación mayor a nota1 y nota2:", notas_recuperacion_mayor_nota1_y_nota2)

    # Consulta 25: Estudiantes con al menos una nota de recuperación
    estudiantes_con_recuperacion = Estudiante.objects.filter(nota__recuperacion__isnull=False,
                                                             user_id=user_id).distinct()
    print("Estudiantes con al menos una nota de recuperación:", estudiantes_con_recuperacion)

    # Consulta 26: Profesores que han dado una asignatura específica (por ejemplo, 'Matemáticas')
    try:
        asignatura_especifica = Asignatura.objects.get(descripcion='Matemáticas', user_id=user_id)
        profesores_asignatura_especifica = Profesor.objects.filter(nota__asignatura=asignatura_especifica,
                                                                   user_id=user_id).distinct()
        print("Profesores que han dado 'Matemáticas':", profesores_asignatura_especifica)
    except Asignatura.DoesNotExist:
        print(f"Error: No se pudo encontrar la asignatura 'Matemáticas' para el usuario {user_id}.")

    # Consulta 27: Asignaturas que tienen al menos una nota registrada
    asignaturas_con_notas = Asignatura.objects.filter(nota__isnull=False, user_id=user_id).distinct()
    print("Asignaturas que tienen al menos una nota registrada:", asignaturas_con_notas)

    # Consulta 28: Asignaturas que no tienen notas registradas
    asignaturas_sin_notas = Asignatura.objects.filter(nota__isnull=True, user_id=user_id)
    print("Asignaturas que no tienen notas registradas:", asignaturas_sin_notas)

    # Consulta 29: Estudiantes que no tienen notas de recuperación
    estudiantes_sin_recuperacion = Estudiante.objects.filter(nota__recuperacion__isnull=True,
                                                             user_id=user_id).distinct()
    print("Estudiantes que no tienen notas de recuperación:", estudiantes_sin_recuperacion)

    # Consulta 30: Promedio de nota1 y nota2 de cada nota (corregida)
    from django.db.models import FloatField
    from django.db.models.functions import Cast
    promedio_notas = Nota.objects.filter(user_id=user_id).annotate(
        promedio_notas=Cast(F('nota1') + F('nota2'), FloatField()) / 2
    )
    print("Promedio de nota1 y nota2 de cada nota:")
    for nota in promedio_notas:
        print(f"- {nota}: {nota.promedio_notas}")

        # Consulta 31: Notas con nota1 menor que 6.0 y nota2 mayor que 7.0
    notas_nota1_menor_6_nota2_mayor_7 = Nota.objects.filter(nota1__lt=6.0, nota2__gt=7.0, user_id=user_id)
    print("Notas con nota1 menor que 6.0 y nota2 mayor que 7.0:", notas_nota1_menor_6_nota2_mayor_7)

    # Consulta 32: Notas con nota1 en la lista [7.0, 8.0, 9.0]
    notas_nota1_en_lista = Nota.objects.filter(nota1__in=[7.0, 8.0, 9.0], user_id=user_id)
    print("Notas con nota1 en la lista [7.0, 8.0, 9.0]:", notas_nota1_en_lista)

    # Consulta 33: Notas cuyo id está en un rango del 1 al 5
    notas_rango_id = Nota.objects.filter(id__range=(1, 5), user_id=user_id)
    print("Notas cuyo id está en un rango del 1 al 5:", notas_rango_id)

    # Consulta 34: Notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]
    notas_recuperacion_no_en_lista = Nota.objects.exclude(recuperacion__in=[8.0, 9.0, 10.0], user_id=user_id)
    print("Notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:", notas_recuperacion_no_en_lista)

    # Consulta 35: Suma de todas las notas de un estudiante (corregida)
    while True:
        try:
            estudiante_id = int(input("Ingrese el ID del estudiante para consultar sus notas: "))
            suma_notas_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(suma_notas=Sum('nota1'))['suma_notas']
            if suma_notas_estudiante is not None:
                print(f"Suma de todas las notas del estudiante con ID {estudiante_id}: {suma_notas_estudiante}")
            else:
                print(f"El estudiante con ID {estudiante_id} no tiene notas registradas.")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
        except Estudiante.DoesNotExist:
            print(f"Error: No se encontró ningún estudiante con el ID {estudiante_id}.")

    # Consulta 36: Nota máxima obtenida por un estudiante
    nota_maxima_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(Max('nota1'))[
        'nota1__max']
    print(f"Nota máxima obtenida por el estudiante con ID {estudiante_id}: {nota_maxima_estudiante}")

    # Consulta 37: Nota mínima obtenida por un estudiante
    nota_minima_estudiante = Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).aggregate(Min('nota1'))[
        'nota1__min']
    print(f"Nota mínima obtenida por el estudiante con ID {estudiante_id}: {nota_minima_estudiante}")

    # Consulta 30: Promedio de nota1 y nota2 de cada nota (corregida)
    from django.db.models import FloatField
    from django.db.models.functions import Cast
    promedio_notas = Nota.objects.filter(user_id=user_id).annotate(
        promedio=Cast(F('nota1') + F('nota2'), FloatField()) / 2
    )
    print("Promedio de nota1 y nota2 de cada nota:")
    for nota in promedio_notas:
        print(f"- {nota}: {nota.promedio}")

    # Consulta 39: Promedio de todas las notas de un estudiante sin incluir recuperación
    promedio_sin_recuperacion = \
    Nota.objects.filter(estudiante_id=estudiante_id, user_id=user_id).exclude(recuperacion__isnull=False).aggregate(
        Avg('nota1'))['nota1__avg']
    print(f"Promedio de notas del estudiante con ID {estudiante_id} (sin recuperación): {promedio_sin_recuperacion}")

    # Consulta 40: Obtener todas las notas de un estudiante con el detalle de todos sus datos relacionados
    notas_estudiante_detalle = Nota.objects.filter(estudiante=estudiante_id).prefetch_related('detallenota_set')
    print(f"Notas del estudiante con ID {estudiante_id} y sus detalles:")
    for nota in notas_estudiante_detalle:
        print(f"- {nota}:")
        for detalle in nota.detallenota_set.all():
            print(f"  - {detalle}")

    # Consulta 41: Obtener todas las notas de un período específico
    periodo_especifico = Periodo.objects.get(
        nombre='Periodo 1')  # Reemplazar con el nombre del período que deseas consultar
    notas_periodo_especifico = Nota.objects.filter(periodo=periodo_especifico, user_id=user_id)
    print(f"Notas del período '{periodo_especifico}':", notas_periodo_especifico)

    # Consulta 42: Consultar todas las notas de una asignatura dada en un período
    asignatura_especifica = Asignatura.objects.get(nombre='Matemáticas', user_id=user_id)
    notas_asignatura_periodo = Nota.objects.filter(asignatura=asignatura_especifica, periodo=periodo_especifico,
                                                   user_id=user_id)
    print(f"Notas de '{asignatura_especifica}' en el periodo '{periodo_especifico}':", notas_asignatura_periodo)

    # Consulta 43: Obtener todas las notas de un profesor en particular
    profesor_especifico = Profesor.objects.get(cedula='0927454326',
                                               user_id=user_id)  # Reemplazar con la cédula del profesor que deseas consultar
    notas_profesor = Nota.objects.filter(profesor=profesor_especifico, user_id=user_id)
    print(f"Notas del profesor '{profesor_especifico.nombre} {profesor_especifico.apellido}':", notas_profesor)

    # Consulta 44: Consultar todas las notas de un estudiante con notas superiores a un valor dado
    estudiante_especifico = Estudiante.objects.get(cedula='1234567891',
                                                   user_id=user_id)  # Reemplazar con la cédula del estudiante que deseas consultar
    notas_estudiante_altas = Nota.objects.filter(estudiante=estudiante_especifico, nota1__gt=15.0, user_id=user_id)
    print(f"Notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' superiores a 15.0:")
    for nota in notas_estudiante_altas:
        print(f"- {nota}: {nota.nota1}")

    # Consulta 45: Obtener todas las notas de un estudiante ordenadas por período
    notas_estudiante_ordenadas = Nota.objects.filter(estudiante=estudiante_especifico, user_id=user_id).order_by(
        'periodo__nombre')
    print(
        f"Notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' ordenadas por periodo:")
    for nota in notas_estudiante_ordenadas:
        print(f"- {nota.periodo}: {nota}")

    # Consulta 46: Consultar la cantidad total de notas para un estudiante
    total_notas_estudiante = Nota.objects.filter(estudiante=estudiante_especifico, user_id=user_id).count()
    print(
        f"Total de notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}': {total_notas_estudiante}")

    # Consulta 47: Calcular el promedio de las notas de un estudiante en un período dado
    promedio_notas_estudiante_periodo = Nota.objects.filter(
        estudiante=estudiante_especifico, periodo=periodo_especifico, user_id=user_id
    ).aggregate(Avg('nota1'))['nota1__avg']
    if promedio_notas_estudiante_periodo is not None:
        print(
            f"Promedio de notas del estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' en el periodo '{periodo_especifico}': {promedio_notas_estudiante_periodo}"
        )
    else:
        print(
            f"El estudiante '{estudiante_especifico.nombre} {estudiante_especifico.apellido}' no tiene notas en el periodo '{periodo_especifico}'."
        )

    # Consulta 48: Consultar todas las notas con una observación específica (por ejemplo, 'Reprobado')
    notas_observacion_especifica = Nota.objects.filter(observacion='Reprobado', user_id=user_id)
    print("Notas con observación 'Reprobado':", notas_observacion_especifica)

    # Consulta 49: Obtener todas las notas de un estudiante ordenadas por asignatura
    notas_estudiante_ordenadas_asignatura = DetalleNota.objects.filter(estudiante_id=estudiante_id).order_by('nota__asignatura__descripcion').select_related('nota', 'nota__asignatura')
    print(f"Notas del estudiante con ID {estudiante_id} ordenadas por asignatura:")
    for detalle_nota in notas_estudiante_ordenadas_asignatura:
        print(f"- {detalle_nota.nota.asignatura}: {detalle_nota.nota} - Nota 1: {detalle_nota.nota1}")

    # Operación 50: Actualizar nota1 para alumnos con nota1 < 20
    Nota.objects.filter(nota1__lt=20).update(nota1=20)

    # Operación 51: Actualizar nota2 para alumnos con nota2 < 15
    Nota.objects.filter(nota2__lt=15).update(nota2=15)

    # Operación 52: Actualizar recuperación para alumnos con recuperación < 10
    Nota.objects.filter(recuperacion__lt=10).update(recuperacion=10)

    # Operación 53: Actualizar observación para alumnos que hayan aprobado
    Nota.objects.filter(nota1__gte=10, nota2__gte=10).update(observacion='Aprobado')

    # Operación 54: Actualizar todas las notas en un período específico
    notas_periodo_especifico = Nota.objects.filter(periodo=periodo_especifico)
    for nota in notas_periodo_especifico:
        nota.nota1 += 1
        nota.save()

    # Operación 55: Eliminar físicamente todas las notas de un estudiante
    DetalleNota.objects.filter(estudiante_id=estudiante_id).hard_delete()

    # Operación 56: Eliminar lógicamente todas las notas de un estudiante
    DetalleNota.objects.filter(estudiante_id=estudiante_id).delete()

    # Operación 57: Eliminar físicamente todas las notas de un período específico
    DetalleNota.objects.filter(nota__periodo=periodo_especifico).hard_delete()

    # Operación 58: Eliminar lógicamente todas las notas de un período específico
    DetalleNota.objects.filter(nota__periodo=periodo_especifico).delete()

    # Operación 59: Eliminar físicamente todos los detalles de notas que tengan una nota1 menor a 10
    notas_con_nota1_menor_a_10 = Nota.objects.filter(nota1__lt=10)
    DetalleNota.objects.filter(nota__in=notas_con_nota1_menor_a_10).delete()

    # Consulta 60: Crear un registro de notas de un estudiante (similar a la creación de una factura)
    try:
        estudiante = Estudiante.objects.get(id=1, user_id=user_id)
        periodo = Periodo.objects.get(id=1, user_id=user_id)
        asignaturas = Asignatura.objects.filter(user_id=user_id)
        profesores = Profesor.objects.filter(user_id=user_id)

        nueva_nota = Nota.objects.create(
            periodo=periodo,
            estudiante=estudiante,
            user=user
        )

        detalles_notas = []
        for asignatura in asignaturas:
            profesor = random.choice(profesores)
            detalle = DetalleNota(
                nota=nueva_nota,
                asignatura=asignatura,
                profesor=profesor,
                porcentaje=random.randint(10, 50),
                user=user,
                nota1=round(random.uniform(0, 20), 2),  # Asignar nota1 aleatoria
                nota2=round(random.uniform(0, 20), 2),  # Asignar nota2 aleatoria
                recuperacion=round(random.uniform(0, 20), 2) if random.random() < 0.3 else None
                # Asignar recuperación aleatoria
            )
            detalles_notas.append(detalle)

        DetalleNota.objects.bulk_create(detalles_notas)
        print("Registro de notas creado exitosamente.")
    except ObjectDoesNotExist:
        print("Error: No se pudo encontrar el estudiante, periodo, asignatura o profesor.")


# Ejecutar inserciones y consultas
if __name__ == '__main__':
    create_user(create=True)  # Crear usuario solo si no existe
    user = User.objects.get(username='poo')  # Obtener el usuario creado
    insertar_periodos(user)
    insertar_asignaturas(user)
    insertar_profesores(user)
    insertar_estudiantes(user)
    insertar_notas(user, Estudiante.objects.all(), Periodo.objects.all(), Asignatura.objects.all(),
                   Profesor.objects.all())
    consultas_orm()

