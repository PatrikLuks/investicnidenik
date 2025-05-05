import yfinance as yf
from django.shortcuts import render
import json

def chart_kb(request):
    ticker = yf.Ticker("KOMB.PR")  # Symbol pro Komerční banku na Yahoo Finance
    hist = ticker.history(period="6mo")  # Historie za posledních 6 měsíců
    dates = hist.index.strftime('%Y-%m-%d').tolist()
    prices = hist['Close'].tolist()

    context = {
        'dates': json.dumps(dates),
        'prices': json.dumps(prices),
    }
    return render(request, 'chart_kb.html', context)

def home(request):
    return render(request, 'home.html')

def asset_list(request):
    return render(request, 'assets.html')

def trade_list(request):
    return render(request, 'trades.html')

def note_list(request):
    return render(request, 'notes.html')

def investment_list(request):
    return render(request, 'investments.html')
