from django.contrib import admin

from .models import Categorie, Journal, HistoriqueActivite


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'datecreation'
    )

    search_fields = (
        'nom',
        'description'
    )

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'auteur',
        'categorie',
        'statut',
        'datecreation'
    )

    list_filter = (
        'statut',
        'categorie'
    )

    search_fields = (
        'titre',
        'contenu'
    )


@admin.register(HistoriqueActivite)
class HistoriqueActiviteAdmin(admin.ModelAdmin):

    list_display = (
        'journal',
        'datecreation'
    )