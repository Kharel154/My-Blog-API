const API_URL = 'https://My-Blog-API.onrender.com/api/articles';';

document.addEventListener('DOMContentLoaded', fetchArticles);


document.getElementById('articleForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const id = document.getElementById('articleId').value;
    const articleData = {
        titre: document.getElementById('titre').value,
        auteur: document.getElementById('auteur').value,
        date: document.getElementById('date').value,
        categorie: document.getElementById('categorie').value,
        tags: document.getElementById('tags').value,
        contenu: document.getElementById('contenu').value
    };

    
    const url = id ? `${API_URL}/${id}` : API_URL;
    const method = id ? 'PUT' : 'POST';

    try {
        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(articleData)
        });

        if (response.ok) {
            alert(id ? 'Article modifié avec succès !' : 'Article créé avec succès !');
            annulerModification(); 
            fetchArticles(); 
        } else {
            alert("Erreur lors de l'enregistrement.");
        }
    } catch (error) {
        console.error('Erreur:', error);
    }
});


async function fetchArticles() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        afficherArticles(data);
    } catch (error) {
        console.error('Erreur de chargement:', error);
    }
}

function afficherArticles(articles) {
    const conteneur = document.getElementById('articlesList');
    conteneur.innerHTML = '';

    if (articles.length === 0) {
        conteneur.innerHTML = '<p>Aucun article trouvé.</p>';
        return;
    }

    articles.forEach(article => {
        const div = document.createElement('div');
        div.className = 'article-card';
        div.innerHTML = `
            <h3>${article.titre}</h3>
            <p class="meta">Par ${article.auteur} | ${article.categorie}</p>
            <p>${article.contenu.substring(0, 80)}...</p>
            <div class="btn-actions">
                <button class="btn-lire" onclick="lireArticle(${article.id})">👁️ Lire</button>
                <button class="btn-modifier" onclick="preparerModification(${article.id})">📝 Modifier</button>
                <button class="delete-btn" onclick="supprimerArticle(${article.id})">🗑️ Supprimer</button>
            </div>
        `;
        conteneur.appendChild(div);
    });
}


async function lireArticle(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const article = await response.json();
        
        document.getElementById('modalTitre').innerText = article.titre;
        document.getElementById('modalMeta').innerText = `Par ${article.auteur} | Date: ${article.date} | Catégorie: ${article.categorie}`;
        document.getElementById('modalContenu').innerText = article.contenu;
        document.getElementById('modalTags').innerText = `Tags: ${article.tags}`;
        
        document.getElementById('lectureModal').style.display = 'flex';
    } catch (error) {
        console.error('Erreur lors de la lecture:', error);
    }
}

function fermerModal() {
    document.getElementById('lectureModal').style.display = 'none';
}


async function preparerModification(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const article = await response.json();

        
        document.getElementById('articleId').value = article.id;
        document.getElementById('titre').value = article.titre;
        document.getElementById('auteur').value = article.auteur;
        document.getElementById('date').value = article.date;
        document.getElementById('categorie').value = article.categorie;
        document.getElementById('tags').value = article.tags;
        document.getElementById('contenu').value = article.contenu;

        
        document.getElementById('submitBtn').innerText = "Enregistrer la modification";
        document.getElementById('submitBtn').style.backgroundColor = "#f39c12";
        document.getElementById('cancelBtn').style.display = "block";
        
        
        window.scrollTo(0, 0);
    } catch (error) {
        console.error('Erreur lors de la préparation:', error);
    }
}

function annulerModification() {
    document.getElementById('articleForm').reset();
    document.getElementById('articleId').value = '';
    document.getElementById('submitBtn').innerText = "Ajouter l'article";
    document.getElementById('submitBtn').style.backgroundColor = "#2ecc71";
    document.getElementById('cancelBtn').style.display = "none";
}

// 5. SUPPRIMER UN ARTICLE
async function supprimerArticle(id) {
    if(confirm("Voulez-vous vraiment supprimer cet article ?")) {
        try {
            const response = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            if (response.ok) fetchArticles();
        } catch (error) {
            console.error('Erreur lors de la suppression:', error);
        }
    }
}

// RECHERCHER UN ARTICLE
async function searchArticles() {
    const query = document.getElementById('searchInput').value;
    if (!query) return fetchArticles(); // Si c'est vide, on recharge tout

    try {
        const response = await fetch(`${API_URL}/search?query=${query}`);
        const data = await response.json();
        afficherArticles(data);
    } catch (error) {
        console.error('Erreur de recherche:', error);
    }
}
