from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Departamento(Base.Base, Base):
    __tablename__ = "departamento"
    numero = Column#(<Domínio e restrições>)
    nome = Column#(<Domínio e restrições>)
    numeroEmpregado = Column#(<Domínio e restrições>)
    nssEmpregrado = Column#(<Domínio e restrições>)
    dataInicio = Column#(<Domínio e restrições>)