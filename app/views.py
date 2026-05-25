from django.shortcuts import render, redirect, get_object_or_404
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