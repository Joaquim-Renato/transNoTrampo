from django import forms
from .models import Empreendedor


class EmpreendedorEdicaoForm(forms.ModelForm):

    class Meta:
        model = Empreendedor
        fields = [
            'nome', 'idade', 'identidadegenero', 'telefone', 'email', 'servico', 'descricao', 'cidade', 'estado', 'foto_perfil']

    