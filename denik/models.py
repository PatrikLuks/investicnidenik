# denik/models.py
from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.timezone import now
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Investice(models.Model):
    TYPY = [
        ('akcie', 'Akcie'),
        ('etf', 'ETF'),
        ('krypto', 'Kryptoměna'),
        ('nemovitost', 'Nemovitost'),
        ('jine', 'Jiné'),
    ]

    nazev = models.CharField(max_length=100)
    typ = models.CharField(max_length=20, choices=TYPY)
    ticker = models.CharField(max_length=20, blank=True, null=True)
    mena = models.CharField(max_length=10, default='CZK')
    popis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nazev} ({self.ticker})"


class Transakce(models.Model):
    investice = models.ForeignKey(Investice, on_delete=models.CASCADE, related_name='transakce')
    datum = models.DateField()
    mnozstvi = models.DecimalField(max_digits=10, decimal_places=2)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.investice.nazev} - {self.datum}"


class Poznamka(models.Model):
    investice = models.ForeignKey(Investice, on_delete=models.CASCADE, related_name='poznamky')
    titulek = models.CharField(max_length=100)
    obsah = models.TextField()
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulek


class Obchod(models.Model):
    aktivum = models.ForeignKey(Investice, on_delete=models.CASCADE, related_name='obchody')
    mnozstvi = models.DecimalField(max_digits=10, decimal_places=2)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    datum = models.DateField()

    def __str__(self):
        return f"{self.aktivum.nazev} - {self.datum}"


class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


def create_default_groups():
    Group.objects.get_or_create(name='Administrators')
    Group.objects.get_or_create(name='Regular Users')


@receiver(post_migrate)
def create_sample_data(sender, **kwargs):
    if sender.name == 'denik':
        investice1 = Investice.objects.get_or_create(nazev='Apple', typ='akcie', ticker='AAPL', mena='USD', popis='Technologická společnost')[0]
        investice2 = Investice.objects.get_or_create(nazev='Bitcoin', typ='krypto', ticker='BTC', mena='USD', popis='Kryptoměna')[0]

        Transakce.objects.get_or_create(investice=investice1, datum='2025-01-01', mnozstvi=10, cena=150)
        Transakce.objects.get_or_create(investice=investice2, datum='2025-02-01', mnozstvi=0.5, cena=30000)

        Poznamka.objects.get_or_create(investice=investice1, titulek='Poznámka k Apple', obsah='Sledovat vývoj akcií.')
        Poznamka.objects.get_or_create(investice=investice2, titulek='Poznámka k Bitcoinu', obsah='Zvážit dlouhodobou investici.')