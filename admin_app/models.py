from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date

wydatki = (
    (1, 'MATERIAŁY'),
    (2, 'NARZĘDZIA'),
    (3, 'PENSJE'),
    (4, 'PODWYKONAWCA'),
    (5, 'ODPADY'),
    (6, 'INNE')
)


class Budowa(models.Model):
    miasto = models.CharField(max_length=128)
    ulica = models.CharField(max_length=128)
    kod_pocztowy = models.CharField(max_length=7)
    typ = models.CharField(max_length=128)
    podwykonawca = models.CharField(max_length=128)
    kierownik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kierownik')
    budzet = models.PositiveIntegerField(default=0)
    users = models.ManyToManyField(User)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def get_absolute_url(self):
        return reverse('update_budowa', args=(self.id,))

    def __str__(self):
        return f"{self.miasto} {self.ulica}"


class Tag(models.Model):
    tag = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.tag}"

class Przetarg(models.Model):
    miasto = models.CharField("MIASTO",max_length=128)
    ulica = models.CharField("ULICA", max_length=128)
    kod_pocztowy = models.CharField("KOD POCZTOWY", max_length=128)
    typ_budowy = models.CharField("TYP BUDOWLI", max_length=128)
    typ_budynku = models.CharField("TYP BUDYNKU", max_length=128)
    zleceniodawca = models.CharField("ZLECENIODAWCA", max_length=128)
    budzet = models.PositiveIntegerField("BUDŻET", default=None)
    data = models.DateField("DATA", auto_now_add=False, auto_now=False, blank=True, null=True)
    dodanie = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)


    def get_absolute_url(self):
        return reverse('update_przetarg', args=(self.id, ))


class MainUpdate(models.Model):
    text = models.CharField(max_length=256)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BudowaUpdate(models.Model):
    text = models.CharField(max_length=256)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budowa = models.ForeignKey(Budowa, on_delete=models.CASCADE)


class Wydatki(models.Model):
    kategoria = models.IntegerField(choices=wydatki, default=0)
    kwota = models.PositiveIntegerField(default=None)
    budowa = models.ForeignKey(Budowa, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    opis = models.CharField(max_length=256)


