from pydantic import BaseModel, Field
from typing import Optional

class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=1)
    contenu: str = Field(..., min_length=1)
    auteur: str = Field(..., min_length=1)
    date: str
    categorie: str
    tags: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    titre: Optional[str] = None
    contenu: Optional[str] = None
    categorie: Optional[str] = None
    tags: Optional[str] = None

class ArticleResponse(ArticleBase):
    id: int

    class Config:
        from_attributes = True
