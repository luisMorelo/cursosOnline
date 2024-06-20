import os
from django.core.exceptions import ValidationError

def validar_tipo_archivo(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.jpg', '.jpeg', '.png', '.mp4', '.mov','.wmv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'El archivo no tiene una extensión permitida. Extensiones permitidas: {", ".join(valid_extensions)}')
