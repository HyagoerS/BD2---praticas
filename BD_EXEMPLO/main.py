from requests import Session
from sqlalchemy import create_engine
from sqlalchemy import select
#from models import Base
from sqlalchemy.orm import sessionmaker
from models import Curso, Estudante



engine = create_engine("sqlite:///escola.db")
#engine = create_engine("sqlite:///escola.db", echo=True)
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
''''
with Session() as session:
    curso_eng_comp = Curso(nome="Engenharia de Computação")
    
    estudante_ana = Estudante(nome="Ana", email="ana@email.com", curso_id=1)
    estudante_joao = Estudante(nome="João", email="joao@email.com", curso_id=1)
    estudante_maria = Estudante(nome="Maria", email="maria@email.com", curso_id=1)
    estudante_pedro = Estudante(nome="Pedro", email="pedro@email.com", curso_id=1)
    
    session.add(curso_eng_comp)

    session.add(estudante_ana)
    session.add(estudante_joao)
    session.add(estudante_maria)
    session.add(estudante_pedro)

    session.commit()
'''
with Session() as session:
    query = select(Estudante)

    estudantes = session.execute(query).scalars().all()

    for estudante in estudantes:
        print(estudante)




#print("Gerando o schema do banco de dados...")

#print("Schema gerado com sucesso!")