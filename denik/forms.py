# denik/forms.py
import requests
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

class RealTimeInvesticeForm(forms.Form):
    ASSET_CHOICES = [
        ('stocks', 'Akcie'),
        ('crypto', 'Kryptoměny'),
        ('real_estate', 'Nemovitosti'),
        ('etf', 'ETF'),
    ]

    asset_type = forms.ChoiceField(choices=ASSET_CHOICES, label='Typ investice')
    asset_name = forms.ChoiceField(choices=[], label='Název investice')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset_name'].choices = self.get_real_time_assets()

    def get_real_time_assets(self):
        # Example API integration for stocks and crypto
        assets = []
        try:
            # Fetch stocks (example: Alpha Vantage or Yahoo Finance API)
            stocks_response = requests.get('https://api.example.com/stocks')
            if stocks_response.status_code == 200:
                stocks = stocks_response.json()
                assets.extend([(stock['symbol'], stock['name']) for stock in stocks])

            # Fetch cryptocurrencies (example: CoinGecko API)
            crypto_response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={'vs_currency': 'usd'})
            if crypto_response.status_code == 200:
                cryptos = crypto_response.json()
                assets.extend([(crypto['id'], crypto['name']) for crypto in cryptos])

            # Add static options for real estate and ETFs
            assets.extend([
                ('real_estate_1', 'Nemovitost Praha 1'),
                ('real_estate_2', 'Nemovitost Brno'),
                ('etf_1', 'SPDR S&P 500 ETF'),
                ('etf_2', 'Vanguard Total Stock Market ETF'),
            ])
        except Exception as e:
            print(f"Error fetching assets: {e}")

        return assets
