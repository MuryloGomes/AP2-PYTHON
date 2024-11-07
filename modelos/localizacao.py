from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Localizacao(Base.Base, Base):
    __tablename__ = "localizacao"
    localizacao = Column#(<Domínio e restrições>)
    numeroDepartamento = Column#(<Domínio e restrições>)
