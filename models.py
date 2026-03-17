from sqlalchemy import(
    create_engine, Column, Integer, String, Date, ForeignKey
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Curso(Base):
    __tablename__ = 'cursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullabel=False, unique=True)

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    curso_id = Column(Integer, ForeignKey('cursos.id'), nullable=False)

    def __repr__(self):
        return f"Estudante(id={self.id}, nome='{self.nome}')"