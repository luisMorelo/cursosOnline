from django.contrib import admin
from .models import Curso, Inscripcion, Examen, Respuesta, Instructor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Inscripcion)
admin.site.register(Examen)
admin.site.register(Respuesta)
admin.site.register(Instructor)
