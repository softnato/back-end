from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Voluntariado_actividades_comunitarias.views import (bienvenida,vista_protegida_funcion,VistaProtegidaClase)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida, name='bienvenida'),
    path('voluntariado/', include('Voluntariado_actividades_comunitarias.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='Voluntariado_actividades_comunitarias/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='bienvenida'), name='logout'),
    path('protegida-funcion/', vista_protegida_funcion, name='protegida_funcion'),
    path('protegida-clase/', VistaProtegidaClase.as_view(), name='protegida_clase'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'Voluntariado_actividades_comunitarias.views.pagina_no_encontrada'