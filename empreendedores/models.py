from django.db import models


class Empreendedor(models.Model):
        IDENTIDADE_GENERO_CHOICES = [
        ('select_ident', 'Selecione a sua identidade de genero'),
        ('transmasculine', 'Transmasculine'),
        ('homem_trans', 'Homem Transgênero'),
        ('travesti', 'Travesti'),
        ('mulher_trans', 'Mulher Transgênero'),
        ('nao_binario', 'Não Binário'),
        ('outro', 'Outro'),
        ('prefiro_nao_dizer', 'Prefiro não dizer'),
    ]
        
        id = models.AutoField(primary_key=True)
        nome = models.CharField(max_length=100, verbose_name="Nome Completo")
        idade = models.IntegerField(verbose_name="Idade")
        identidadegenero = models.CharField(
            max_length=20,
            choices=IDENTIDADE_GENERO_CHOICES,
            verbose_name="Identidade de Gênero", default='select_ident')
        telefone = models.CharField(max_length=15, verbose_name="Telefone")
        email = models.EmailField(unique=True, verbose_name="E-mail")
        senha = models.CharField(max_length=300, verbose_name="Senha")
        servico = models.CharField(max_length=200, verbose_name="Serviço Oferecido")
        descricao = models.TextField(verbose_name="Descrição do Serviço")
        data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
        foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True, verbose_name="Foto de Perfil")

        def __str__(self):
            return self.nome  # Exibindo o nome do usuário (Empreendedor)
