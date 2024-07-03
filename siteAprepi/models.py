from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# construindo a NAVBAR:
# modelos para o link APREPI

class QuemSomos(models.Model):
    titulo = models.CharField(max_length=200, default='Quem Somos')
    conteudo = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='quem_somos_image/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    

class Historia(models.Model):
    titulo = models.CharField(max_length=200, default='Historia')
    conteudo = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='historia_image/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
# modelos para sublink TRANSPARÊNCIA

class DocumentoGeral(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentos_gerais/')
    descricao = models.TextField(blank=True, null=True)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class AtaReuniao(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='atas_reunioes/')
    descricao = models.TextField(blank=True, null=True)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# modelo para o link DIRETORIA

class Diretoria(models.Model):
    titulo = models.CharField(max_length=100, default='Diretoria')
    imagem_diretoria = models.ImageField(upload_to='diretoria/', blank=True, null=True)
    descricao_diretoria = models.TextField(blank=True, null=True)
    imagem_conselho_fiscal = models.ImageField(upload_to='conselho_fiscal/', blank=True, null=True)
    descricao_conselho_fiscal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# modelos para REGISTRO

class Associado(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    matricula = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='associados', default=1 )

    def __str__(self):
        return self.nome
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuarios', default=1)

    def __srt__(self):
        return self.nome
    
