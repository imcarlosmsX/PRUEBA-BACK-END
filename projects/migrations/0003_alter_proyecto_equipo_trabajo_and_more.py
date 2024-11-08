from django.db import migrations, models

def set_default_equipo_trabajo(apps, schema_editor):
    Roles = apps.get_model('projects', 'Roles')
    EquipoTrabajo = apps.get_model('projects', 'EquipoTrabajo')
    default_equipo = EquipoTrabajo.objects.get(pk=1)  # Replace 1 with the actual default ID
    Roles.objects.filter(equipo_trabajo__isnull=True).update(equipo_trabajo=default_equipo)

class Migration(migrations.Migration):

    dependencies = [
        ('projects', 'previous_migration_name'),  # Replace with the actual previous migration name
    ]

    operations = [
        migrations.RunPython(set_default_equipo_trabajo),
    ]