from django.contrib import admin
from anuncio.models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_criacao', 'valor', 'veiculo', 'usuario')
    search_fields = ('titulo', 'descricao')

admin.site.register(Anuncio, AnuncioAdmin)