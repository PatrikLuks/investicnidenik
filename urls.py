from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_objektů, name='seznam_objektů'),
    path('detail/<int:id>/', views.detail_objektu, name='detail_objektu'),
]
