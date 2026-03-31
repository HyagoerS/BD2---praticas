from requests import Session
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from models import Curso, Estudante



engine = create_engine("sqlite:///escola.db")
#engine = create_engine("sqlite:///escola.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

with Session() as session:
    curso_eng_comp = Curso(nome="Engenharia de Computação")
    estudante_ana = Estudante(nome="Ana", email="ana@email.com", curso_id=1)
    print("DSebug")
    session.add(curso_eng_comp)
    session.add(estudante_ana)

    session.commit()




#print("Gerando o schema do banco de dados...")

#print("Schema gerado com sucesso!")