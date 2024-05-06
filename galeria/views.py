from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

# Create your views here.
# from django.http import HttpResponse


def index(request):
    # fotografias = Fotografia.objects.all()# Traz todos os itens do banco de dados
    
    # filter() significa que ele filtra quais os itens eu quero trazer do banco de dados
    # fotografias = Fotografia.objects.filter(publicada=True)# publicada=True é um campo que eu adicionei ao arquivo models.py
    
    # filter() junto com order_by. O order_by mostra os campos de forma ascendente ou descendente
    # Colocando o sinal de menos (-) em ('-data_fotografia') ele inverte as posições e o mais recente aparece primeiro
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)# Ordenando por data_fotografia
    
    ''' Dicionário retirado e substituido
    dados = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelecope.org / NASA / James webb'},
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / NASA / Hubble'}
}
    return render(request, 'galeria/index.html', {'cards': dados})# cards ligado ao for da index.html
'''
    return render(request, 'galeria/index.html', {"cards": fotografias})# cards ligado ao for da index.html
    
def imagem(request, foto_id):# foto_id sendo recebida de urls.py
    fotografia = get_object_or_404(Fotografia, pk=foto_id)# Ou pega o objeto ou diz que ele não foi encontrado
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})