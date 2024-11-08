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

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    descripcion_equipo = models.TextField()

    def __str__(self):
        return self.nombre_equipo

class UsuarioEquipo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.equipo.nombre_equipo} - {self.rol.nombre_rol}"

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    descripcion_proyecto = models.TextField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proyecto

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
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_sprint

class SprintTarea(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sprint.nombre_sprint} - {self.tarea.nombre_tarea}"

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tarea.nombre_tarea} - {self.fecha_comentario}"