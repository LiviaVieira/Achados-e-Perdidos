from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class StatusItem(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class LocalEncontrado(models.Model):
    nome_local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_local


class ItemPerdido(models.Model):
    nome_item = models.CharField(max_length=100)
    descricao = models.TextField()
    data_perda = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_item


class ItemEncontrado(models.Model):
    nome_item = models.CharField(max_length=100)
    descricao = models.TextField()
    local_encontrado = models.ForeignKey(LocalEncontrado, on_delete=models.CASCADE)
    data_encontro = models.DateField()

    def __str__(self):
        return self.nome_item


class ConsultaItem(models.Model):
    pesquisa = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return self.pesquisa


class Devolucao(models.Model):
    data_devolucao = models.DateField()
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return f"Devolução {self.id}"


class AtualizacaoItem(models.Model):
    descricao = models.TextField()
    status = models.ForeignKey(StatusItem, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atualização {self.id}"


class ExcluirItem(models.Model):
    id_item = models.IntegerField()
    motivo_exclusao = models.CharField(max_length=200)

    def __str__(self):
        return f"Exclusão {self.id_item}"


class HistoricoDevolucao(models.Model):
    item = models.ForeignKey(ItemPerdido, on_delete=models.CASCADE)
    dono = models.CharField(max_length=100)
    data_devolucao = models.DateField()

    def __str__(self):
        return self.dono


class Login(models.Model):
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Registrar(models.Model):
    responsavel_cadastro = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.responsavel_cadastro.nome


class FiltroCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade_itens = models.IntegerField()

    def __str__(self):
        return self.categoria.nome


class Relatorio(models.Model):
    quantidade = models.IntegerField()
    categorias = models.CharField(max_length=200)
    datas = models.DateField()

    def __str__(self):
        return f"Relatório {self.id}"