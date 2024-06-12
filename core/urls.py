from django.urls import path
from .views import (
    ListaEstudiantesView, ListaProfesoresView, ListaAsignaturasView,
    ListaPeriodosView, ListaNotasView,
    CrearEstudianteView, EditarEstudianteView, EliminarEstudianteView,
    CrearProfesorView, EditarProfesorView, EliminarProfesorView,
    CrearAsignaturaView, EditarAsignaturaView, EliminarAsignaturaView,
    CrearPeriodoView, EditarPeriodoView, EliminarPeriodoView,
    CrearNotaView, EditarNotaView, EliminarNotaView,
)

app_name = 'core'

urlpatterns = [
    # URLs para listado
    path('estudiantes/', ListaEstudiantesView.as_view(), name='lista_estudiantes'),
    path('profesores/', ListaProfesoresView.as_view(), name='lista_profesores'),
    path('asignaturas/', ListaAsignaturasView.as_view(), name='lista_asignaturas'),
    path('periodos/', ListaPeriodosView.as_view(), name='lista_periodos'),
    path('notas/', ListaNotasView.as_view(), name='lista_notas'),

    # URLs para Estudiantes (CRUD)
    path('estudiantes/crear/', CrearEstudianteView.as_view(), name='crear_estudiante'),
    path('estudiantes/<int:pk>/editar/', EditarEstudianteView.as_view(), name='editar_estudiante'),
    path('estudiantes/<int:pk>/eliminar/', EliminarEstudianteView.as_view(), name='eliminar_estudiante'),

    # URLs para Profesores (CRUD)
    path('profesores/crear/', CrearProfesorView.as_view(), name='crear_profesor'),
    path('profesores/<int:pk>/editar/', EditarProfesorView.as_view(), name='editar_profesor'),
    path('profesores/<int:pk>/eliminar/', EliminarProfesorView.as_view(), name='eliminar_profesor'),

    # URLs para Asignaturas (CRUD)
    path('asignaturas/crear/', CrearAsignaturaView.as_view(), name='crear_asignatura'),
    path('asignaturas/<int:pk>/editar/', EditarAsignaturaView.as_view(), name='editar_asignatura'),
    path('asignaturas/<int:pk>/eliminar/', EliminarAsignaturaView.as_view(), name='eliminar_asignatura'),

    # URLs para Periodos (CRUD)
    path('periodos/crear/', CrearPeriodoView.as_view(), name='crear_periodo'),
    path('periodos/<int:pk>/editar/', EditarPeriodoView.as_view(), name='editar_periodo'),
    path('periodos/<int:pk>/eliminar/', EliminarPeriodoView.as_view(), name='eliminar_periodo'),

    # URLs para Notas (CRUD)
    path('notas/crear/', CrearNotaView.as_view(), name='crear_nota'),
    path('notas/<int:pk>/editar/', EditarNotaView.as_view(), name='editar_nota'),
    path('notas/<int:pk>/eliminar/', EliminarNotaView.as_view(), name='eliminar_nota'),
]
