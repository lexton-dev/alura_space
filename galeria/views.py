from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def index(request):
    # return HttpResponse('<h1> Alura Space </h1>') - Não precisamos mais deste
    return render(request, 'galeria/index.html')
    
def imagem(request):
    return render(request, 'galeria/imagem.html')