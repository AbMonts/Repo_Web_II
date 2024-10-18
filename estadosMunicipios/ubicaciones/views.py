from django.shortcuts import render

from django.http import JsonResponse
from .models import Estado, Municipio
# Create your views here.



# def cargar_municipios(request):
#     estado_id = request.GET.get('estado_id')
#     municipios = Municipio.objects.filter(estado_id=estado_id).all()
#     return JsonResponse(list(municipios.values('id', 'nombre')), safe=False)

# def index(request):
#     estados = Estado.objects.all()
#     return render(request, 'ubicaciones/index.html', {'estados': estados})

#ctrl + k c
#ctrl + k u

def index(request):
    estados = Estado.objects.all()  # Obtener todos los estados
    return render(request, 'ubicaciones/index.html', {'estados': estados})

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre')
    return JsonResponse(list(municipios), safe=False)