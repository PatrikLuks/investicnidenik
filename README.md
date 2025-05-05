# 📈 Investiční deník

Tato webová aplikace vytvořená v Djangu slouží jako osobní investiční deník. Umožňuje sledování obchodů, aktiv, výnosů a poznámek k investičním rozhodnutím.

## 🧠 Funkce
- Přehled investičních aktiv (např. akcie, krypto, fondy, atd.)
- Záznam jednotlivých obchodů (nákup/prodej)
- Výpočet výnosů a ztrát
- Možnost přidávat vlastní poznámky k obchodům
- Administrace dat přes Django admin

## 🧱 Použité technologie
- Python 3
- Django 5
- SQLite (pro vývoj)
- HTML, CSS (základní šablony)

## 🔧 Instalace
```bash
git clone https://github.com/PatrikLuks/investicnidenik.git
cd investicnidenik
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
