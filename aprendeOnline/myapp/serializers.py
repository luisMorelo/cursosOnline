from rest_framework import serializers
from .models import Curso, Inscripcion


class cursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso

        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion']

        #le indico que este campo sera solo lectura y no se puede modificar
        read_only_fields = ('fecha_creacion',) 




class InscripcionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inscripcion
        fields = ['id', 'curso', 'inscrito_en']