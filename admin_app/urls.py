from django.contrib import admin
from django.urls import path

from admin_app import views

urlpatterns = [
    path('main_admin/', views.MainPageView.as_view(), name='strona_glowna'),
    path('main_admin/add_update/', views.AddMainUpdateView.as_view(), name='main_update'),
    path('add_budowa/', views.AddBudowaView.as_view(), name='add_budowa'),
    path('lista_budowa/', views.ListaBudowaView.as_view(), name='lista_budowa'),
    path('budowa/<int:id>/', views.BudowaView.as_view(), name='main_budowa'),
    path('budowa/<int:id>/add_update/', views.AddUpdateView.as_view(), name='add_updates'),
    path('budowa/<int:id>/add_wydatek/', views.AddWydatkiView.as_view(), name='add_wydatki'),

    path('add_przetarg/', views.AddPrzetargView.as_view(), name='add_przetarg'),
    path('lista_przetarg/', views.ListaPrzetargView.as_view(), name='lista_przetarg'),
    path('przetarg/<int:id>/', views.PrzetargView.as_view(), name='main_przetarg'),
    path('przetarg/<int:id>/delete/', views.DelPrzetargView.as_view(), name='del_przetarg'),
    path('update_przetarg/<int:pk>/', views.PrzetargUpdateView.as_view(), name='update_przetarg'),

    path('add_wydatki/', views.AddWydatkiView.as_view(), name='add_wydatki'),
    path('wydatki/', views.WydatkiView.as_view(), name='wydatki'),

    path('user/<int:id>', views.UserView.as_view(), name='user_info'),
    path('add_tag/', views.AddTagView.as_view(), name='add_tag')
]
