from sqlalchemy import Column, Integer, String

from modelos.base import Base


class Empregado(Base.Base, Base):
    __tablename__ = "empregado"
    nss = Column(Integer, primary_key=True)
    pnome = Column(String, nullable=False)
    mnome = Column(String(50), unique=True)
    snome = Column#(<Domínio e restrições>)
    sexo = Column#(<Domínio e restrições>)
    dataNasc = Column#(<Domínio e restrições>)
    salario = Column#(<Domínio e restrições>)
    endereco = Column#(<Domínio e restrições>)
    numeroDepartamento = Column#(<Domínio e restrições>)
    nssSupervisor = Column#(<Domínio e restrições>)
