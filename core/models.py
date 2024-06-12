from django.db import models

class Periodo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    año = models.IntegerField()  # Año del periodo académico
    activo = models.BooleanField(default=True)  # Indica si el periodo está activo
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    pre_requisitos = models.ManyToManyField('self', blank=True)  # Relación consigo misma para prerrequisitos
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    titulo = models.CharField(max_length=50)  # Título académico (Lic., Mg., Dr., etc.)
    especialidad = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()

class Estudiante(models.Model):  # Definición del modelo Estudiante
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    # Campos adicionales del caso de estudio:
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()

class Nota(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey('core.Estudiante', on_delete=models.CASCADE)  # Usa el nombre completo del modelo
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    recuperacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)  # Promedio (calculado)
    estado = models.CharField(max_length=20)  # Estado (Aprobado, Reprobado, etc.)
    observacion = models.TextField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"Nota de {self.estudiante} en {self.asignatura} - {self.periodo}"

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()

class DetalleNota(models.Model):
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)  # Descripción del detalle (Examen, Tarea, etc.)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje que representa en la nota final
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"Detalle de {self.nota}: {self.descripcion}"

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
