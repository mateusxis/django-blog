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

    def clean_username(self):
        username =  self.cleaned_data.get('username')

        if username:
            username = username.strip()
            if " " in username:
                raise forms.ValidationError("Espaços não são permitidos nesse campo.")
            else:
                return username
            
    def clean_confirmedPassword(self):
        password =  self.cleaned_data.get('password')
        confirmedPassword =  self.cleaned_data.get('confirmedPassword')

        if password and confirmedPassword and password != confirmedPassword:
            raise forms.ValidationError("Senhas não são iguais.")
        else:
            return confirmedPassword