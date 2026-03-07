from django.db import models


class Tag(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField()
    link = models.URLField(blank=True)
    codigo = models.URLField(blank=True)
    

    def __str__(self):
        return self.titulo


class Certificacao(models.Model):
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    emitido_em = models.DateField(null=True, blank=True,help_text="Formato YYYY/MM/DD")

    def __str__(self):
        return self.titulo


class TecHabilidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Carreira(models.Model):
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
    localizacao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)  # Ex: Estágio, Curso, Trabalho
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    habilidades = models.ManyToManyField(TecHabilidade, blank=True)

    def __str__(self):
        return self.titulo