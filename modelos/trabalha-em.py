from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

from datetime import time

from projeto import Projeto

from empregado import Empregado

from sqlalchemy.orm import relationship


class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha-em"
    nssEmpregado = Column(Integer, ForeignKey("nss"))
    numeroProjeto = Column(Integer, ForeignKey("numero_projeto"))
    horas = Column (time())