from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, UpdateView
from admin_app.forms import AddBudowaForm, AddPrzetargForm, AddWydatkiForm, AddTagForm
from admin_app.models import Budowa, BudowaUpdate, Przetarg, Wydatki, MainUpdate, wydatki


class MainPageView(PermissionRequiredMixin, View):
    permission_required = ['admin.view_logentry']

    def get(self, request):
        employees = User.objects.filter(groups__name='Kierownicy')
        lista = Wydatki.objects.all()
        suma = 0
        for i in lista:
            suma += i.kwota

        return render(request, 'admin_app/mains/main.html',
                      {'update': MainUpdate.objects.all().order_by('data'),
                       'suma': suma, 'wydatki': lista, 'employees': employees})


class UserView(LoginRequiredMixin, View):
    def get(self, request, id):
        return render(request, 'admin_app/mains/user_info.html',
                      {'kiero': User.objects.get(pk=id)})

    def post(self, request, id):
        kiero = User.objects.get(id=id)
        admini = Group.objects.get(name='Administracja')
        kierownicy = Group.objects.get(name='Kierownicy')
        kierownicy.user_set.remove(kiero)
        admini.user_set.add(kiero)
        kiero.is_staff = True
        return redirect('strona_glowna')


class AddMainUpdateView(LoginRequiredMixin, View):
    def get(self, reqeust):
        return render(reqeust, 'admin_app/updaty_main/add_main_update.html')

    def post(self, request):
        user = request.user
        data = datetime.now().time
        text = request.POST['text']
        if text == '':
            return HttpResponse('Nie mozesz dodac pustego wpisu')
        MainUpdate.objects.create(user=user, data=data, text=text)
        return redirect('strona_glowna')


class AddBudowaView(PermissionRequiredMixin, View):
    permission_required = ['admin_app.add_budowa']

    def get(self, request):
        form = AddBudowaForm()
        g = Group.objects.get(name='Kierownicy')
        users = User.objects.filter(groups=g)
        form.fields['kierownik'].queryset = users
        return render(request, 'admin_app/budowa/add_budowa.html', {'form': form})

    def post(self, request):
        form = AddBudowaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_budowa')
        return render(request, 'admin_app/budowa/add_budowa.html', {'form': form})


class ListaBudowaView(PermissionRequiredMixin, ListView):
    permission_required = ['admin_app.view_budowa']
    model = Budowa
    template_name = 'admin_app/budowa/lista_budowa.html'
    context_object_name = 'lista_budowa_list'


class BudowaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.view_budowa']

    def get(self, request, id):
        budowa = Budowa.objects.get(pk=id)
        lista = Wydatki.objects.all()
        lista = lista.filter(budowa=budowa)
        data = lista
        suma = 0
        for i in data:
            suma += i.kwota

        return render(request, 'admin_app/budowa/budowa.html',
                      {'budowa': Budowa.objects.get(pk=id), 'suma': suma})


class AddUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.add_budowaupdate']

    def get(self, reqeust, id):
        return render(reqeust, 'admin_app/updaty/add_update.html', {'budowa': Budowa.objects.get(pk=id)})

    def post(self, request, id):
        budowa = Budowa.objects.get(pk=id)
        user = request.user
        data = datetime.now().time
        text = request.POST['text']
        if text == '':
            return HttpResponse('Nie możesz dodać pustego wpisu')
        BudowaUpdate.objects.create(budowa=budowa, user=user, data=data, text=text)
        return redirect('main_budowa', id)


class AddPrzetargView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.add_przetarg']

    def get(self, request):
        form = AddPrzetargForm()
        return render(request, 'admin_app/przetargi/add_przetarg.html', {'form': form})

    def post(self, request):
        form = AddPrzetargForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_przetarg')
        return render(request, 'admin_app/mains/add.html', {'form': form})


class ListaPrzetargView(LoginRequiredMixin, ListView):
    model = Przetarg
    template_name = 'admin_app/przetargi/lista_przetarg.html'
    context_object_name = 'przetarg_lista'


class PrzetargView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.view_przetarg']

    def get(self, request, id):
        return render(request, 'admin_app/przetargi/przetarg_details.html', {'przetarg': Przetarg.objects.get(pk=id)})


class DelPrzetargView(PermissionRequiredMixin, View):
    permission_required = ['admin_app.delete_przetarg']

    def get(self, request, id):
        return render(request, 'admin_app/przetargi/del_przetarg.html',
                      {'przetarg': Przetarg.objects.get(pk=id)})

    def post(self, request, id):
        if request.POST['potwierdzenie'] == 'tak':
            p = Przetarg.objects.get(pk=id)
            p.delete()
        return redirect('lista_przetarg')


class PrzetargUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['admin_app.change_przetarg']

    model = Przetarg
    template_name = 'admin_app/przetargi/update_przetarg.html'
    fields = ['miasto', 'ulica', 'kod_pocztowy', 'typ_budowy', 'typ_budynku', 'zleceniodawca', 'budzet', 'data']

    def get_success_url(self):
        super().get_success_url()
        return reverse("lista_przetarg")


class AddWydatkiView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.add_wydatki']

    def get(self, request):
        form = AddWydatkiForm()
        return render(request, 'admin_app/wydatki/add_wydatki.html', {'form': form})

    def post(self, request):
        form = AddWydatkiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wydatki')
        return render(request, 'admin_app/mains/add.html', {'form': form})


class WydatkiView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ['admin_app.view_wydatki']

    def get(self, request):
        kategoria = request.GET.get('kategoria', '0')
        lista = Wydatki.objects.all()
        if kategoria != '0':
            lista = lista.filter(kategoria=kategoria)
        data = lista
        suma = 0
        for i in data:
            suma += i.kwota
        return render(request, 'admin_app/wydatki/wydatki.html',
                      {'wydatki': lista, 'kategoria': wydatki, 'suma': suma})


class AddTagView(PermissionRequiredMixin, View):
    permission_required = ['admin_app.add_tag']
    def get(self, request):
        form = AddTagForm()
        return render(request, 'admin_app/przetargi/add_tag.html', {'form': form})

    def post(self, request):
        form = AddTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_przetarg')
        return render(request, 'admin_app/przetargi/add_tag.html', {'form': form})
