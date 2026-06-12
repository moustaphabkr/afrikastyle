from django.db import models
from django.utils.text import slugify

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='sous_categories'
    )

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.nom}"
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1000)
    # Modification : renommage de lien_affiliation en url_affiliation
    url_affiliation = models.URLField(max_length=1000)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    # LA NOUVELLE CASE À COCHER :
    coup_de_coeur = models.BooleanField(default=False, verbose_name="Afficher dans les Coups de Cœur")
    
    categorie = models.ForeignKey(
        Categorie, 
        on_delete=models.CASCADE, 
        related_name='produits'
    )

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom

# Ajout du modèle pour les images additionnelles
class ImageProduit(models.Model):
    produit = models.ForeignKey(
        Produit, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image_url = models.URLField(max_length=1000)