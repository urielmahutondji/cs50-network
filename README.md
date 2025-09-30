# 🌐 Social Network - Réseau social Django

Projet développé dans le cadre du cours **CS50 Web Programming with Python and JavaScript (CS50W)**.  
L’objectif est de construire un **réseau social complet** permettant aux utilisateurs de publier, suivre d’autres utilisateurs, aimer des publications et interagir via une interface monopage.

---

## 📌 Fonctionnalités principales

- **Gestion des utilisateurs**
  - Inscription, connexion et déconnexion
  - Authentification sécurisée via Django
  - Navigation adaptée selon l’état de connexion

- **Publications**
  - Création d’une nouvelle publication (texte)
  - Affichage chronologique des publications (les plus récentes en premier)
  - Modification d’une publication via une interface JavaScript sans rechargement de page

- **Interactions sociales**
  - Bouton *J’aime / Je n’aime plus* sur chaque publication
  - Mise à jour asynchrone du compteur de likes via `fetch`
  - Commentaires facultatifs (améliorations possibles)

- **Profils utilisateurs**
  - Page profil avec :
    - Nombre d’abonnés et d’abonnements
    - Liste des publications de l’utilisateur
    - Bouton **Suivre / Se désabonner** (sauf pour soi-même)

- **Flux personnalisés**
  - **Tous les posts** : affichage global de toutes les publications
  - **Suivi** : affichage des publications des utilisateurs suivis

- **Pagination**
  - Affichage limité à 10 publications par page
  - Boutons **Précédent / Suivant** pour naviguer entre les pages

- **Interface monopage**
  - Chargement dynamique des contenus avec JavaScript
  - Utilisation des appels API pour gérer les actions utilisateur

---

## 🛠️ Stack technique

- **Backend :** Django (Python)  
- **Frontend :** HTML, CSS, JavaScript (ES6)  
- **Base de données :** SQLite (par défaut)  
- **API REST :** Django views + `fetch` (JSON)  
- **Pagination :** Django `Paginator` + Bootstrap pour l’affichage  

---


## 🚀 Installation et exécution

### 1. Cloner le projet
```bash
git clone https://github.com/urielmahutondji/cs50-network.git
cd cs50-network
````

### 2. Créer et activer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py makemigrations network
python manage.py migrate
```

### 5. Lancer le serveur

```bash
python manage.py runserver
```

Accéder à l’application sur : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 Création d’un superutilisateur

```bash
python manage.py createsuperuser
```

➡ Accès à l’interface admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📝 Spécification respectée

1. Création de nouvelles publications
2. Affichage global de tous les posts
3. Page de profil avec abonnements et abonnés
4. Suivi : affichage des posts des utilisateurs suivis
5. Pagination (10 posts par page)
6. Modification des publications (édition asynchrone via JavaScript)
7. J’aime / Je n’aime plus avec mise à jour asynchrone

---

## 📸 Démonstration

[Voir la vidéo de démonstration](https://youtu.be/6QDxlkusEGM?si=Dn3r0RBa3iv3-Q1j)


---

## 📌 Roadmap (améliorations futures)

* Ajout de commentaires sur les publications
* Notifications en temps réel (WebSockets)
* Amélioration du design avec Bootstrap ou Tailwind
* Déploiement sur une plateforme cloud (Railway, Render, Heroku, etc.)

---

## 📜 Licence

Projet réalisé dans le cadre du **CS50 Web Programming with Python and JavaScript**.
Code disponible sous licence MIT.

---

## 👨‍💻 Auteur

Développé par **urielmahutondji** pour le projet **CS50W Social Network**.

