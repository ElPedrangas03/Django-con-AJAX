from django.http import JsonResponse
from .models import Municipio

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).all()
    return JsonResponse(list(municipios.values('id', 'nombre')), safe=False)