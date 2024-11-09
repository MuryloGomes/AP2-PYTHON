from sqlalchemy import Column, Integer, String, ForeignKey

from modelos.base import Base

from departamento import Departamento

from sqlalchemy.orm import relationship


class Localizacao(Base.Base, Base):
    __tablename__ = "localizacao"
    localizacao = Column(String(50))
    numeroDepartamento = Column(Integer, ForeignKey("numeroDepart"))
