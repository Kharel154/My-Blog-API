import os
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Blog INF222")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/api/articles", response_model=schemas.ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/api/articles", response_model=List[schemas.ArticleResponse])
def read_articles(categorie: Optional[str] = None, date: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_articles(db, categorie=categorie, date=date)


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




@app.get("/")
async def read_index():
    return FileResponse('index.html')



app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
