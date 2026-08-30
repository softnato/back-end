from django.shortcuts import render

def bienvenida(request):
    return render(request, 'Voluntariado_actividades_comunitarias/inicio.html')

def pagina_no_encontrada(request, exception):
    return render(request, 'Voluntariado_actividades_comunitarias/404.html', status=404)