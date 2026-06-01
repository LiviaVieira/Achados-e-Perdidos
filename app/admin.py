from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(StatusItem)
admin.site.register(LocalEncontrado)
admin.site.register(ItemPerdido)
admin.site.register(ItemEncontrado)
admin.site.register(ConsultaItem)
admin.site.register(Devolucao)
admin.site.register(AtualizacaoItem)
admin.site.register(ExcluirItem)
admin.site.register(HistoricoDevolucao)
admin.site.register(Login)
admin.site.register(Registrar)
admin.site.register(FiltroCategoria)
admin.site.register(Relatorio)