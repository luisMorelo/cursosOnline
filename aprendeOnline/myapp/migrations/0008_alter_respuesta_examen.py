# Generated by Django 4.2.13 on 2024-06-27 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_pregunta_examen_remove_respuesta_opcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='examen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='myapp.examen'),
        ),
    ]