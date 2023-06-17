from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Fulano da Silva'
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class RegisterForms(forms.Form):
    username = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: fulano.silva'
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: fulano.silva@xtpo.com'
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    confirmedPassword = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha mais uma vez'
            }
        )
    )