# denik/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investice/', views.investice_list, name='investice_list'),
    path('investice/<int:pk>/', views.investice_detail, name='investice_detail'),
    path('transakce/edit/<int:transakce_id>/', views.edit_transakce, name='edit_transakce'),
    path('transakce/delete/<int:transakce_id>/', views.delete_transakce, name='delete_transakce'),
    path('poznamka/edit/<int:poznamka_id>/', views.edit_poznamka, name='edit_poznamka'),
    path('poznamka/delete/<int:poznamka_id>/', views.delete_poznamka, name='delete_poznamka'),
    # Další cesty
]
