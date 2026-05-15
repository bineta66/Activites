#!/usr/bin/env python
"""
Script pour peupler la base de données avec des données de test
"""
import os
import django
import random
from datetime import datetime, timedelta

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sta_project.settings')
django.setup()

from activities.models import Categorie, Journal
from django.contrib.auth.models import User

def create_test_data():
    print("Création des données de test...")

    # Créer un utilisateur de test si nécessaire
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("✓ Utilisateur de test créé")

    # Créer des catégories
    categories_data = [
        {'nom': 'Développement', 'description': 'Activités liées au développement logiciel', 'couleur': '#007bff'},
        {'nom': 'Design', 'description': 'Activités de conception et design', 'couleur': '#28a745'},
        {'nom': 'Testing', 'description': 'Activités de test et qualité', 'couleur': '#dc3545'},
        {'nom': 'Documentation', 'description': 'Rédaction de documentation', 'couleur': '#ffc107'},
        {'nom': 'Recherche', 'description': 'Activités de recherche et analyse', 'couleur': '#6f42c1'},
    ]

    categories = []
    for cat_data in categories_data:
        cat, created = Categorie.objects.get_or_create(
            nom=cat_data['nom'],
            defaults=cat_data
        )
        categories.append(cat)
        if created:
            print(f"✓ Catégorie '{cat.nom}' créée")

    # Créer des journaux de test
    journals_data = [
        {
            'titre': 'Implémentation de l\'authentification',
            'contenu': 'Aujourd\'hui, j\'ai travaillé sur l\'implémentation du système d\'authentification. J\'ai utilisé Django\'s authentication framework avec des vues basées sur des classes. Le système inclut l\'inscription, la connexion et la déconnexion des utilisateurs.',
            'categorie': categories[0],  # Développement
            'statut': 'publie'
        },
        {
            'titre': 'Conception de l\'interface utilisateur',
            'contenu': 'J\'ai conçu les maquettes pour le dashboard principal. L\'interface utilise Bootstrap 5 pour un design responsive. Le dashboard affiche les statistiques des activités, la liste des tâches récentes et un timeline des événements.',
            'categorie': categories[1],  # Design
            'statut': 'publie'
        },
        {
            'titre': 'Tests unitaires des modèles',
            'contenu': 'J\'ai écrit et exécuté les tests unitaires pour tous les modèles Django. Les tests couvrent les méthodes de création, modification et suppression des objets, ainsi que les relations entre modèles.',
            'categorie': categories[2],  # Testing
            'statut': 'publie'
        },
        {
            'titre': 'Rédaction du guide utilisateur',
            'contenu': 'J\'ai commencé la rédaction du guide utilisateur pour l\'application STA. Le guide couvre l\'installation, la configuration et l\'utilisation de base de la plateforme de traçabilité d\'activités.',
            'categorie': categories[3],  # Documentation
            'statut': 'brouillon'
        },
        {
            'titre': 'Analyse des besoins métier',
            'contenu': 'J\'ai analysé les besoins métier pour l\'amélioration du système de traçabilité. Les utilisateurs ont besoin de rapports plus détaillés et d\'une meilleure visualisation des données d\'activité.',
            'categorie': categories[4],  # Recherche
            'statut': 'publie'
        },
        {
            'titre': 'Optimisation des performances',
            'contenu': 'J\'ai optimisé les requêtes de base de données en ajoutant des index appropriés et en utilisant select_related/prefetch_related pour réduire le nombre de requêtes SQL.',
            'categorie': categories[0],  # Développement
            'statut': 'publie'
        },
        {
            'titre': 'Tests d\'intégration',
            'contenu': 'J\'ai mis en place des tests d\'intégration pour vérifier le fonctionnement complet du système. Les tests couvrent les workflows complets depuis la création d\'un journal jusqu\'à sa publication.',
            'categorie': categories[2],  # Testing
            'statut': 'brouillon'
        },
        {
            'titre': 'Recherche sur les technologies frontend',
            'contenu': 'J\'ai étudié différentes technologies frontend pour améliorer l\'expérience utilisateur. Les options envisagées incluent React, Vue.js et Angular, ainsi que des frameworks CSS comme Tailwind.',
            'categorie': categories[4],  # Recherche
            'statut': 'publie'
        }
    ]

    for journal_data in journals_data:
        journal, created = Journal.objects.get_or_create(
            titre=journal_data['titre'],
            auteur=user,
            defaults=journal_data
        )
        if created:
            print(f"✓ Journal '{journal.titre}' créé")

    print("\nDonnées de test créées avec succès !")
    print(f"- {len(categories)} catégories")
    print(f"- {len(journals_data)} journaux")
    print(f"- Utilisateur de test: testuser / testpass123")

if __name__ == '__main__':
    create_test_data()