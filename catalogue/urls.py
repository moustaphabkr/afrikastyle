from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categorie/<slug:slug>/', views.categorie_detail, name='categorie_detail'),
]