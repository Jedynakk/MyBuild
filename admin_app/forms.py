from django import forms
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

from admin_app.models import Budowa, BudowaUpdate, Wydatki, Przetarg, Tag


class AddBudowaForm(forms.ModelForm):

    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        g = Group.objects.get('Kierownicy')
        kierownicy = User.objects.filter(groups=g)
        self.fields['kierownik'].queryset = kierownicy

    class Meta:
        model = Budowa
        fields = ['miasto', 'ulica', 'kod_pocztowy', 'typ', 'podwykonawca', 'budzet', 'kierownik', 'image']
        widgets = {
            'miasto': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'MIASTO'}),
            'ulica': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'ULICA'}),
            'kod_pocztowy': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'KOD POCZTOWY'}),
            'typ': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'TYP BUDOWY'}),
            'podwykonawca': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'PODWYKONAWCA'}),
            'budzet': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'BUDZET'}),
            'kierownik': forms.Select(attrs={'class': 'fieldsy'}),
        }

        labels = {
            "miasto": "MIASTO",
            "ulica": "ULICA",
            "kod_pocztowy": "KOD POCZTOWY",
            "typ": "TYP BUDOWY",
            "podwykonawca": "PODWYKONAWCA",
            "kierownik": "KIEROWNIK",
            "budzet": "BUDZET",
            "image": "ZDJECIE BUDOWY",

        }


class AddWydatkiForm(forms.ModelForm):
    class Meta:
        model = Wydatki
        fields = ['budowa', 'kategoria', 'kwota', 'opis']
        widgets = {
            'budowa': forms.Select(attrs={'class': 'fieldsy', 'placeholder': 'BUDOWA'}),
            'kategoria': forms.Select(attrs={'class': 'fieldsy', 'placeholder': 'KATEGORIA'}),
            'kwota': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'KWOTA'}),
            'opis': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'OPIS'}),

        }

        labels = {
            "budowa": "BUDOWA",
            "kategoria": "KATEGORIA",
            "kwota": "KWOTA",
            "opis": "OPIS",
        }


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
        widgets = {
            'tag': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'TAG'})
        }
        labels = {
            "tag": "TAG",}

class AddPrzetargForm(forms.ModelForm):
    data = forms.DateField(widget=forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'MM/DD/YY'}), label="DATA")

    class Meta:
        model = Przetarg
        fields = ['miasto', 'ulica', 'kod_pocztowy', 'typ_budowy', 'typ_budynku', 'zleceniodawca', 'budzet', 'data',
                  'tags']
        widgets = {
            'miasto': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'MIASTO'}),
            'ulica': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'ULICA'}),
            'kod_pocztowy': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'KOD POCZTOWY'}),
            'typ_budowy': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'TYP BUDOWY'}),
            'typ_budynku': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'TYP BUDYNKU'}),
            'zleceniodawca': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'ZLECENIODAWCA'}),
            'budzet': forms.TextInput(attrs={'class': 'fieldsy', 'placeholder': 'BUDZET'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

        labels = {
            "miasto": "MIASTO",
            "ulica": "ULICA",
            "kod_pocztowy": "KOD POCZTOWY",
            "typ_budowy": "TYP BUDOWY",
            "typ_budynku": "TYP BUDYNKU",
            "zleceniodawca": "ZLECENIODAWCA",
            "budzet": "BUDŻET",

        }
