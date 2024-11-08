from rest_framework import serializers
from .models import Usuario, Roles, Tarea, Sprint, Proyecto, EquipoTrabajo, UsuarioEquipo, Comentario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ['id',]

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
        read_only_fields = ['id']

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        read_only_fields = ['id']


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'
        read_only_fields = ['id']


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        read_only_fields = ['id']

class EquipoTrabajoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipoTrabajo
        fields = '__all__'
        read_only_fields = ['id']

class UsuarioEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEquipo
        fields = '__all__'
        read_only_fields = ['id']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ['id']