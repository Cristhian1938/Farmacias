from django.shortcuts import render
from .models import Inventario, Pedido

def base(request):
    return render(request, 'base.html')

def inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventario': inventario})

def pedidos_view(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})
