from django import forms
from django.contrib.auth.models import User
from .models import QuemSomos, Historia, DocumentoGeral, AtaReuniao, Diretoria, Associado, Usuario

# formulário para link APREPI

class QuemSomosForm(forms.ModelForm):
    class Meta:
        model = QuemSomos
        fields = '__all__'


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = '__all__'

class DocumentoGeralForm(forms.ModelForm):
    class Meta:
        model = DocumentoGeral
        fields = ['titulo', 'arquivo', 'descricao']

class AtaReuniaoForm(forms.ModelForm):
    class Meta:
        model = AtaReuniao
        fields = ['titulo', 'arquivo', 'descricao']

# formulário para link DIRETORIA

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = '__all__'

# formulário para REGISTRO

class AssociadoForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Associado
        fields = ['nome', 'endereco', 'matricula', 'email']

    def save(self, commit=True):
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
            email = self.cleaned_data['email']
        )
        associado = super().save(commit=False)
        associado.user = user
        if commit:
            associado.save()
        return associado


class UsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'email']

    def save(self, commit=True):
        user = User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password'],
            email = self.cleaned_data['email']
        )
        usuario = super().save(commit=False)
        usuario.user = user
        if commit:
            usuario.save()
        return usuario
