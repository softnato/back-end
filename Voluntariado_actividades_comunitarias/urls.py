from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActividadViewSet, PerfilVoluntarioViewSet, OrganizacionViewSet,
    CategoriaViewSet, InscripcionViewSet, ResenaViewSet,
    ComunaViewSet, HabilidadViewSet, HistorialEstadoInscripcionViewSet
)

router = DefaultRouter()
router.register(r'actividades', ActividadViewSet, basename='actividad')
router.register(r'perfiles', PerfilVoluntarioViewSet, basename='perfil')
router.register(r'organizaciones', OrganizacionViewSet, basename='organizacion')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripcion')
router.register(r'resenas', ResenaViewSet, basename='resena')
router.register(r'comunas', ComunaViewSet, basename='comuna')
router.register(r'habilidades', HabilidadViewSet, basename='habilidad')
router.register(r'historial-inscripciones', HistorialEstadoInscripcionViewSet, basename='historial-inscripcion')

urlpatterns = [
    path('', include(router.urls)),
]