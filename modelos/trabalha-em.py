from sqlalchemy import Column, Integer, String

from modelos.base import Base


class TrabalhaEm(Base.Base, Base):
    __tablename__ = "trabalha-em"
    nssEmpregado = Column#(<Domínio e restrições>)
    numeroProjeto = Column#(<Domínio e restrições>)
    horas = Column#(<Domínio e restrições>)