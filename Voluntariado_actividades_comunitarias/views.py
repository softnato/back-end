from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import (
    Organizacion, Categoria, Actividad, PerfilVoluntario,
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Actividad deshabilitada correctamente'}, status=status.HTTP_200_OK)


class PerfilVoluntarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilVoluntario.objects.filter(habilitado=True).order_by('-id')
    serializer_class = PerfilVoluntarioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Perfil deshabilitado correctamente'}, status=status.HTTP_200_OK)


class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = OrganizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Organización deshabilitada correctamente'}, status=status.HTTP_200_OK)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(habilitado=True).order_by('-id')
    serializer_class = CategoriaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Categoría deshabilitada correctamente'}, status=status.HTTP_200_OK)


class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = InscripcionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Inscripción deshabilitada correctamente'}, status=status.HTTP_200_OK)


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.filter(habilitado=True).order_by('-id')
    serializer_class = ResenaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Reseña deshabilitada correctamente'}, status=status.HTTP_200_OK)


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.filter(habilitado=True).order_by('-id')
    serializer_class = ComunaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Comuna deshabilitada correctamente'}, status=status.HTTP_200_OK)


class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidad.objects.filter(habilitado=True).order_by('-id')
    serializer_class = HabilidadSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Habilidad deshabilitada correctamente'}, status=status.HTTP_200_OK)


class HistorialEstadoInscripcionViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoInscripcion.objects.filter(habilitado=True).order_by('-id')
    serializer_class = HistorialEstadoInscripcionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.habilitado = False
        instance.save()
        return Response({'mensaje': 'Historial deshabilitado correctamente'}, status=status.HTTP_200_OK)
    
    
@login_required
def vista_protegida_funcion(request):
    return render(request, 'Voluntariado_actividades_comunitarias/protegida_funcion.html')

class VistaProtegidaClase(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'Voluntariado_actividades_comunitarias/protegida_clase.html')