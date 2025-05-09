from django.contrib import admin
from .models import Investice, Transakce, Poznamka

admin.site.register(Investice)
admin.site.register(Transakce)
admin.site.register(Poznamka)
