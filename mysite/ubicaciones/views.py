from django.http import JsonResponse
from django.shortcuts import render
from .models import Municipio, Estado

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).all()
    return JsonResponse(list(municipios.values('id', 'nombre')), safe=False)
def index(request):
    estados = Estado.objects.all()
    return render(request, 'index.html', {'estados': estados})