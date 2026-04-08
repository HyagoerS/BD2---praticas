from sqlalchemy import create_engine
from models_biblioteca import Base

engine = create_engine("sqlite:///biblioteca.db", echo=True)

print("Gerando o schema (biblioteca) do banco de dados...")
Base.metadata.create_all(engine)
print("Schema da biblioteca gerado com sucesso!")