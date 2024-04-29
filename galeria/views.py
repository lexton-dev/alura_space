from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def index(request):
    dados = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelecope.org / NASA / James webb'},
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / NASA / Hubble'}
}
    return render(request, 'galeria/index.html', {'cards': dados})# cards ligado ao for da index.html
    
def imagem(request):
    return render(request, 'galeria/imagem.html')