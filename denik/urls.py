# denik/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investice/', views.investice_list, name='investice_list'),
    path('investice/<int:pk>/', views.investice_detail, name='investice_detail'),
]
