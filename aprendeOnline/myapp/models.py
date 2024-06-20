from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Modelo de la tabla curso
class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.titulo

# Modelo de la tabla inscripción
class Inscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'curso')

    def __str__(self):
        return f"{self.user.username} inscrito en {self.curso.titulo}"

# Modelo para materiales del curso
class Material(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materiales')
    titulo = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='materiales/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Modelo para exámenes
class Examen(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='examenes')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField()

    def __str__(self):
        return self.titulo

# Modelo para preguntas del examen
class Pregunta(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.TextField()

    def __str__(self):
        return self.texto

# Modelo para opciones de respuesta
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

# Modelo para respuestas de los estudiantes
class Respuesta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} respondió {self.opcion.texto} para {self.pregunta.texto}"
