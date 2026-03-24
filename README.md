# My-Blog-API

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Framework](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange)

Ce projet est une application web Fullstack permettant de gérer des articles de blog de manière interactive. Développé dans le cadre de l'unité d'enseignement **INF222** à l'**Université de Yaoundé I**.

---

## 🌐 1. Lien du Projet (Déploiement)
L'application est hébergée sur la plateforme Cloud Render et est accessible via l'URL suivante :
👉 **Lien direct :** [https://my-blog-api-usc5.onrender.com/](https://my-blog-api-usc5.onrender.com/)

---

## 🛠️ 2. Installation et Configuration locale

### Prérequis
* Python 3.10 ou version ultérieure
* Git

### Étapes d'installation (Ubuntu / Terminal)
1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/Kharel154/My-Blog-API.git](https://github.com/Kharel154/My-Blog-API.git)
   cd My-Blog-API
2. **Créer et activer l'environnement virtuel :** 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    
3. **Installer les dépendances :**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic

4. **Lancer le serveur de développement :**
   ```bash
   python3 main.py
  <img width="976" height="586" alt="Screenshot from 2026-03-23 00-48-30" src="https://github.com/user-attachments/assets/76a305f7-557f-4c68-ac09-f8a150bfb527" />


## 🛰️ 3. Endpoints de l'API REST

L'API suit les standards REST pour la communication entre le client et le serveur. Voici la liste des points de terminaison disponibles :

### Table des Endpoints
| Méthode | Endpoint | Action | Description |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/articles` | Liste | Récupère tous les articles de la base de données. |
| **POST** | `/api/articles` | Création | Ajoute un nouvel article (titre, auteur, contenu, catégorie). |
| **GET** | `/api/articles/{id}` | Lecture | Récupère les détails d'un article spécifique via son ID. |
| **PUT** | `/api/articles/{id}` | Mise à jour | Modifie les informations d'un article existant. |
| **DELETE** | `/api/articles/{id}` | Suppression | Retire un article définitivement de la base de données. |
| **GET** | `/api/articles/search` | Recherche | Filtre les articles par mots-clés dans le titre ou le contenu. |

### Documentation Interactive
FastAPI génère automatiquement une documentation interactive (Swagger UI) qui permet de tester ces points de terminaison sans outil externe.
👉 **Accès :** `https://my-blog-api-usc5.onrender.com/docs`
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-53-54" src="https://github.com/user-attachments/assets/7b5e56d2-79ec-4e82-b7be-18579da0bf68" />

<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-43-07" src="https://github.com/user-attachments/assets/837fe618-4b38-4cad-8427-c9a904d0211e" />

<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-45-20" src="https://github.com/user-attachments/assets/d00fd504-c7c4-480f-949c-5c97ca7275b4" />

<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-46-39" src="https://github.com/user-attachments/assets/de0be597-2b42-4802-a925-77a7a26cba4e" />

<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-48-23" src="https://github.com/user-attachments/assets/fe71f38c-6497-4252-8c7d-99fe7dbd0a9b" />
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-50-23" src="https://github.com/user-attachments/assets/fecc8f59-adda-4565-977c-50483f9c01e9" />

<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-52-07" src="https://github.com/user-attachments/assets/782717b4-8997-417f-877b-34a98cc7de5e" />
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-52-17" src="https://github.com/user-attachments/assets/6d8976b3-cdce-43ca-8995-cf5af5ee897b" />
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-52-43" src="https://github.com/user-attachments/assets/45cc47b7-9c13-4327-a97f-696d710aa861" />

#### Format des Données (Schéma JSON)
Pour les requêtes **POST** et **PUT**, le corps de la requête doit respecter la structure suivante :

    ```json
    {
      "titre": "Titre de l'article",
      "auteur": "Nom de l'auteur",
      "contenu": "Contenu détaillé",
      "categorie": "Informatique"
    }


##  4. Interface et Utilisation

L'interface utilisateur a été conçue pour être intuitive, moderne et entièrement réactive (Responsive Design). Elle permet une gestion fluide des articles sans rechargement de la page grâce à l'utilisation intensive de requêtes asynchrones.

### 4.1. Présentation de l'Interface (Frontend) et Exemple d'Utilisation
L'application propose un **"Dark Mode"** natif pour un meilleur confort visuel. À gauche, un formulaire permet la saisie des données, tandis qu'à droite, la liste des articles se met à jour dynamiquement.

L'interface de l'app de blog
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-25-11" src="https://github.com/user-attachments/assets/611ee143-1fb2-4a4c-b861-0e66fdbbfc96" />



Pour creer un article, vous remplisez les info demander et clickez sur Ajouter l'article
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-25-22" src="https://github.com/user-attachments/assets/4074fcf9-1aff-4974-9cf7-96082bae6965" />


Voici l'article ajouter en bas
<img width="1920" height="1080" alt="Screenshot from 2026-03-23 21-25-38" src="https://github.com/user-attachments/assets/41084ad6-0d02-441e-81d6-c73801ce2870" />



### 4.2. Logique d'Utilisation (CRUD)
Le fichier `script.js` gère les interactions principales via l'API **Fetch** :

1.  **Affichage :** Au chargement de la page, une requête `GET` récupère tous les articles en base de données.
2.  **Création :** Lors de la soumission du formulaire, les données sont envoyées via une requête `POST` au format JSON.
3.  **Lecture :** Un clic sur un article ouvre une fenêtre modale affichant le contenu complet récupéré dynamiquement.
4.  **Suppression :** Chaque article possède un bouton permettant d'envoyer une requête `DELETE` au serveur.

