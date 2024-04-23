# Vamos importar:
from django.urls import path
from galeria.views import index

# Criando uma lista para manter todos os endereços da nossa aplicação relacionados à galeria, 
# com o comando urlpatterns, dentro do qual criaremos uma lista, abrindo colchetes.
urlpatterns = [
    path('', index, name='index'),
]