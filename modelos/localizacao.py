from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

from sqlalchemy.orm import relationship


class Localizacao(Base.Base, Base):
    __tablename__ = "localizacao"
    localizacaoKey = Column(Integer, primary_key=True, unique=True)
    localizacao = Column(String(50))
    #numeroDepartamento = Column(Integer, ForeignKey("Departamento.numeroDepart."))
