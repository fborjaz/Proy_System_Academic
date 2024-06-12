from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Estudiante, Profesor, Asignatura, Periodo, Nota
from .forms import (
    EstudianteForm,
    ProfesorForm,
    AsignaturaForm,
    PeriodoForm,
    NotaForm
)


# Vista para la página de inicio
def index(request):
    return render(request, 'index.html')


# Vistas para Estudiantes
class ListaEstudiantesView(ListView):
    model = Estudiante
    template_name = 'core/Estudiantes/lista_estudiantes.html'


class CrearEstudianteView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'core/Estudiantes/crear_estudiante.html'
    success_url = reverse_lazy('core:lista_estudiantes')


class EditarEstudianteView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'core/Estudiantes/editar_estudiante.html'
    success_url = reverse_lazy('core:lista_estudiantes')


class EliminarEstudianteView(DeleteView):
    model = Estudiante
    template_name = 'core/Estudiantes/eliminar_estudiante.html'
    success_url = reverse_lazy('core:lista_estudiantes')


# Vistas para Profesores
class ListaProfesoresView(ListView):
    model = Profesor
    template_name = 'core/Profesores/lista_profesores.html'


class CrearProfesorView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'core/Profesores/crear_profesor.html'
    success_url = reverse_lazy('core:lista_profesores')


class EditarProfesorView(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'core/Profesores/editar_profesor.html'
    success_url = reverse_lazy('core:lista_profesores')


class EliminarProfesorView(DeleteView):
    model = Profesor
    template_name = 'core/Profesores/eliminar_profesor.html'
    success_url = reverse_lazy('core:lista_profesores')


# Vistas para Asignaturas
class ListaAsignaturasView(ListView):
    model = Asignatura
    template_name = 'core/Asignaturas/lista_asignaturas.html'


class CrearAsignaturaView(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'core/Asignaturas/crear_asignatura.html'
    success_url = reverse_lazy('core:lista_asignaturas')


class EditarAsignaturaView(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'core/Asignaturas/editar_asignatura.html'
    success_url = reverse_lazy('core:lista_asignaturas')


class EliminarAsignaturaView(DeleteView):
    model = Asignatura
    template_name = 'core/Asignaturas/eliminar_asignatura.html'
    success_url = reverse_lazy('core:lista_asignaturas')


# Vistas para Periodos
class ListaPeriodosView(ListView):
    model = Periodo
    template_name = 'core/Periodos/lista_periodos.html'


class CrearPeriodoView(CreateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = 'core/Periodos/crear_periodo.html'
    success_url = reverse_lazy('core:lista_periodos')


class EditarPeriodoView(UpdateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = 'core/Periodos/editar_periodo.html'
    success_url = reverse_lazy('core:lista_periodos')


class EliminarPeriodoView(DeleteView):
    model = Periodo
    template_name = 'core/Periodos/eliminar_periodo.html'
    success_url = reverse_lazy('core:lista_periodos')


# Vistas para Notas
class ListaNotasView(ListView):
    model = Nota
    template_name = 'core/Notas/lista_notas.html'


class CrearNotaView(CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'core/Notas/crear_nota.html'
    success_url = reverse_lazy('core:lista_notas')


class EditarNotaView(UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'core/Notas/editar_nota.html'
    success_url = reverse_lazy('core:lista_notas')


class EliminarNotaView(DeleteView):
    model = Nota
    template_name = 'core/Notas/eliminar_nota.html'
    success_url = reverse_lazy('core:lista_notas')
