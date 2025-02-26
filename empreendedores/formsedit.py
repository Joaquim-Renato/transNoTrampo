from django import forms
from .models import Empreendedor
from .utils import criptografia 

class EmpreendedorEdicaoForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha sera resetada,insira uma nova'}),
        label="Nova senha",
       
    )
    confirmacao_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha sera resetada por favor insira uma nova'}),
        label="Confirme a nova senha",
        
    )

    class Meta:
        model = Empreendedor
        fields = ['nome', 'idade', 'identidadegenero', 'telefone', 'email', 'senha', 'confirmacao_senha', 'servico', 'descricao', 'foto_perfil']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        # Verificar se a senha foi informada e se a confirmação é válida
        if senha and confirmacao_senha:
            if senha != confirmacao_senha:
                raise forms.ValidationError("As senhas não coincidem. Digite novamente.")

        return cleaned_data

def save(self, commit=True):
    user = super().save(commit=False)

    if self.cleaned_data.get("senha"):
        # Em vez de user.set_password(), use a função de criptografia correta
        user.senha = criptografia(self.cleaned_data["senha"])

    if commit:
        user.save()
    return user
