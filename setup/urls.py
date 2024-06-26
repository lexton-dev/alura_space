"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from galeria.views import index -> Foi para urls.py da galeria

# # Agora, precisamos tornar o urlpatterns dp arquivo urls.py da galeria disponível aqui. 
# Para isso, removeremos a linha de código da galeria.views. 
# Em django.urls, vamos importar, além de path, um método chamado include.

# Vamos remover index do último path do código e substitui-lo por include(). 
# Dentro dos parênteses, vamos inserir o nome do aplicativo, "galeria", e urls:
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),  -> Não precisamos mais...
    path('', include('galeria.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
