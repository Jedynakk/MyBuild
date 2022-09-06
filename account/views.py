from audioop import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from account.forms import AddUserForm, LoginForm
from account.models import Kierownicy


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                if request.user.groups.filter(name='Administracja'):
                    return redirect('strona_glowna')
                else:
                    return redirect('main_employee')

        return render(request, 'account/login.html', {'form': LoginForm()})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'account/add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        kierownicy = Group.objects.get(name='Kierownicy')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_staff = False
            user.save()
            user.groups.add(kierownicy)
            return redirect('login')
        return render(request, 'account/add_user.html', {'form': form})

