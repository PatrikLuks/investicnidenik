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