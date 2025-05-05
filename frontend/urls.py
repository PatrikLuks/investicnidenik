from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart_kb/', views.chart_kb, name='chart_kb'),
    path('assets/', views.asset_list, name='asset_list'),
    path('trades/', views.trade_list, name='trade_list'),
    path('notes/', views.note_list, name='note_list'),
    path('investments/', views.investment_list, name='investment_list'),
]
