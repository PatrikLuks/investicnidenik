# denik/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView

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
    path('investice/chart-data/', views.investice_chart_data, name='investice_chart_data'),
    path('investice/chart/', TemplateView.as_view(template_name='denik/investice_chart.html'), name='investice_chart'),
    path('investice/export-csv/', views.export_investice_csv, name='export_investice_csv'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.user_profile, name='profile'),
    path('accounts/edit-profile/', views.edit_profile, name='edit_profile'),
]

