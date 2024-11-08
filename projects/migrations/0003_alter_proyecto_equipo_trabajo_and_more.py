# Generated by Django 5.1.3 on 2024-11-08 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_id_tarea_comentario_tarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='equipo_trabajo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.equipotrabajo'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='equipo_trabajo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='projects.equipotrabajo'),
        ),
    ]
