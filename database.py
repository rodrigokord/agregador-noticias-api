from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define que vamos usar o SQLite e cria um arquivo chamado noticias.db na sua pasta
URL_BANCO_DADOS = "sqlite:///./noticias.db"

# Cria o "motor" que executa os comandos no banco
engine = create_engine(URL_BANCO_DADOS, connect_args={"check_same_thread": False})

# Inicia a sessão (como se fosse abrir a porta para ler ou gravar dados)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para criarmos a estrutura da tabela no próximo passo
Base = declarative_base()