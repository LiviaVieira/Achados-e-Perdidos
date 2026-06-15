from django.contrib import admin
from .models import *

# INLINE 1
class ItemPerdidoInline(admin.TabularInline):
    model = ItemPerdido
    extra = 0

# INLINE 2
class DevolucaoInline(admin.TabularInline):
    model = Devolucao
    extra = 0

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ItemPerdidoInline]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = [DevolucaoInline]

admin.site.register(StatusItem)
admin.site.register(LocalEncontrado)
admin.site.register(ItemEncontrado)
admin.site.register(ConsultaItem)
admin.site.register(AtualizacaoItem)
admin.site.register(ExcluirItem)
admin.site.register(HistoricoDevolucao)
admin.site.register(Login)
admin.site.register(Registrar)
admin.site.register(FiltroCategoria)
admin.site.register(Relatorio)