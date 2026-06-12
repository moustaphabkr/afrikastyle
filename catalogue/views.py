from django.shortcuts import render, get_object_or_404
from .models import Categorie, Produit

def home(request):
    categories_principales = Categorie.objects.filter(parent__isnull=True)
    
    # FILTRE : Uniquement les produits cochés "coup_de_coeur"
    coups_de_coeur = Produit.objects.filter(coup_de_coeur=True).order_by('-date_ajout')
    
    context = {
        'categories': categories_principales,
        'nouveautes': coups_de_coeur,
    }
    return render(request, 'catalogue/index.html', context)


def categorie_detail(request, slug):
    # Correction ici : get_object_or_404 au lieu de 400
    categorie_actuelle = get_object_or_404(Categorie, slug=slug)
    
    # On récupère ses sous-catégories directes (ex: Femme -> Vêtements, Accessoires)
    sous_categories = categorie_actuelle.sous_categories.all()
    
    # Récupération en cascade de tous les produits de la branche
    categories_liees = [categorie_actuelle]
    
    # On cherche les enfants (niveau 2)
    for enfant in sous_categories:
        categories_liees.append(enfant)
        # On cherche les petits-enfants (niveau 3, ex: Robes)
        for petit_enfant in enfant.sous_categories.all():
            categories_liees.append(petit_enfant)
            
    # On filtre tous les produits qui appartiennent à ces catégories
    produits = Produit.objects.filter(categorie__in=categories_liees).order_by('-date_ajout')
    
    context = {
        'categorie': categorie_actuelle,
        'sous_categories': sous_categories,
        'produits': produits,
    }
    return render(request, 'catalogue/categorie.html', context)

def produit_detail(request, slug):
    # On récupère le produit grâce à son slug unique
    produit = get_object_or_404(Produit, slug=slug)
    
    context = {
        'produit': produit,
    }
    return render(request, 'catalogue/produit.html', context)