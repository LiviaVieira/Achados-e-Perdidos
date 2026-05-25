from django.contrib import admin
from django.urls import path

from app.views import *


urlpatterns = [

    # ADMIN
    path(
        'admin/',
        admin.site.urls
    ),

    # HOME
    path(
        '',
        IndexView.as_view(),
        name='index'
    ),

    # ITENS PERDIDOS
    path(
        'itens/',
        ItensPerdidosView.as_view(),
        name='itens'
    ),

    # CATEGORIAS
    path(
        'categorias/',
        CategoriasView.as_view(),
        name='categorias'
    ),

    # USUÁRIOS
    path(
        'usuarios/',
        UsuariosView.as_view(),
        name='usuarios'
    ),

    # LOCAIS ENCONTRADOS
    path(
        'locais/',
        LocaisView.as_view(),
        name='locais'
    ),

    # ITENS ENCONTRADOS
    path(
        'encontrados/',
        ItensEncontradosView.as_view(),
        name='encontrados'
    ),

    # DEVOLUÇÕES
    path(
        'devolucoes/',
        DevolucoesView.as_view(),
        name='devolucoes'
    ),

]