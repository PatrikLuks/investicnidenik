from django.shortcuts import render, get_object_or_404
from .models import Investice

def home(request):
    return render(request, 'denik/home.html')

def investice_list(request):
    investice = Investice.objects.all()
    return render(request, 'denik/investice_list.html', {'investice': investice})

def investice_detail(request, pk):
    investice = get_object_or_404(Investice, pk=pk)
    transakce = investice.transakce.all()
    poznamky = investice.poznamky.all()
    return render(request, 'denik/investice_detail.html', {
        'investice': investice,
        'transakce': transakce,
        'poznamky': poznamky,
    })
