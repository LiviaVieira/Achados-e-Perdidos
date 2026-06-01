from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', IndexView.as_view(), name='index'),

    # RF01 - Itens Perdidos
    path(
        'itens/',
        ItensPerdidosView.as_view(),
        name='itens'
    ),

    # RF02 - Categorias
    path(
        'categorias/',
        CategoriasView.as_view(),
        name='categorias'
    ),

    # RF03 - Usuários
    path(
        'usuarios/',
        UsuariosView.as_view(),
        name='usuarios'
    ),

    # RF04 - Itens Encontrados
    path(
        'encontrados/',
        ItensEncontradosView.as_view(),
        name='encontrados'
    ),

    # RF05 - Consulta de Itens
    path(
        'consultas/',
        ConsultasView.as_view(),
        name='consultas'
    ),

    # RF06 - Locais Encontrados
    path(
        'locais/',
        LocaisView.as_view(),
        name='locais'
    ),

    # RF07 - Devoluções
    path(
        'devolucoes/',
        DevolucoesView.as_view(),
        name='devolucoes'
    ),

    # RF08 - Atualização de Itens
    path(
        'atualizacoes/',
        AtualizacoesView.as_view(),
        name='atualizacoes'
    ),

    # RF09 - Exclusões
    path(
        'exclusoes/',
        ExclusoesView.as_view(),
        name='exclusoes'
    ),

    # RF10 - Histórico de Devoluções
    path(
        'historico/',
        HistoricoView.as_view(),
        name='historico'
    ),

    # RF11 - Login
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    # RF12 - Status dos Itens
    path(
        'status/',
        StatusView.as_view(),
        name='status'
    ),

    # RF13 - Responsável pelo Cadastro
    path(
        'registrar/',
        RegistrarView.as_view(),
        name='registrar'
    ),

    # RF14 - Filtro por Categoria
    path(
        'filtros/',
        FiltroCategoriaView.as_view(),
        name='filtros'
    ),

    # RF15 - Relatórios
    path(
        'relatorios/',
        RelatoriosView.as_view(),
        name='relatorios'
    ),

]