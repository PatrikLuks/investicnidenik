# test_data.py

import datetime
from denik.models import Asset, Trade, Note, Investment

# Odstranění starých testovacích dat
Note.objects.all().delete()
Trade.objects.all().delete()
Investment.objects.all().delete()
Asset.objects.all().delete()

# Vytvoření aktiv
assets = [
    Asset.objects.create(name="Apple", asset_type="Stock", symbol="AAPL", current_price=174.32),
    Asset.objects.create(name="Tesla", asset_type="Stock", symbol="TSLA", current_price=712.50),
    Asset.objects.create(name="Bitcoin", asset_type="Crypto", symbol="BTC", current_price=38000.00),
    Asset.objects.create(name="Ethereum", asset_type="Crypto", symbol="ETH", current_price=2600.00),
    Asset.objects.create(name="Amazon", asset_type="Stock", symbol="AMZN", current_price=3450.00),
]

# Vytvoření obchodů (Trades)
trades = []
for asset in assets:
    trades.append(Trade.objects.create(asset=asset, date=datetime.date(2024, 5, 1), trade_type='BUY', quantity=10, price=asset.current_price))
    trades.append(Trade.objects.create(asset=asset, date=datetime.date(2024, 5, 3), trade_type='SELL', quantity=5, price=asset.current_price + 10))

# Vytvoření poznámek (Notes)
for trade in trades:
    Note.objects.create(trade=trade, content=f"Trade note for {trade.asset.symbol} on {trade.date}")
    Note.objects.create(trade=trade, content="Second note with additional insight.")

# Vytvoření investic (Investments)
for asset in assets:
    Investment.objects.create(asset=asset, amount_invested=1000.00, date_invested=datetime.date(2024, 4, 15))
