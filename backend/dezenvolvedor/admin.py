# Register your models here.
from django.contrib import admin
from .models.dev import  Tag, Projeto, Certificacao, TecHabilidade, Carreira
# Register your models here.

admin.site.index_title = "Administração do Portfólio"
admin.site.register(Tag)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao', 'link')
    search_fields = ('titulo',)

@admin.register(Certificacao)
class CertificacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'emitido_em')
    search_fields = ('titulo', 'instituicao')

@admin.register(TecHabilidade)
class TecHabilidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Carreira)
class CarreiraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao')
    search_fields = ('titulo', 'instituicao')