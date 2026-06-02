from django.shortcuts import render
from .models import Categorie, Produit

def home(request):
    # On récupère uniquement les catégories qui n'ont pas de parent (les catégories racines)
    categories_principales = Categorie.objects.filter(parent__isnull=True)
    
    # Optionnel : On peut aussi récupérer les 4 derniers produits ajoutés pour faire une section "Nouveautés"
    nouveautes = Produit.objects.order_by('-date_ajout')[:4]
    
    context = {
        'categories': categories_principales,
        'nouveautes': nouveautes,
    }
    return render(request, 'catalogue/index.html', context)