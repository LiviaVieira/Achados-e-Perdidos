from django.shortcuts import render
from django.views import View

from .models import *


class IndexView(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'index.html'
        )


class ItensPerdidosView(View):

    def get(self, request, *args, **kwargs):

        itens = ItemPerdido.objects.all()

        return render(
            request,
            'itens.html',
            {'itens': itens}
        )


class CategoriasView(View):

    def get(self, request, *args, **kwargs):

        categorias = Categoria.objects.all()

        return render(
            request,
            'categorias.html',
            {'categorias': categorias}
        )


class UsuariosView(View):

    def get(self, request, *args, **kwargs):

        usuarios = Usuario.objects.all()

        return render(
            request,
            'usuarios.html',
            {'usuarios': usuarios}
        )


class LocaisView(View):

    def get(self, request, *args, **kwargs):

        locais = LocalEncontrado.objects.all()

        return render(
            request,
            'locais.html',
            {'locais': locais}
        )


class ItensEncontradosView(View):

    def get(self, request, *args, **kwargs):

        encontrados = ItemEncontrado.objects.all()

        return render(
            request,
            'encontrados.html',
            {'encontrados': encontrados}
        )


class DevolucoesView(View):

    def get(self, request, *args, **kwargs):

        devolucoes = Devolucao.objects.all()

        return render(
            request,
            'devolucoes.html',
            {'devolucoes': devolucoes}
        )


class ConsultasView(View):

    def get(self, request, *args, **kwargs):

        consultas = ConsultaItem.objects.all()

        return render(
            request,
            'consultas.html',
            {'consultas': consultas}
        )


class AtualizacoesView(View):

    def get(self, request, *args, **kwargs):

        atualizacoes = AtualizacaoItem.objects.all()

        return render(
            request,
            'atualizacoes.html',
            {'atualizacoes': atualizacoes}
        )


class ExclusoesView(View):

    def get(self, request, *args, **kwargs):

        exclusoes = ExcluirItem.objects.all()

        return render(
            request,
            'exclusoes.html',
            {'exclusoes': exclusoes}
        )


class HistoricoView(View):

    def get(self, request, *args, **kwargs):

        historicos = HistoricoDevolucao.objects.all()

        return render(
            request,
            'historico.html',
            {'historicos': historicos}
        )


class LoginView(View):

    def get(self, request, *args, **kwargs):

        logins = Login.objects.all()

        return render(
            request,
            'login.html',
            {'logins': logins}
        )


class StatusView(View):

    def get(self, request, *args, **kwargs):

        status = StatusItem.objects.all()

        return render(
            request,
            'status.html',
            {'status': status}
        )


class RegistrarView(View):

    def get(self, request, *args, **kwargs):

        registros = Registrar.objects.all()

        return render(
            request,
            'registrar.html',
            {'registros': registros}
        )


class FiltroCategoriaView(View):

    def get(self, request, *args, **kwargs):

        filtros = FiltroCategoria.objects.all()

        return render(
            request,
            'filtros.html',
            {'filtros': filtros}
        )


class RelatoriosView(View):

    def get(self, request, *args, **kwargs):

        relatorios = Relatorio.objects.all()

        return render(
            request,
            'relatorios.html',
            {'relatorios': relatorios}
        )