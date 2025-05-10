from django.shortcuts import render, get_object_or_404
from .models import Investice
from django.shortcuts import render, redirect
from .models import Investice, Transakce
from .forms import TransakceForm
from .models import Poznamka
from .forms import PoznamkaForm
from django.shortcuts import render, get_object_or_404
from .models import Investice, Transakce, Poznamka
from .forms import TransakceForm
from django.http import HttpResponseRedirect
from .forms import PoznamkaForm
from django.shortcuts import render
from .models import Aktivum  # Pokud máš model Aktivum
from .models import Obchod
from .models import Poznamka


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

def add_transakce(request, investice_id):
    investice = Investice.objects.get(id=investice_id)
    if request.method == 'POST':
        form = TransakceForm(request.POST)
        if form.is_valid():
            transakce = form.save(commit=False)
            transakce.investice = investice
            transakce.save()
            return redirect('investice_detail', investice_id=investice.id)
    else:
        form = TransakceForm()

    return render(request, 'denik/add_transakce.html', {'form': form, 'investice': investice})
    

    def add_poznamka(request, investice_id):
    investice = Investice.objects.get(id=investice_id)
    if request.method == 'POST':
        form = PoznamkaForm(request.POST)
        if form.is_valid():
            poznamka = form.save(commit=False)
            poznamka.investice = investice
            poznamka.save()
            return redirect('investice_detail', investice_id=investice.id)
    else:
        form = PoznamkaForm()

    return render(request, 'denik/add_poznamka.html', {'form': form, 'investice': investice})

    def investice_detail(request, investice_id):
    investice = get_object_or_404(Investice, id=investice_id)
    transakce = Transakce.objects.filter(investice=investice)
    poznamky = Poznamka.objects.filter(investice=investice)
    
    return render(request, 'denik/investice_detail.html', {
        'investice': investice,
        'transakce': transakce,
        'poznamky': poznamky,
    })

    def edit_transakce(request, transakce_id):
    transakce = get_object_or_404(Transakce, id=transakce_id)
    if request.method == 'POST':
        form = TransakceForm(request.POST, instance=transakce)
        if form.is_valid():
            form.save()
            return redirect('investice_detail', investice_id=transakce.investice.id)
    else:
        form = TransakceForm(instance=transakce)
    
    return render(request, 'denik/edit_transakce.html', {'form': form, 'transakce': transakce})

    def delete_transakce(request, transakce_id):
    transakce = get_object_or_404(Transakce, id=transakce_id)
    investice_id = transakce.investice.id
    transakce.delete()
    return HttpResponseRedirect(reverse('investice_detail', args=[investice_id]))

    def edit_poznamka(request, poznamka_id):
    poznamka = get_object_or_404(Poznamka, id=poznamka_id)
    if request.method == 'POST':
        form = PoznamkaForm(request.POST, instance=poznamka)
        if form.is_valid():
            form.save()
            return redirect('investice_detail', investice_id=poznamka.investice.id)
    else:
        form = PoznamkaForm(instance=poznamka)
    
    return render(request, 'denik/edit_poznamka.html', {'form': form, 'poznamka': poznamka})

    # denik/views.py
def delete_poznamka(request, poznamka_id):
    poznamka = get_object_or_404(Poznamka, id=poznamka_id)
    investice_id = poznamka.investice.id
    poznamka.delete()
    return HttpResponseRedirect(reverse('investice_detail', args=[investice_id]))


def seznam_aktiv(request):
    # Pokud už máš model pro aktiva, tak načteme všechna aktiva
    aktiva = Aktivum.objects.all()
    return render(request, 'denik/seznam_aktiv.html', {'aktiva': aktiva})

def obchody_list(request):
    return render(request, 'denik/obchody_list.html')

def poznamky_list(request):
    return render(request, 'denik/poznamky_list.html')

def obchod_list(request):
    obchody = Obchod.objects.all()
    return render(request, 'denik/obchod_list.html', {'obchody': obchody})

def poznamka_list(request):
    poznamky = Poznamka.objects.all()
    return render(request, 'denik/poznamka_list.html', {'poznamky': poznamky})