from django.shortcuts import render, get_object_or_404, redirect
from .models import Investice, Transakce, Poznamka, Obchod, UserActivityLog, Notification  # Odstraněn neplatný model `Aktivum`
from .forms import InvesticeForm, TransakceForm, PoznamkaForm, UserRegisterForm, UserUpdateForm, RealTimeInvesticeForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
import csv
from plotly.offline import plot
from plotly.graph_objs import Scatter
import requests
import logging

logger = logging.getLogger(__name__)

def is_admin(user):
    return user.groups.filter(name='Administrators').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    logs = UserActivityLog.objects.all().order_by('-timestamp')[:50]
    return render(request, 'denik/admin_dashboard.html', {'logs': logs})

# Úvodní stránka
def home(request):
    return render(request, 'denik/home.html')

def log_user_activity(user, action):
    UserActivityLog.objects.create(user=user, action=action)

# Seznam investic
@login_required
def investice_list(request):
    if request.method == 'POST':
        form = RealTimeInvesticeForm(request.POST)
        if form.is_valid():
            asset_type = form.cleaned_data['asset_type']
            asset_name = form.cleaned_data['asset_name']
            Investice.objects.create(
                nazev=asset_name,
                typ=asset_type,
                uzivatel=request.user
            )
            return redirect('investice_list')
    else:
        form = RealTimeInvesticeForm()

    # Fetch real market data for various asset types
    stocks = []
    etfs = []
    cryptos = []
    real_estate = []
    try:
        # Fetch stocks
        stock_response = requests.get('https://api.example.com/stocks', params={
            'currency': 'usd',
            'limit': 10
        })
        if stock_response.status_code == 200:
            stocks = stock_response.json()

        # Fetch ETFs
        etf_response = requests.get('https://api.example.com/etfs', params={
            'currency': 'usd',
            'limit': 10
        })
        if etf_response.status_code == 200:
            etfs = etf_response.json()

        # Fetch cryptocurrencies
        crypto_response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False
        })
        if crypto_response.status_code == 200:
            cryptos = crypto_response.json()

        # Fetch real estate data (mocked example)
        real_estate = [
            {'name': 'Nemovitost A', 'symbol': 'REAL1', 'current_price': 500000},
            {'name': 'Nemovitost B', 'symbol': 'REAL2', 'current_price': 750000}
        ]

    except requests.RequestException as e:
        print(f"Error fetching market data: {e}")

    investice_list = Investice.objects.filter(uzivatel=request.user)
    return render(request, 'denik/investice_list.html', {
        'investice_list': investice_list,
        'form': form,
        'stocks': stocks,
        'etfs': etfs,
        'cryptos': cryptos,
        'real_estate': real_estate
    })

# Detail investice
@login_required
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
@login_required
def add_investice(request):
    if request.method == 'POST':
        form = RealTimeInvesticeForm(request.POST)
        if form.is_valid():
            # Process the selected asset and save it as an investment
            asset_type = form.cleaned_data['asset_type']
            asset_name = form.cleaned_data['asset_name']
            Investice.objects.create(
                nazev=asset_name,
                typ=asset_type,
                uzivatel=request.user
            )
            return redirect('investice_list')
    else:
        form = RealTimeInvesticeForm()

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

def investice_chart_data(request):
    data = Investice.objects.values('typ').annotate(total=Sum('cena')).order_by('typ')
    chart_data = {
        'labels': [item['typ'] for item in data],
        'data': [item['total'] for item in data],
    }
    return JsonResponse(chart_data)

@login_required
def investice_chart(request, investice_id):
    investice = get_object_or_404(Investice, id=investice_id)
    transakce = Transakce.objects.filter(investice=investice).order_by('datum')

    # Prepare data for the chart
    dates = [t.datum for t in transakce]
    prices = [t.cena for t in transakce]

    # Create a Plotly scatter plot
    scatter = Scatter(x=dates, y=prices, mode='lines+markers', name='Cena investice')
    layout = {
        'title': f'Vývoj ceny investice: {investice.nazev}',
        'xaxis': {'title': 'Datum'},
        'yaxis': {'title': 'Cena'},
    }
    plot_div = plot({'data': [scatter], 'layout': layout}, output_type='div')

    return render(request, 'denik/investice_chart.html', {'plot_div': plot_div, 'investice': investice})

def export_investice_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="investice.csv"'

    writer = csv.writer(response)
    writer.writerow(['Název', 'Typ', 'Měna', 'Popis'])

    investice = Investice.objects.all()
    for item in investice:
        writer.writerow([item.nazev, item.typ, item.mena, item.popis])

    return response

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

def simulace_rustu(request, pk):
    investice = get_object_or_404(Investice, pk=pk)
    # Simulace růstu investice (příklad logiky)
    simulace_data = {
        'investice': investice,
        'simulace': [
            {'rok': i, 'hodnota': investice.cena * (1 + 0.05) ** i} for i in range(1, 11)
        ]
    }
    return render(request, 'denik/simulace_graf.html', simulace_data)

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'denik/notifications.html', {'notifications': user_notifications})