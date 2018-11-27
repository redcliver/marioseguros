from django.db import models
from django.utils import timezone

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    data_nasc = models.DateTimeField(default=timezone.now, null=True, blank=True)
    inscricao = models.CharField(max_length=30, null=True, blank=True)
    venc_habilitacao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    rg = models.CharField(max_length=30, null=True, blank=True)
    rg_data = models.DateTimeField(null=True, blank=True)
    rg_uf = models.CharField(max_length=30, null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=6, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone1 = models.CharField(max_length=20, null=True, blank=True)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    email1 = models.CharField(max_length=200, null=True, blank=True)
    telefone2 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    email2 = models.CharField(max_length=200, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome