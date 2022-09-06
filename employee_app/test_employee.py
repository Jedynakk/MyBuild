from datetime import datetime

from django.urls import reverse

import pytest


def test_main_page(client):
    url = reverse('main_employee')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_main_page_zalogowany(client, user):
    url = reverse('main_employee')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_list_niezlogowany(client):
    url = reverse('budowy')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_budowa_list_zalogowany(client, user):
    url = reverse('budowy')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_details_niezlogowany(client, budowa):
    url = reverse('budowa_details', args=(budowa.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_budowa_details_zalogowany(client, user, budowa):
    url = reverse('budowa_details', args=(budowa.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_update_get(client, user, budowa):
    url = reverse('add_updates_em',  args=(budowa.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_update_post(client, user, budowa):
    url = reverse('add_updates_em',  args=(budowa.id,))
    data = {
        'user':user,
        'data':datetime.now().time,
        'text':'ala ma kota'
    }
    response = client.post(url, data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_main_update_get(client, user):
    url = reverse('add_update')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_main_update_post(client, user):
    url = reverse('add_update')
    data = {
        'user':user,
        'data':datetime.now().time,
        'text':'ala ma kota'
    }
    response = client.post(url, data)
    assert response.status_code == 302