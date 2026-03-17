from sqlalchemy import(
    create_engine, Column, Integer, String, Float, Boolean
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float(10), nullable=False)
    em_estoque = Column(Boolean, default=True)