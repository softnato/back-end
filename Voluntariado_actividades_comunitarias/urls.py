from rest_framework.routers import DefaultRouter
from .views import (
    PerfilVoluntarioViewSet, OrganizacionViewSet, CategoriaViewSet,
    ActividadViewSet, InscripcionViewSet, ResenaViewSet,
    ComunaViewSet, HabilidadViewSet, HistorialEstadoInscripcionViewSet
)

router = DefaultRouter()
router.register(r'perfiles', PerfilVoluntarioViewSet)
router.register(r'organizaciones', OrganizacionViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'actividades', ActividadViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'resenas', ResenaViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'habilidades', HabilidadViewSet)
router.register(r'historial-inscripciones', HistorialEstadoInscripcionViewSet)

urlpatterns = router.urls