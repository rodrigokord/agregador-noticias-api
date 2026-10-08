from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

# Ao rodar, isso cria o arquivo noticias.db fisicamente se ele não existir
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agregador de Notícias - Editora Esfera")

# Esquema de validação (como os dados devem chegar para nós)
class NoticiaCreate(BaseModel):
    titulo: str
    categoria: str
    url: str

# Função que abre e fecha a conexão de forma segura a cada uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "API conectada ao banco de dados com sucesso!"}

@app.post("/noticias")
def adicionar_noticia(noticia: NoticiaCreate, db: Session = Depends(get_db)):
    # Converte a notícia enviada para o formato que o banco entende e salva
    nova_noticia = models.NoticiaDB(titulo=noticia.titulo, categoria=noticia.categoria, url=noticia.url)
    db.add(nova_noticia)
    db.commit()
    db.refresh(nova_noticia)
    return {"mensagem": "Notícia salva no banco!", "dados": nova_noticia}

@app.get("/noticias")
def listar_noticias(db: Session = Depends(get_db)):
    # Consulta e retorna todas as linhas da tabela "noticias"
    return db.query(models.NoticiaDB).all()