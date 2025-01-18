from django.db import models
from django.contrib.auth.models import User

class Empreendedor(models.Model):
    id = models.AutoField(primary_key=True)
    
    idade = models.CharField(max_length=4)
    identidadegenero = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    servico = models.CharField(max_length=200)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username  # Exibindo o nome do usuário (Empreendedor)
