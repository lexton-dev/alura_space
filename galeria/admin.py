from django.contrib import admin

from galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)# Tem que ter a vírgula porque aqui é uma tupla, senão não funcionará
    list_filter = ('categoria',)# Tem que ter a vírgula porque aqui é uma tupla, senão não funcionará
    list_editable = ('publicada',)# Tem que ter a vírgula porque aqui é uma tupla, senão não funcionará
    list_per_page = 3
    

admin.site.register(Fotografia, ListandoFotografias)
