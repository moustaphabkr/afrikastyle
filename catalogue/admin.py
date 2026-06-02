from django.contrib import admin
from .models import Categorie, Produit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'parent', 'slug']
    prepopulated_fields = {'slug': ('nom',)} # Remplit le slug tout seul pendant que tu tapes le nom
    list_filter = ['parent']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie']
    list_filter = ['categorie']