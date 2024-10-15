from django.urls import path
from .views import cargar_municipios

urlpatterns = [
    path('ajax/cargar-municipios/', cargar_municipios, name='ajax_cargar_municipios'),
]