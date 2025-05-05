# investicnidenik/models.py
from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Trade(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateField()
    trade_type = models.CharField(max_length=10, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.trade_type} {self.quantity} {self.asset.symbol} on {self.date}"

class Note(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.trade}"

class Investment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateField()

    def __str__(self):
        return f"Investment in {self.asset.name} on {self.date_invested}"
