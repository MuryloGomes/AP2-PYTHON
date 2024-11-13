from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from modelos.base import Base

from sqlalchemy.orm import relationship


class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha-em"
    tbkey = Column(Integer, primary_key=True, unique=True)
    #nssEmpregado = Column(Integer, ForeignKey("Empregado.nss"))
    #numeroProjeto = Column(Integer, ForeignKey("Departamento.numeroDepart"))
    horas = Column (DateTime())