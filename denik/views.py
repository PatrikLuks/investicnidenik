from django.shortcuts import render
from .models import TvéModely

def seznam_objektů(request):
    objekty = TvéModely.objects.all()  # Získej všechny objekty
    return render(request, 'seznam.html', {'objekty': objekty})

def detail_objektu(request, id):
    objekt = TvéModely.objects.get(id=id)  # Získej jeden objekt podle ID
    return render(request, 'detail.html', {'objekt': objekt})
