from django.http import HttpResponse
from django.shortcuts import render


def portal_clientes(request):
    return render(request, 'respuesta_solicitud.html')

def trabajar(request):
    return HttpResponse("Hola mundo")

def cualquiercosa(request):
    return HttpResponse("<h1/>Endpoint haciendo cualquier cosa<h1/>")

def respuesta_solicitud(request):
    return render(request, 'respuesta_solicitud.html')