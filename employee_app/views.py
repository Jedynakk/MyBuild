from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from admin_app.models import Budowa, BudowaUpdate, MainUpdate


class MainEmployeeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'employee_app/base.html',{'update': MainUpdate.objects.all().order_by('data')})


class Lista_Budowa(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        budowy = Budowa.objects.filter(kierownik_id=user)
        return render(request, 'employee_app/lista_budowa.html', {'budowy': budowy})


class BudowaView(LoginRequiredMixin, View):
    def get(self, request, id):
        return render(request, 'employee_app/budowa.html', {'budowa': Budowa.objects.get(pk=id)})

class AddUpdateView(LoginRequiredMixin, View):
    def get(self, reqeust, id):
        return render(reqeust, 'admin_app/updaty/add_update.html', {'budowa': Budowa.objects.get(pk=id)})

    def post(self, request, id):
        budowa = Budowa.objects.get(pk=id)
        user = request.user
        data = datetime.now().time
        text = request.POST['text']
        BudowaUpdate.objects.create(budowa=budowa, user=user, data=data, text=text)
        return redirect('budowa_details', id)

class AddMainUpdateView(LoginRequiredMixin, View):
    def get(self, reqeust):
        return render(reqeust, 'admin_app/updaty/add_update.html')

    def post(self, request):
        user = request.user
        data = datetime.now().time
        text = request.POST['text']
        MainUpdate.objects.create(user=user, data=data, text=text)
        return redirect('main_employee')

