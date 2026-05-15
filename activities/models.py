from django.db import models

# Create your models here.
# models categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    couleur = models.CharField(max_length=7, default='#007bff')  
    datecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

# models Journaux    
class Journal(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    datecreation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    capture = models.ImageField(upload_to='captures/', null=True, blank=True)
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    STATUTS = (
        ('brouillon', 'Brouillon'),
        ('publie', 'Publié'),
        ('resolu', 'Résolu'),
    )
    statut = models.CharField(max_length=20, choices=STATUTS, default='brouillon')

    def __str__(self):
        return self.titre
    

    class Meta:
        ordering = ['-datecreation']
        verbose_name = "Journal"
        verbose_name_plural = "Journaux"

#models Historique des activités    
class HistoriqueActivite(models.Model):

    journal = models.ForeignKey(
        Journal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    deleted_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    message = models.TextField()

    datecreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.message
