from sqlalchemy import Column, Integer, String
from database import Base

class NoticiaDB(Base):
    __tablename__ = "noticias" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    categoria = Column(String)
    url = Column(String)