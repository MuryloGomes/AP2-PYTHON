from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Dependente(Base.Base, Base):
    __tablename__ = "dependente"
    nssEmpregado = Column#(<Domínio e restrições>)
    nome = Column#(<Domínio e restrições>)
    sexo = Column#(<Domínio e restrições>)
    dataNasc = Column#(<Domínio e restrições>)
    tipoRelacionamento = Column#(<Domínio e restrições>)