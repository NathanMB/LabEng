from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Medico



class MedicoCreationForm(UserCreationForm):
    email = forms.CharField(min_length=6)
    first_name = forms.CharField(min_length=3)
    last_name = forms.CharField(min_length=3)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = Medico
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = Medico.objects.get(email=email)
        except Medico.DoesNotExist:
            return email
        raise forms.ValidationError('Esse email já existe')

class MedicoChangeForm(UserChangeForm):
    crm = forms.CharField(min_length=5)
    email = forms.CharField(min_length=6)
    first_name = forms.CharField(min_length=6)
    last_name = forms.CharField(min_length=6)
    password = forms.CharField()

    class Meta:
        model = Medico
        fields = ['first_name', 'last_name', 'email', 'crm']

class MedicoAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'id': 'id_usuario',
                                      'class': 'form-control pl-5',
                                      'placeholder': 'Informe seu email',
                                      'size': '60'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'id_password',
                                          'class': 'form-control pl-5',
                                          'placeholder': 'Digite a senha',
                                          'size': '60'}))