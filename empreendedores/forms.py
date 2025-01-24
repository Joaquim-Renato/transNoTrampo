from django import forms
from .models import Empreendedor


class EmpreendedorForm(forms.ModelForm):
    class Meta:
        model = Empreendedor
        fields = ['nome', 'idade', 'identidadegenero', 'telefone', 'email', 'senha', 'servico', 'descricao']
        widgets = {
            'senha': forms.PasswordInput(),  # Isso vai garantir que o campo senha seja exibido como '*****'
        }
