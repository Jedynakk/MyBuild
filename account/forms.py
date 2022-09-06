from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'LOGIN'}), label="LOGIN")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'fieldsy', 'placeholder': 'HASŁO'}), label="HASŁO")




class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'fieldsy', 'placeholder': 'HASŁO'}), label="HASŁO")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'fieldsy', 'placeholder': 'PONÓW HASŁO'}), label="PONÓW HASŁO")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'LOGIN'}),
            'email': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'E-MIAL'}),
            'first_name': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'IMIĘ'}),
            'last_name': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'NAZWISKO'}),
        }

        labels = {
            "username": "LOGIN",
            "email": "E-MAIL",
            "first_name": "IMIĘ",
            "last_name": "NAZWISKO",
        }
        help_texts = {
            'username':''
        }
    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Hasła się nie zgadzają!')
        return data
