from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    PerfilVoluntario, Organizacion, Categoria, Actividad,
    Inscripcion, Resena, Comuna, Habilidad, HistorialEstadoInscripcion
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PerfilVoluntarioSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = PerfilVoluntario
        fields = '__all__'

class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    organizacion_nombre = serializers.ReadOnlyField(source='organizacion.nombre')
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    cupos_disponibles = serializers.ReadOnlyField()

    class Meta:
        model = Actividad
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    voluntario_username = serializers.ReadOnlyField(source='voluntario.username')
    actividad_titulo = serializers.ReadOnlyField(source='actividad.titulo')

    class Meta:
        model = Inscripcion
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = '__all__'

class HistorialEstadoInscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoInscripcion
        fields = '__all__'