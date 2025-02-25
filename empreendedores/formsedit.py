from django import forms
from .models import Empreendedor

class EmpreendedorEdicaoForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Deixe em branco caso não queira atualizar sua senha'}),

        label="Nova senha (opcional)",
        required=False
    )
    confirmacao_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Deixe em branco caso não queira atualizar sua senha'}),
        label="Confirme a nova senha",
        required=False
    )

    class Meta:
        model = Empreendedor
        fields = ['nome', 'idade', 'identidadegenero', 'telefone', 'email', 'senha', 'confirmacao_senha', 'servico', 'descricao', 'foto_perfil']
        
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha or confirmacao_senha:
            if senha != confirmacao_senha:
                raise forms.ValidationError("As senhas não coincidem. Digite novamente.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["senha"]:
            user.set_password(self.cleaned_data["senha"])
        if commit:
            user.save()
        return user
