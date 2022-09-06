import pytest
from django.contrib.auth.models import User, Permission

from admin_app.models import Budowa, Przetarg


@pytest.fixture
def user():
    u = User.objects.create(username='testowy')
    permission = Permission.objects.get(codename='view_logentry')
    permission2 = Permission.objects.get(codename='add_budowa')
    permission3 = Permission.objects.get(codename='view_budowa')
    permission4 = Permission.objects.get(codename='add_budowaupdate')
    permission5 = Permission.objects.get(codename='add_przetarg')
    permission6 = Permission.objects.get(codename='view_przetarg')
    permission7 = Permission.objects.get(codename='add_wydatki')
    permission8 = Permission.objects.get(codename='view_wydatki')
    permission9 = Permission.objects.get(codename='change_przetarg')
    permission10 = Permission.objects.get(codename='delete_przetarg')
    permission11 = Permission.objects.get(codename='add_tag')
    u.user_permissions.add(permission3)
    u.user_permissions.add(permission)
    u.user_permissions.add(permission2)
    u.user_permissions.add(permission4)
    u.user_permissions.add(permission5)
    u.user_permissions.add(permission6)
    u.user_permissions.add(permission7)
    u.user_permissions.add(permission8)
    u.user_permissions.add(permission9)
    u.user_permissions.add(permission10)
    u.user_permissions.add(permission11)
    return u

@pytest.fixture
def user_bez():
    u = User.objects.create(username='testowy')
    return u


@pytest.fixture
def budowa(user):
    b = Budowa.objects.create(miasto="krakow", ulica="wawelska", kod_pocztowy="01-234",
                              typ="blok", kierownik=user, budzet="10000")
    return b


@pytest.fixture
def budowa_list(user):
    lst = []
    b = Budowa()
    b.miasto = "gdansl"
    b.ulica = "prosta"
    b.typ = 'blok'
    b.budzet = 100
    b.kod_pocztowy = '12-122'
    b.podwykonawca = 'polbud'
    b.kierownik = user
    b.save()
    lst.append(b)
    return lst


@pytest.fixture
def przetarg_list(user):
    lst = []
    p = Przetarg()
    p.miasto = "gdansl"
    p.ulica = "prosta"
    p.typ_budynku = 'blok'
    p.typ_budowy = 'blok'
    p.budzet = 100
    p.kod_pocztowy = '12-122'
    p.zleceniodawca = 'polbud'
    p.save()
    lst.append(p)
    return lst


@pytest.fixture
def przetarg():
    p = Przetarg.objects.create(miasto="krakow", ulica="wawelska", kod_pocztowy="01-234",
                                typ_budynku="blok", typ_budowy='rekonstrukcja', budzet="10000", zleceniodawca='polbud')
    return p


@pytest.fixture
def kategoria():
    kateogrie = ((1, 'MATERIAŁY'),
                (2, 'NARZĘDZIA'),
                (3, 'PENSJE'),
                (4, 'PODWYKONAWCA'),
                (5, 'ODPADY'),
                (6, 'INNE'))

    return kateogrie