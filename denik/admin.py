from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Investice, Transakce, Poznamka, Obchod
from .models import create_default_groups, UserActivityLog, Notification

# Vytvoření výchozích skupin při spuštění adminu
create_default_groups()

admin.site.register(Investice)
admin.site.register(Transakce)
admin.site.register(Poznamka)
admin.site.register(Obchod)

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')
