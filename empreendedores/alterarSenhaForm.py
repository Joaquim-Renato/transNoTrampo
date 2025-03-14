from django import forms
from .models import Empreendedor
from .utils import criptografia

class AlterarSenhaForm(forms.ModelForm):
    senha_atual = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha atual'}),
        label="Senha atual",
        required=True,
    )
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a nova senha'}),
        label="Nova senha",
        required=True,
    )
    confirmacao_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a nova senha'}),
        label="Confirme a nova senha",
        required=True,
    )

    class Meta:
        model = Empreendedor
        fields = []  # Não precisamos de campos do modelo aqui

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get("nova_senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        # Verificar se as senhas coincidem
        if nova_senha and confirmacao_senha:
            if nova_senha != confirmacao_senha:
                raise forms.ValidationError("As senhas não coincidem. Digite novamente.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data.get("nova_senha"):
            # Criptografa a nova senha
            user.senha = criptografia(self.cleaned_data["nova_senha"])

        if commit:
            user.save()
        return user