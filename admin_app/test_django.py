from datetime import datetime

import pytest
from django.urls import reverse

from admin_app.forms import AddBudowaForm, AddPrzetargForm, AddWydatkiForm, AddTagForm


def test_main_page(client):
    url = reverse('strona_glowna')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_main_page_zalogowany(client, user):
    url = reverse('strona_glowna')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_info(client, user):
    url = reverse('user_info', args=(user.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_info_zalogowany(client, user):
    url = reverse('user_info', args=(user.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db
def test_main_update_get(client, user):
    url = reverse('main_update')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_main_update_post(client, user):
    url = reverse('main_update')
    data = {
        'user':user,
        'data':datetime.now().time,
        'text':'ala ma kota'
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_budowa_get(client, user):
    url = reverse('add_budowa')
    response = client.get(url)
    assert response.status_code == 302





@pytest.mark.django_db
def test_add_budowa_post(client, user):
    url = reverse('add_budowa')
    data = {
        "miasto": "krakow",
        "ulica": "wawelska",
        "kod_pocztowy": "01-234",
        "typ": "blok",
        'kierownik': user.id,
        "budzet": "10000",
    }
    client.force_login(user)
    response = client.post(url, data)
    assert response.status_code == 200



@pytest.mark.django_db
def test_budowa_list_get(client, user):
    url = reverse('lista_budowa')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_list(client, user, budowa_list):
    url = reverse('lista_budowa')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(budowa_list)
    for b in budowa_list:
        assert b in response.context['object_list']


@pytest.mark.django_db
def test_budowa_details_niezalogowany(client, user, budowa):
    url = reverse('main_budowa', args=(budowa.id,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_budowa_details_zalogowany(client, user, budowa):
    url = reverse('main_budowa', args=(budowa.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_update_get(client, user, budowa):
    url = reverse('add_updates',  args=(budowa.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_budowa_update_post(client, user, budowa):
    url = reverse('add_updates',  args=(budowa.id,))
    data = {
        'user':user,
        'data':datetime.now().time,
        'text':'ala ma kota'
    }
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_przetarg_get(client, user):
    url = reverse('add_przetarg')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddPrzetargForm)

@pytest.mark.django_db
def test_add_przetarg_user_nie_upr(client, user_bez):
    url = reverse('add_przetarg')
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403



@pytest.mark.django_db
def test_add_przetarg_post(client, user):
    url = reverse('add_przetarg')
    data = {
        'miasto': 'krakow',
        'ulica': 'długa',
        'kod_pocztowy': '01-212',
        'typ_budowy': 'renowacja',
        'typ_budynku': 'basen',
        'zleceniodawca': 'polbud',
        'budzet': 9000,
    }
    client.force_login(user)
    response = client.post(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_przetarg_list(client, user):
    url = reverse('lista_przetarg')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_przetarg_list_list(client, user, przetarg_list):
    url = reverse('lista_przetarg')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(przetarg_list)
    for p in przetarg_list:
        assert p in response.context['object_list']


@pytest.mark.django_db
def test_przetarg_details_niezalogowany(client, user, przetarg):
    url = reverse('main_przetarg', args=(przetarg.id,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_przetarg_details_user_nie_upr(client, user_bez, przetarg):
    url = reverse('main_przetarg', args=(przetarg.id,))
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_przetarg_details_zalogowany(client, user, przetarg):
    url = reverse('main_przetarg', args=(przetarg.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200




@pytest.mark.django_db
def test_add_wydatek_get(client,user, budowa, kategoria):
    url = reverse('add_wydatki')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_wydatek_user_nie_upr(client, user_bez):
    url = reverse('add_wydatki')
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403



@pytest.mark.django_db
def test_add_wydatek_post(client,user, budowa, kategoria):
    url = reverse('add_wydatki')
    data = {
        'budowa':budowa.id,
        'kategoria':'1',
        'kwota':100,
        'opis':'lopaty'
    }
    client.force_login(user)
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_wydatki_niezalogowany(client, user):
    url = reverse('wydatki')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_wydatki_user_nie_upr(client, user_bez):
    url = reverse('wydatki')
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_wydatki_zalogowany(client, user):
    url = reverse('wydatki')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_del_user_niezalogowany(client, user, przetarg):
    url = reverse('del_przetarg',  args=(przetarg.id,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_del_user_nie_upr(client, user_bez, przetarg):
    url = reverse('del_przetarg',  args=(przetarg.id,))
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_del_user_zalogowany(client, user, przetarg):
    url = reverse('del_przetarg', args=(przetarg.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_przetarg_edit_niezalogowany(client, user, przetarg):
    url = reverse('update_przetarg', args=(przetarg.id,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_update_przetarg_user_nie_upr(client, user_bez, przetarg):
    url = reverse('update_przetarg',  args=(przetarg.id,))
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_przetarg_edit_zalogowany(client, user, przetarg):
    url = reverse('update_przetarg', args=(przetarg.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_tag_get(client, user):
    url = reverse('add_tag')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddTagForm)

@pytest.mark.django_db
def test_add_tag_user_nie_upr(client, user_bez):
    url = reverse('add_tag')
    client.force_login(user_bez)
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_przetarg_post(client, user):
    url = reverse('add_tag')
    data = {
        'tag': 'WAAAZNE',
    }
    client.force_login(user)
    response = client.post(url, data)
    assert response.status_code == 302



