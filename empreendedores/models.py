from django.db import models


class Empreendedor(models.Model):
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()  
    identidadegenero = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=300)
    servico = models.CharField(max_length=200)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome  # Exibindo o nome do usuário (Empreendedor)
