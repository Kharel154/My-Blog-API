import os
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Création des tables dans la base de données
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Blog INF222")

# 1. CONFIGURATION CORS (Indispensable pour Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines pour éviter le blocage navigateur
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Dépendance pour la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROUTES API ---

@app.post("/api/articles", response_model=schemas.ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/api/articles", response_model=List[schemas.ArticleResponse])
def read_articles(categorie: Optional[str] = None, date: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_articles(db, categorie=categorie, date=date)

# Route de recherche (Placée AVANT la route avec {id} pour éviter les conflits)
@app.get("/api/articles/search", response_model=List[schemas.ArticleResponse])
def search_articles(query: str, db: Session = Depends(get_db)):
    return crud.search_articles(db, query_text=query)

@app.get("/api/articles/{id}", response_model=schemas.ArticleResponse)
def read_article(id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(db, article_id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return db_article

@app.put("/api/articles/{id}", response_model=schemas.ArticleResponse)
def update_article(id: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = crud.update_article(db, article_id=id, article_data=article)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return db_article

@app.delete("/api/articles/{id}", status_code=status.HTTP_200_OK)
def delete_article(id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return {"message": "Article supprimé avec succès"}

# --- GESTION DU FRONTEND ---

# Route pour servir l'index.html à la racine
@app.get("/")
async def read_index():
    return FileResponse('index.html')

# Montage des fichiers statiques (CSS, JS)
# Note : directory="." signifie que tes fichiers style.css et script.js sont à côté de main.py
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Utilisation de la variable PORT pour Render (8000 par défaut localement)
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
