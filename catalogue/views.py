from django.shortcuts import render
from .models import Categorie, Produit

def home(request):
    # On prend uniquement les catégories racines (ex: Femme)
    categories_principales = Categorie.objects.filter(parent__isnull=True)
    
    # On prend les 4 derniers produits ajoutés pour les coups de cœur
    nouveautes = Produit.objects.order_by('-date_ajout')[:4]
    
    context = {
        'categories': categories_principales,
        'nouveautes': nouveautes,
    }
    return render(request, 'catalogue/index.html', context)