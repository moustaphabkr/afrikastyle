from django.db import models
from django.utils.text import slugify

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    # Le slug permet d'avoir de belles URL (ex: femme-accessoires-sacs)
    slug = models.SlugField(unique=True, blank=True)
    
    # LA LIGNE MAGIQUE : Une catégorie peut pointer vers une catégorie parente
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
        # Génère automatiquement le slug si on ne le remplit pas
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        # Affichage propre dans l'admin (ex: Femme > Accessoires > Sacs)
        if self.parent:
            return f"{self.parent} > {self.nom}"
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    # ... tes autres champs actuels (image, lien d'affiliation, etc.) ...
    
    # On lie le produit à sa catégorie finale (ex: un sac sera lié directement à la sous-catégorie 'Sacs')
    categorie = models.ForeignKey(
        Categorie, 
        on_delete=models.CASCADE, 
        related_name='produits'
    )

    def __str__(self):
        return self.nom