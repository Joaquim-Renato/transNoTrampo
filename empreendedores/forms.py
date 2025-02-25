from django import forms
from .models import Empreendedor


class EmpreendedorForm(forms.ModelForm):
    confirmacao_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirme sua senha"
    )


    class Meta:
        model = Empreendedor
        fields = [
        'nome', 'idade', 'identidadegenero', 'telefone', 'email', 'senha', 
        'confirmacao_senha', 'servico', 'descricao', 'foto_perfil']
        widgets = {
            'senha': forms.PasswordInput(),
            'identidadegenero': forms.Select(attrs={'class': 'form-control'}),
            
        }
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            raise forms.ValidationError("As senhas não coincidem. Digite novamente.")

        return cleaned_data
