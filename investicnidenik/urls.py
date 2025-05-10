from django.contrib import admin
from django.urls import path, include  # ⬅️ přidáno "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),  # ⬅️ přidáno propojení na frontend.urls
    path('denik/', include('denik.urls')),  # Přidáno propojení na denik.urls
]
