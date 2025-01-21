from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmpreendedorSignUpForm(UserCreationForm):
    idade = forms.IntegerField(label="Idade", required=True)
    identidadegenero = forms.CharField(label="Identidade de Gênero", max_length=50, required=True)
    telefone = forms.CharField(label="Telefone", max_length=15, required=True)
    servico = forms.CharField(label="Serviço", max_length=100, required=True)
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={"rows": 3}), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
