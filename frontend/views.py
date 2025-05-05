from django.shortcuts import render
from investicnidenik.models import Asset, Trade, Note, Investment

def home(request):
    assets = Asset.objects.all()
    trades = Trade.objects.all()
    notes = Note.objects.all()
    investments = Investment.objects.all()

    return render(request, 'frontend/home.html', {
        'assets': assets,
        'trades': trades,
        'notes': notes,
        'investments': investments,
    })
