from rest_framework import viewsets
from django.shortcuts import render, HttpResponse
import requests
from django.views.generic.list import ListView  

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'codigo'and 'latitud'and 'longitud'and 'producto'and 'area' in request.GET:
        codigo = request.GET['codigo']
        latitud = request.GET['latitud']
        longitud = request.GET['longitud']
        producto = request.GET['producto']
        area = request.GET['area']
        
        # Verifica si el value no esta vacio
        if codigo and latitud and longitud and producto and area:
            # Crea el json para realizar la petición POST al Web Service
            args = {'codigo':codigo,
                    'latitud': latitud,
                    'longitud':longitud,
                    'producto': producto,
                    'area':area}
            
            response = requests.post('http://127.0.0.1:8000/temphum/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()
            
    response = requests.get('https://pi1-eafit-clopezr9.azurewebsites.net/')
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})
