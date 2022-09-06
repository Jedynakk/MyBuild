

from django.contrib import admin
from django.urls import path

from employee_app import views

urlpatterns = [
    path('main_employee/', views.MainEmployeeView.as_view(), name='main_employee'),
    path('main_employee/update/', views.AddMainUpdateView.as_view(), name='add_update'),
    path('budowa/', views.Lista_Budowa.as_view(), name='budowy'),
    path('budowa/<int:id>', views.BudowaView.as_view(), name='budowa_details'),
    path('budowa/<int:id>/add_update/', views.AddUpdateView.as_view(), name='add_updates_em'),

]