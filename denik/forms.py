# denik/forms.py
from django import forms
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
