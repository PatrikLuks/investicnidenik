# investicnidenik/admin.py
from django.contrib import admin
from .models import Asset, Trade, Note, Investment

admin.site.register(Asset)
admin.site.register(Trade)
admin.site.register(Note)
admin.site.register(Investment)
