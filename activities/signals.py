from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Journal



@receiver(post_save, sender=Journal)
def log_journal_change(sender, instance, created, **kwargs):

    if created:

        print(
            
            f"NOUVELLE NOTE CRÉÉE | "
            f"Auteur: {instance.auteur.username} | "
            f"Titre: {instance.titre} | "
            f"Catégorie: {instance.categorie.nom} | "
            f"Statut: {instance.get_statut_display()} | "
            f"Date: {instance.datecreation}"
        )

    else:

        print(
            f"\nNOTE MODIFIÉE | "
            f"Auteur: {instance.auteur.username} | "
            f"Titre: {instance.titre}\n |"
             f"Catégorie: {instance.categorie.nom} |\n"
            f"datecreation:{instance.datecreation}"
        )


# SUPPRESSION
@receiver(pre_delete, sender=Journal)
def log_journal_deletion(sender, instance, **kwargs):

    print(
        f"\n NOTE SUPPRIMÉE | "
        f"Auteur: {instance.auteur.username} | "
        f"Titre: {instance.titre}\n"
    )