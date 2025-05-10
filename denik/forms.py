# denik/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Investice, Transakce, Poznamka

class InvesticeForm(forms.ModelForm):
    class Meta:
        model = Investice
        fields = ['nazev', 'typ', 'ticker', 'mena']

class TransakceForm(forms.ModelForm):
    class Meta:
        model = Transakce
        fields = ['investice', 'datum', 'mnozstvi', 'cena']

class PoznamkaForm(forms.ModelForm):
    class Meta:
        model = Poznamka
        fields = ['investice', 'titulek', 'obsah']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
