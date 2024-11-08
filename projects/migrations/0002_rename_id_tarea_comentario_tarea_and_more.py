# Generated by Django 5.1.3 on 2024-11-08 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='id_tarea',
            new_name='tarea',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='sprint',
            old_name='id_tarea',
            new_name='tarea',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='usuarioequipo',
            old_name='id_equipo_trabajo',
            new_name='equipo_trabajo',
        ),
        migrations.RenameField(
            model_name='usuarioequipo',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='equipotrabajo',
            name='id_proyecto',
        ),
        migrations.RemoveField(
            model_name='equipotrabajo',
            name='rol_id',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='id_sprint',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='equipo_trabajo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.equipotrabajo'),
        ),
        migrations.AddField(
            model_name='roles',
            name='equipo_trabajo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='projects.equipotrabajo'),
        ),
    ]
