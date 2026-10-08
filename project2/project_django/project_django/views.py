from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def portal_clientes(request):
    return render(request, 'dashboard.html')