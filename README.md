# Investiční deník

Aplikace pro sledování investic, jejich transakcí a poznámek. Umožňuje přidávat nové investice, transakce a poznámky přes webové rozhraní.

## Funkce:
- Zobrazování seznamu všech investic
- Detailní zobrazení investice s transakcemi a poznámkami
- Možnost přidávat nové záznamy do aplikace (investice, transakce, poznámky)

## Technologie:
- Django 4.x
- SQLite (pro vývoj)
- Git, GitHub pro verzování

## Jak spustit:
1. Klonujte tento repozitář:
   ```bash
   git clone <URL_REPOZITÁŘE>
   cd investicnidenik
   ```
2. Vytvořte virtuální prostředí:
   ```bash
   python3 -m venv venv
   ```
3. Aktivujte virtuální prostředí a nainstalujte závislosti:
   ```bash
   source venv/bin/activate  # Na Windows použijte `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
4. Spusťte migrace:
   ```bash
   python manage.py migrate
   ```
5. Vytvořte superuživatele:
   ```bash
   python manage.py createsuperuser
   ```
6. Spusťte server:
   ```bash
   python manage.py runserver
   ```

## Další kroky:
- Přihlaste se do administrace na `/admin` a přidejte vzorová data.
- Prozkoumejte aplikaci na `/` a dalších stránkách.

## Dokumentace

### Popis projektu
Investiční deník je webová aplikace postavená na frameworku Django, která umožňuje uživatelům sledovat jejich investice, transakce a poznámky. Aplikace obsahuje následující funkce:

- Úvodní stránka s přehledem aplikace.
- Seznam všech investic.
- Detailní zobrazení investice včetně transakcí a poznámek.
- Možnost přihlášení, registrace a správy uživatelského profilu.
- Administrační dashboard pro správu aplikace.

### Jak spustit projekt

1. Klonujte tento repozitář:
   ```bash
   git clone <URL_REPOZITÁŘE>
   cd investicnidenik
   ```
2. Vytvořte virtuální prostředí:
   ```bash
   python3 -m venv venv
   ```
3. Aktivujte virtuální prostředí a nainstalujte závislosti:
   ```bash
   source venv/bin/activate  # Na Windows použijte `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
4. Spusťte migrace:
   ```bash
   python manage.py migrate
   ```
5. Vytvořte superuživatele:
   ```bash
   python manage.py createsuperuser
   ```
6. Spusťte server:
   ```bash
   python manage.py runserver
   ```

### Struktura aplikace
- **Úvodní stránka**: `/`
- **Seznam investic**: `/investice/`
- **Detail investice**: `/investice/<id>/`
- **Administrační dashboard**: `/admin-dashboard/`

### Požadavky
- Python 3.8+
- Django 4.x

### Autor
Tento projekt byl vytvořen jako součást ročníkového projektu.
