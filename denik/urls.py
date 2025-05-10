# denik/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investice/', views.investice_list, name='investice_list'),
    path('investice/<int:pk>/', views.investice_detail, name='investice_detail'),
    path('investice/<int:pk>/edit/', views.edit_investice, name='edit_investice'),
    path('investice/<int:pk>/delete/', views.delete_investice, name='delete_investice'),
    path('poznamka/<int:pk>/edit/', views.edit_poznamka, name='edit_poznamka'),
    path('poznamka/<int:pk>/delete/', views.delete_poznamka, name='delete_poznamka'),
    # path('seznam_aktiv/', views.seznam_aktiv, name='seznam_aktiv'),  # Odstraněno, protože pohled neexistuje
    path('obchody/', views.obchody_list, name='obchody_list'),
    path('poznamky/', views.poznamky_list, name='poznamky_list'),
    path('investice/add/', views.add_investice, name='add_investice'),
    path('transakce/add/', views.add_transakce, name='add_transakce'),
    path('poznamka/add/', views.add_poznamka, name='add_poznamka'),
    path('transakce/<int:pk>/edit/', views.edit_transakce, name='edit_transakce'),
    path('transakce/<int:pk>/delete/', views.delete_transakce, name='delete_transakce'),
]

