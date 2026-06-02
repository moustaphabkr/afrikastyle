from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Nouvelle route pour les catégories (ex: /categorie/femme/ ou /categorie/robes/)
    path('categorie/<slug:slug>/', views.categorie_detail, name='categorie_detail'),
]