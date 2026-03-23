from sqlalchemy.orm import Session
import models, schemas

def get_articles(db: Session, categorie: str = None, date: str = None):
    query = db.query(models.Article)
    if categorie:
        query = query.filter(models.Article.categorie == categorie)
    if date:
        query = query.filter(models.Article.date == date)
    return query.all()

def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def search_articles(db: Session, query_text: str):
    if query_text.isdigit():
        return db.query(models.Article).filter(models.Article.id == int(query_text)).all()
    
    return db.query(models.Article).filter(
        (models.Article.titre.contains(query_text)) | 
        (models.Article.contenu.contains(query_text))
    ).all()

def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article_id: int, article_data: schemas.ArticleUpdate):
    db_article = get_article(db, article_id)
    if db_article:
        update_data = article_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = get_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article
