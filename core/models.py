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

    def clean(self):
        # Validar que la fecha de inicio sea anterior a la fecha de fin
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")

        # Validar que el año coincida con las fechas
        if self.fecha_inicio.year != self.año or self.fecha_fin.year != self.año:
            raise ValidationError("El año debe coincidir con el año de las fechas de inicio y fin.")

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
    cedula = models.CharField(max_length=15, unique=False)
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
    cedula = models.CharField(max_length=15, unique=False)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

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
    estudiante = models.ForeignKey('core.Estudiante', on_delete=models.CASCADE)
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

    def clean(self):
        # Validar que las notas estén dentro del rango 0-20
        if self.nota1 < 0 or self.nota1 > 20:
            raise ValidationError("La nota1 debe estar entre 0 y 20.")
        if self.nota2 < 0 or self.nota2 > 20:
            raise ValidationError("La nota2 debe estar entre 0 y 20.")
        if self.recuperacion and (self.recuperacion < 0 or self.recuperacion > 20):
            raise ValidationError("La recuperación debe estar entre 0 y 20.")

        # Validar que el estado sea 'Aprobado' o 'Reprobado'
        estados_validos = ['Aprobado', 'Reprobado']
        if self.estado not in estados_validos:
            raise ValidationError(f"El estado debe ser uno de los siguientes: {', '.join(estados_validos)}")

    def save(self, *args, **kwargs):
        if self.nota1 and self.nota2:
            self.promedio = (self.nota1 + self.nota2) / 2
        else:
            self.promedio = None
        super().save(*args, **kwargs)

class DetalleNota(models.Model):
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Corregido: un solo campo 'user'
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"Detalle de {self.nota}: {self.descripcion}"

    def delete(self, *args, **kwargs):
        self.state = False
        self.save()
