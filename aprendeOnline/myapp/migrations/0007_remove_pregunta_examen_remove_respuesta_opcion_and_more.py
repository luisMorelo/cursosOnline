# Generated by Django 4.2.13 on 2024-06-27 05:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_curso_imagen_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='examen',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='opcion',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.AddField(
        model_name='respuesta',
        name='examen',
        field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='myapp.examen'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='texto',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Opcion',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
    ]
