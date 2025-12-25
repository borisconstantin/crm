# CRM - Customer Relationship Management

Ce projet est une application de gestion de la relation client (CRM) simplifiée, permettant de gérer une base de contacts de manière efficace. L'application repose sur le framework Django et utilise TinyDB comme système de stockage, offrant une alternative légère et flexible aux bases de données SQL traditionnelles.

## Fonctionnalités

- **Gestion des Contacts (CRUD)** : Ajouter, afficher, modifier et supprimer des fiches clients.
- **Stockage NoSQL** : Utilisation de **TinyDB**, une base de données orientée document (format JSON) pour une gestion fluide et portable des données.
- **Interface Utilisateur** : Design moderne et épuré réalisé avec **Bootstrap** pour une expérience utilisateur intuitive.
- **Visualisation dynamique** : Affichage des données sous forme de tableaux interactifs avec gestion du responsive design.

## Architecture Technique

### 1. Backend (Django & TinyDB)
Le projet utilise Django pour la logique de routage et le traitement des requêtes, mais remplace l'ORM standard par **TinyDB** :
- **Manipulation des données** : Les interactions avec la base de données se font directement via des fichiers JSON.
- **Flexibilité** : La structure des contacts peut être adaptée facilement sans migration de base de données complexe.

### 2. Frontend (HTML / CSS / Bootstrap)
- **Modèles de templates** : Utilisation du moteur de templates Django pour l'affichage dynamique des données.
- **Composants Bootstrap** : Utilisation des grilles, des boutons et des formulaires Bootstrap pour assurer la cohérence visuelle.
- **Responsive** : L'interface s'adapte automatiquement à la taille de l'écran (Desktop, Tablette, Mobile).

## Stack Technique

- **Framework Web** : Django (Python)
- **Base de données** : TinyDB
- **Frontend** : HTML5, CSS3, Bootstrap 5
- **Langage de programmation** : Python 3.x

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/borisconstantin/crm.git](https://github.com/borisconstantin/crm.git)
