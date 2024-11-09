from sqlalchemy import Column, Integer, String, ForeignKey, INTEGER

from modelos.base import Base

from datetime import datetime

from empregado import Empregado 

from sqlalchemy.orm import relationship



class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    nssEmpregado = Column(Integer,ForeignKey("nss"),unique=True )
    nome = Column(String(50))
    sexo = Column(String(15))
    dataNasc = Column(datetime)
    tipoRelacionamento = Column(String(50))