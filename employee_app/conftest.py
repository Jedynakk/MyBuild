import pytest
from django.contrib.auth.models import User

from admin_app.models import Budowa


@pytest.fixture
def user():
    u = User.objects.create(username='testowy')
    return u


@pytest.fixture
def budowa(user):
    b = Budowa.objects.create(miasto="krakow", ulica="wawelska", kod_pocztowy="01-234",
                              typ="blok", kierownik=user, budzet="10000")
    return b

