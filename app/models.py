from django.db import models


class Usuario(models.Model):

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do usuário"
    )

    email = models.CharField(
        max_length=100,
        verbose_name="Email do usuário"
    )

    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone"
    )

    tipo_usuario = models.CharField(
        max_length=30,
        verbose_name="Tipo de usuário"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Categoria(models.Model):

    nome = models.CharField(
        max_length=50,
        verbose_name="Categoria"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class LocalEncontrado(models.Model):

    nome_local = models.CharField(
        max_length=50,
        verbose_name="Local encontrado"
    )

    def __str__(self):
        return self.nome_local

    class Meta:
        verbose_name = "Local Encontrado"
        verbose_name_plural = "Locais Encontrados"


class ItemPerdido(models.Model):

    nome_item = models.CharField(
        max_length=100,
        verbose_name="Nome do item"
    )

    descricao = models.CharField(
        max_length=255,
        verbose_name="Descrição"
    )

    data_perda = models.DateField(
        verbose_name="Data da perda"
    )

    status = models.CharField(
        max_length=30,
        verbose_name="Status"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name="Categoria"
    )

    local = models.ForeignKey(
        LocalEncontrado,
        on_delete=models.CASCADE,
        verbose_name="Local encontrado"
    )

    def __str__(self):
        return self.nome_item

    class Meta:
        verbose_name = "Item Perdido"
        verbose_name_plural = "Itens Perdidos"


class ItemEncontrado(models.Model):

    item = models.ForeignKey(
        ItemPerdido,
        on_delete=models.CASCADE,
        verbose_name="Item perdido"
    )

    local_encontrado = models.CharField(
        max_length=50,
        verbose_name="Local encontrado"
    )

    data_encontro = models.DateField(
        verbose_name="Data do encontro"
    )

    def __str__(self):
        return f"{self.item}"

    class Meta:
        verbose_name = "Item Encontrado"
        verbose_name_plural = "Itens Encontrados"

class Devolucao(models.Model):

    item = models.ForeignKey(
        ItemPerdido,
        on_delete=models.CASCADE,
        verbose_name="Item devolvido"
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    data_devolucao = models.DateField(
        verbose_name="Data da devolução"
    )

    observacoes = models.CharField(
        max_length=255,
        verbose_name="Observações"
    )

    def __str__(self):
        return f"{self.item}"

    class Meta:
        verbose_name = "Devolução"
        verbose_name_plural = "Devoluções"