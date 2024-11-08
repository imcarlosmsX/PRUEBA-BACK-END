from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Roles(models.Model):
    nombre_rol = models.CharField(max_length=100)
    descripcion_rol = models.TextField()

    def __str__(self):
        return self.nombre_rol

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=255)
    estado_tarea = models.CharField(max_length=50)
    fecha_creacion_tarea = models.DateField()
    fecha_entrega_tarea = models.DateField()
    descripcion_tarea = models.TextField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tarea


class Sprint(models.Model):
    nombre_sprint = models.CharField(max_length=255)
    fecha_inicio_sprint = models.DateField()
    fecha_fin_sprint = models.DateField()
    estado_sprint = models.CharField(max_length=50)
    id_tarea = models.ForeignKey(Tarea, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_sprint

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    descripcion_proyecto = models.TextField()
    fecha_inicio_proyecto = models.DateField()
    fecha_fin_proyecto = models.DateField()
    estado_proyecto = models.CharField(max_length=50)
    id_sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_proyecto


class EquipoTrabajo(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    descripcion_equipo = models.TextField()
    rol_id = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_equipo


class UsuarioEquipo(models.Model):
    usuario_equipo_id = models.AutoField(primary_key=True)
    fecha_union = models.DateField()
    rol_equipo = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_equipo_trabajo = models.ForeignKey(EquipoTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_usuario} - {self.id_equipo_trabajo}"

class Comentario(models.Model):
    contenido_comentario = models.TextField()
    fecha_comentario = models.DateField()
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentario by {self.id_usuario} on Tarea {self.id_tarea}"



