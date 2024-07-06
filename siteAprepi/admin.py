from django.contrib import admin
from .models import QuemSomos, Historia, DocumentoGeral, AtaReuniao, Diretoria, CarrosselNoticia, Noticia

# NAVBAR
# Link APREPI

@admin.register(QuemSomos)
class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'conteudo')

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'conteudo')

@admin.register(DocumentoGeral)
class DocumentoGeralAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'descricao')

@admin.register(AtaReuniao)
class AtaReuniaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'descricao')

# link DIRETORIA

@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


# CARROSSEL

@admin.register(CarrosselNoticia)
class CarrosselNoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem')


# PÁGINA PRINCIPAL (HOME)
# Campo NOTÍCIAS RECENTES:

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_publicacao')
    list_filter = ('categoria', 'data_publicacao')
    search_fields = ('titulo', 'descricao', 'conteudo')

