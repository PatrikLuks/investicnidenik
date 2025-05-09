# denik/models.py
from django.db import models

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

    def __str__(self):
        return f"{self.nazev} ({self.ticker})"


class Transakce(models.Model):
    TYP_TRANS = [
        ('nákup', 'Nákup'),
        ('prodej', 'Prodej'),
    ]

    investice = models.ForeignKey(Investice, on_delete=models.CASCADE, related_name='transakce')
    datum = models.DateField()
    cena_za_jednotku = models.DecimalField(max_digits=10, decimal_places=2)
    mnozstvi = models.DecimalField(max_digits=10, decimal_places=2)
    typ = models.CharField(max_length=10, choices=TYP_TRANS)

    def __str__(self):
        return f"{self.typ.capitalize()} {self.investice.nazev} - {self.datum}"


class Poznamka(models.Model):
    investice = models.ForeignKey(Investice, on_delete=models.CASCADE, related_name='poznamky')
    text = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poznámka k {self.investice.nazev} - {self.datum.strftime('%d.%m.%Y')}"
