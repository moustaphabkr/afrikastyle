from django.contrib import admin
from .models import Category, Product

# On dit à Django d'afficher les catégories et les produits dans le panneau d'administration
admin.site.register(Category)
admin.site.register(Product)