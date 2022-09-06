import pytest
from django.contrib.auth.models import User, Group


@pytest.fixture
def login_user():
    data = {
        'username': 'ala',
        'password': 'Dupa'
    }
    User.objects.create_user(**data)
    return data

@pytest.fixture
def group():
    kierownicy = Group.objects.create(name="Kierownicy")
    return kierownicy

@pytest.fixture
def user():
    u = User.objects.create(username='testowy')
    return u

