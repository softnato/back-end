from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    PerfilVoluntario, Organizacion, Categoria, Actividad,
    Inscripcion, Resena, Comuna, Habilidad, HistorialEstadoInscripcion
)
from .serializers import (
    PerfilVoluntarioSerializer, OrganizacionSerializer, CategoriaSerializer,
    ActividadSerializer, InscripcionSerializer, ResenaSerializer,
    ComunaSerializer, HabilidadSerializer, HistorialEstadoInscripcionSerializer
)
def bienvenida(request):
    return render(request, 'Voluntariado_actividades_comunitarias/inicio.html')

def pagina_no_encontrada(request, exception):
    return render(request, '404.html', status=404)
class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.filter(habilitado=True).order_by('-id')
    serializer_class = ActividadSerializer

class PerfilVoluntarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilVoluntario.objects.filter(habilitado=True).order_by('-id')
    serializer_class = PerfilVoluntarioSerializer

class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = OrganizacionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(habilitado=True).order_by('-id')
    serializer_class = CategoriaSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = InscripcionSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.filter(habilitado=True).order_by('-id')
    serializer_class = ResenaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.filter(habilitado=True).order_by('-id')
    serializer_class = ComunaSerializer

class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidad.objects.filter(habilitado=True).order_by('-id')
    serializer_class = HabilidadSerializer

class HistorialEstadoInscripcionViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoInscripcion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = HistorialEstadoInscripcionSerializer