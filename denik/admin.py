from django.contrib import admin
from .models import Investice, Transakce, Poznamka
from .models import Obchod, Poznamka

admin.site.register(Investice)
admin.site.register(Transakce)
admin.site.register(Poznamka)
admin.site.register(Obchod)
