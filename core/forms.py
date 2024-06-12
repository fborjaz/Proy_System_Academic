from django import forms
from .models import Estudiante, Profesor, Asignatura, Periodo, Nota

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'email']
        # Puedes personalizar los widgets o agregar validaciones adicionales aquí

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'cedula', 'titulo', 'especialidad']
        # Puedes personalizar los widgets o agregar validaciones adicionales aquí

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'descripcion', 'creditos', 'pre_requisitos']
        # Puedes personalizar los widgets o agregar validaciones adicionales aquí

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'año', 'activo']
        # Puedes personalizar los widgets o agregar validaciones adicionales aquí

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['periodo', 'asignatura', 'profesor', 'estudiante', 'nota1', 'nota2', 'recuperacion', 'observacion']
        # Puedes personalizar los widgets o agregar validaciones adicionales aquí
