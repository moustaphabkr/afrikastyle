from django.contrib import admin
from .models import Categorie, Produit, ImageProduit

# Ajout de la configuration pour les images multiples
class ImageProduitInline(admin.TabularInline):
    model = ImageProduit
    extra = 1  # Affiche 1 case vide par défaut pour ajouter une image

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'parent', 'slug']
    prepopulated_fields = {'slug': ('nom',)} # Remplit le slug tout seul pendant que tu tapes le nom
    list_filter = ['parent']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie']
    list_filter = ['categorie']
    # On indique à Django d'afficher les images additionnelles ici
    inlines = [ImageProduitInline]