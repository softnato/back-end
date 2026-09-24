from django.contrib import admin
from .models import (
    PerfilVoluntario, Organizacion, Categoria, Actividad, 
    Inscripcion, Resena, Comuna, Habilidad, HistorialEstadoInscripcion
)

admin.site.register(PerfilVoluntario)
admin.site.register(Organizacion)
admin.site.register(Categoria)
admin.site.register(Actividad)
admin.site.register(Inscripcion)
admin.site.register(Resena)
admin.site.register(Comuna)
admin.site.register(Habilidad)
admin.site.register(HistorialEstadoInscripcion)