from django.shortcuts import render
from .models import Product

def home(request):
    # On récupère tous les produits de la base de données
    products = Product.objects.all()
    # On les envoie à notre future page HTML
    return render(request, 'catalogue/index.html', {'products': products})