from django.shortcuts import render
from .models import Noticia
# Create your views here.

def lista_noticias(request):
    noticias = Noticia.objects.order_by('-fecha')  # las más recientes primero
    return render(request, 'app_noticias/lista.html', {'noticias': noticias})