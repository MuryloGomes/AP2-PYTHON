from sqlalchemy import Column, Integer, String, ForeignKey, INTEGER, DateTime

from modelos.base import Base

from sqlalchemy.orm import relationship

class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    #nssEmpregado = Column(Integer,ForeignKey("Empregado.nss"),unique=True )
    numeroDependente = Column(Integer,primary_key=True, unique=True)
    nome = Column(String(50))
    sexo = Column(String(15))
    dataNasc = Column(DateTime)
    tipoRelacionamento = Column(String(50))