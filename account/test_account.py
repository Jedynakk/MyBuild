import pytest
from django.contrib.auth.models import User, Group
from django.urls import reverse

from account.forms import LoginForm, AddUserForm


def test_login_view_get(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, LoginForm)


@pytest.mark.django_db
def test_login_view_post(client, login_user):
    url = reverse('login')
    response = client.post(url, login_user)
    assert response.status_code == 302


def test_add_user_get(client):
    url = reverse('add_user')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddUserForm)


@pytest.mark.django_db
def test_add_user_post(client, group):
    url = reverse('add_user')
    data = {
        'username': 'dupa',
        'first_name': 'Jan',
        'last_name': 'Testowy',
        'password1':'Dupa',
        'password2':'Dupa',
    }
    response = client.post(url, data)
    assert response.status_code == 302



@pytest.mark.django_db
def test_logout_get_nie_zalogowany(client, user):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))



@pytest.mark.django_db
def test_przetarg_edit_zalogowany(client, user):
    url = reverse('logout')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302
