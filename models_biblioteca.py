from sqlalchemy import(
    create_engine, Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Autor():
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)


class Livro():
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    autor_id = Column(Integer, ForeignKey('autores.id'), nullable=False)

    def __repr__(self):
        return f"Autor(id={self.id}, nome='{self.nome}')"

    def __repr__(self):
        return f"Livro(id={self.id}, nome='{self.nome}')"