from django.contrib import admin
from .models import *


admin.site.register(Usuario)

admin.site.register(Categoria)

admin.site.register(LocalEncontrado)

admin.site.register(ItemPerdido)

admin.site.register(ItemEncontrado)

admin.site.register(Devolucao)
