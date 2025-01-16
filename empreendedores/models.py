from django.db import models

# Create your models here.


class Empreendedor(models.Model):
    codigo = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=4)
    identidadegenero = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    servico = models.CharField(max_length=200)
    descricao  = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome