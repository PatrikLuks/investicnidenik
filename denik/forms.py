# denik/forms.py
from django import forms
from .models import Transakce
from .models import Poznamka
class PoznamkaForm(forms.ModelForm):
    class Meta:
        model = Poznamka
        fields = ['text', 'investice']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

class TransakceForm(forms.ModelForm):
    class Meta:
        model = Transakce
        fields = ['datum', 'typ', 'mnozstvi', 'cena_za_jednotku', 'investice']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
        }
