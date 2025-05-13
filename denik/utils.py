import requests

def get_stock_price(symbol):
    """Získá aktuální cenu akcie pomocí API."""
    api_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=YOUR_API_KEY"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("Global Quote", {}).get("05. price", None)
    return None
