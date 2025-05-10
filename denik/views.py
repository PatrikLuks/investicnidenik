from django.shortcuts import render, get_object_or_404, redirect
from .models import Investice, Transakce, Poznamka, Obchod  # Odstraněn neplatný model `Aktivum`
from .forms import InvesticeForm, TransakceForm, PoznamkaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Úvodní stránka
def home(request):
    return render(request, 'denik/home.html')

# Seznam investic
def investice_list(request):
    query = request.GET.get('q')
    typ_filter = request.GET.get('typ')
    investice = Investice.objects.all()

    if query:
        investice = investice.filter(Q(nazev__icontains=query) | Q(ticker__icontains=query))
    if typ_filter:
        investice = investice.filter(typ=typ_filter)

    return render(request, 'denik/investice_list.html', {'investice_list': investice, 'query': query, 'typ_filter': typ_filter})

# Detail investice
def investice_detail(request, pk):
    investice = get_object_or_404(Investice, pk=pk)
    transakce = Transakce.objects.filter(investice=investice)
    poznamky = Poznamka.objects.filter(investice=investice)

    return render(request, 'denik/investice_detail.html', {
        'investice': investice,
        'transakce': transakce,
        'poznamky': poznamky,
    })

# Přidání investice
def add_investice(request):
    if request.method == 'POST':
        form = InvesticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investice_list')
    else:
        form = InvesticeForm()
    return render(request, 'denik/add_investice.html', {'form': form})

# Přidání transakce
def add_transakce(request):
    if request.method == 'POST':
        form = TransakceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investice_list')
    else:
        form = TransakceForm()
    return render(request, 'denik/add_transakce.html', {'form': form})

# Přidání poznámky
def add_poznamka(request):
    if request.method == 'POST':
        form = PoznamkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investice_list')
    else:
        form = PoznamkaForm()
    return render(request, 'denik/add_poznamka.html', {'form': form})

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

def edit_transakce(request, pk):
    transakce = get_object_or_404(Transakce, pk=pk)
    if request.method == 'POST':
        form = TransakceForm(request.POST, instance=transakce)
        if form.is_valid():
            form.save()
            return redirect('investice_detail', pk=transakce.investice.pk)
    else:
        form = TransakceForm(instance=transakce)
    return render(request, 'denik/edit_transakce.html', {'form': form, 'transakce': transakce})

def delete_transakce(request, pk):
    transakce = get_object_or_404(Transakce, pk=pk)
    if request.method == 'POST':
        transakce.delete()
        return redirect('investice_detail', pk=transakce.investice.pk)
    return render(request, 'denik/delete_transakce.html', {'transakce': transakce})

def edit_poznamka(request, pk):
    poznamka = get_object_or_404(Poznamka, pk=pk)
    if request.method == 'POST':
        form = PoznamkaForm(request.POST, instance=poznamka)
        if form.is_valid():
            form.save()
            return redirect('investice_detail', pk=poznamka.investice.pk)
    else:
        form = PoznamkaForm(instance=poznamka)
    return render(request, 'denik/edit_poznamka.html', {'form': form, 'poznamka': poznamka})

def delete_poznamka(request, pk):
    poznamka = get_object_or_404(Poznamka, pk=pk)
    if request.method == 'POST':
        poznamka.delete()
        return redirect('investice_detail', pk=poznamka.investice.pk)
    return render(request, 'denik/delete_poznamka.html', {'poznamka': poznamka})

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

# Editace investice
def edit_investice(request, pk):
    investice = get_object_or_404(Investice, pk=pk)
    if request.method == 'POST':
        form = InvesticeForm(request.POST, instance=investice)
        if form.is_valid():
            form.save()
            return redirect('investice_detail', pk=investice.pk)
    else:
        form = InvesticeForm(instance=investice)
    return render(request, 'denik/edit_investice.html', {'form': form, 'investice': investice})

# Smazání investice
def delete_investice(request, pk):
    investice = get_object_or_404(Investice, pk=pk)
    if request.method == 'POST':
        investice.delete()
        return redirect('investice_list')
    return render(request, 'denik/delete_investice.html', {'investice': investice})