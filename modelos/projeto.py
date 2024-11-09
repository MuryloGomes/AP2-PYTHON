from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

from sqlalchemy.orm import relationship

from departamento import Departamento

class Projeto(Base.Base, Base):
    __tablename__ = "projeto"
    numero_Projeto = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    localizacao = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey("numeroDepart"))