from sqlalchemy import Column, Integer, String, ForeignKey, Float

from modelos.base import Base

from datetime import datetime

from departamento import Departamento

from sqlalchemy.orm import relationship

class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True, unique=True)
    pnome = Column(String(50), nullable=False)
    mnome = Column(String(50), unique=True,nullable=False)
    snome = Column(String(50), unique=True,nullable=False) 
    sexo = Column(String(15),nullable=False, nullable=False)
    dataNasc = Column(datetime, nullable=False)
    salario = Column(float, nullable=False)
    endereco = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey("numero_depart"),unique=True)
    nssSupervisor = Column(Integer, ForeignKey(nss))